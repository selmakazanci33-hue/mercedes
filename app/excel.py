import sqlite3
from pathlib import Path
import pandas as pd


SQLITE_DB_PATH = Path("data/issuer_834.db")
OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_EXCEL = OUTPUT_DIR / "enrollment_lifecycle_engine_jan_may_2026.xlsx"

HISTORY_MONTHS = [
    ("2025", "10"), ("2025", "11"), ("2025", "12"),
    ("2026", "01"), ("2026", "02"), ("2026", "03"), ("2026", "04"), ("2026", "05"),
]

REPORT_MONTHS = [
    ("2026", "01"), ("2026", "02"), ("2026", "03"), ("2026", "04"), ("2026", "05"),
]


def get_events():
    where_sql = " OR ".join(
        [f"(year = '{y}' AND month = '{m}')" for y, m in HISTORY_MONTHS]
    )

    sql = f"""
    SELECT
        issuer,
        year,
        month,
        policy_id,
        member_id,
        subscriber_id,
        household_or_employee_case_id AS household_id,
        insurance_type_code,
        additional_maint_reason_code,
        subscriber_flag,
        relationship,
        benefit_effective_date,
        benefit_end_date,
        member_maint_effective_date,
        raw_xml_path
    FROM stg_834_records
    WHERE ({where_sql})
      AND additional_maint_reason_code IN ('CONFIRM', 'REINSTATE', 'CANCEL', 'TERM')
    """

    conn = sqlite3.connect(SQLITE_DB_PATH)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def clean_events(df):
    df = df.copy()

    df["issuer"] = df["issuer"].astype(str)
    df["year"] = df["year"].astype(str)
    df["month"] = df["month"].astype(str).str.zfill(2)

    df["status"] = df["additional_maint_reason_code"].replace({
        "REINSTATE": "CONFIRM"
    })

    df["insurance_type"] = df["insurance_type_code"].apply(
        lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
    )

    for col in ["policy_id", "member_id", "subscriber_id", "household_id"]:
        df[col] = df[col].astype(str).replace(["None", "nan", "NaN", ""], pd.NA)

    df["enrollment_key"] = df["policy_id"].fillna(df["subscriber_id"]).fillna(df["household_id"])

    # Person-level key: this is where we resolve old policy vs new policy
    df["person_key"] = (
        df["issuer"].astype(str) + "|" +
        df["insurance_type"].astype(str) + "|" +
        df["member_id"].astype(str)
    )

    df["benefit_effective_date"] = pd.to_datetime(df["benefit_effective_date"], errors="coerce")
    df["benefit_end_date"] = pd.to_datetime(df["benefit_end_date"], errors="coerce")
    df["member_maint_effective_date"] = pd.to_datetime(df["member_maint_effective_date"], errors="coerce")

    df["file_month_date"] = pd.to_datetime(df["year"] + "-" + df["month"] + "-01", errors="coerce")

    df["event_date"] = (
        df["member_maint_effective_date"]
        .fillna(df["benefit_effective_date"])
        .fillna(df["file_month_date"])
    )

    df["status_rank"] = df["status"].map({
        "CONFIRM": 4,
        "REINSTATE": 4,
        "CANCEL": 3,
        "TERM": 2
    }).fillna(1)

    return df


def month_bounds(year, month):
    start = pd.Timestamp(f"{year}-{month}-01")
    end = start + pd.offsets.MonthEnd(0)
    return start, end


def build_lifecycle_states(events):
    all_states = []

    for report_year, report_month in REPORT_MONTHS:
        report_start, report_end = month_bounds(report_year, report_month)

        eligible = events[events["event_date"] <= report_end].copy()

        if eligible.empty:
            continue

        eligible["coverage_active_in_month"] = (
            (eligible["benefit_effective_date"].isna() | (eligible["benefit_effective_date"] <= report_end))
            &
            (eligible["benefit_end_date"].isna() | (eligible["benefit_end_date"] >= report_start))
        )

        # Step 1: latest event per policy/member
        eligible = eligible.sort_values([
            "person_key",
            "enrollment_key",
            "event_date",
            "benefit_effective_date",
            "benefit_end_date",
            "status_rank",
            "raw_xml_path"
        ])

        latest_policy_state = eligible.drop_duplicates(
            ["person_key", "enrollment_key"],
            keep="last"
        ).copy()

        # Step 2: resolve current policy per person
        # If same member exists on multiple policies, choose latest valid enrollment.
        latest_policy_state["policy_priority_date"] = (
            latest_policy_state["benefit_effective_date"]
            .fillna(latest_policy_state["event_date"])
        )

        current = latest_policy_state.sort_values([
            "person_key",
            "coverage_active_in_month",
            "policy_priority_date",
            "event_date",
            "status_rank",
            "enrollment_key"
        ]).drop_duplicates("person_key", keep="last").copy()

        current["report_year"] = report_year
        current["report_month"] = report_month
        current["report_start"] = report_start
        current["report_end"] = report_end

        current["months_since_event"] = (
            (report_end.year - current["event_date"].dt.year) * 12
            + (report_end.month - current["event_date"].dt.month)
        )

        current["business_status"] = current["status"]

        # 3-month cancellation rule
        current.loc[
            (current["status"] == "CANCEL") &
            (current["months_since_event"] >= 3),
            "business_status"
        ] = "TERM"

        # If coverage is not active and latest status was CONFIRM, mark as TERM-like business state
        current.loc[
            (current["coverage_active_in_month"] == False) &
            (current["business_status"] == "CONFIRM") &
            (current["benefit_end_date"].notna()) &
            (current["benefit_end_date"] < report_start),
            "business_status"
        ] = "TERM"

        all_states.append(current)

    if not all_states:
        return pd.DataFrame()

    return pd.concat(all_states, ignore_index=True)


def summarize_current(states, status_col, prefix):
    return (
        states.groupby(
            ["issuer", "report_year", "report_month", "insurance_type", status_col],
            dropna=False
        )
        .agg(
            **{
                f"{prefix}_person_count": ("person_key", "nunique"),
                f"{prefix}_enrollment_count": ("enrollment_key", "nunique"),
                f"{prefix}_enrollee_count": ("member_id", "nunique"),
                f"{prefix}_subscriber_count": ("subscriber_id", "nunique"),
            }
        )
        .reset_index()
        .rename(columns={
            "report_year": "year",
            "report_month": "month",
            status_col: "status"
        })
        .sort_values(["issuer", "year", "month", "insurance_type", "status"])
    )


def issuer_month_summary(states, status_col, prefix):
    return (
        states.groupby(["issuer", "report_year", "report_month"], dropna=False)
        .agg(
            **{
                f"{prefix}_person_count": ("person_key", "nunique"),
                f"{prefix}_enrollment_count": ("enrollment_key", "nunique"),
                f"{prefix}_enrollee_count": ("member_id", "nunique"),
                f"{prefix}_subscriber_count": ("subscriber_id", "nunique"),
                f"{prefix}_confirm_count": (status_col, lambda x: (x == "CONFIRM").sum()),
                f"{prefix}_cancel_count": (status_col, lambda x: (x == "CANCEL").sum()),
                f"{prefix}_term_count": (status_col, lambda x: (x == "TERM").sum()),
            }
        )
        .reset_index()
        .rename(columns={
            "report_year": "year",
            "report_month": "month"
        })
        .sort_values(["issuer", "year", "month"])
    )


def raw_month_summary(events):
    return (
        events[events[["year", "month"]].apply(tuple, axis=1).isin(REPORT_MONTHS)]
        .groupby(["issuer", "year", "month"], dropna=False)
        .agg(
            raw_rows=("member_id", "size"),
            raw_enrollment_count=("enrollment_key", "nunique"),
            raw_enrollee_count=("member_id", "nunique"),
            raw_subscriber_count=("subscriber_id", "nunique"),
            raw_file_count=("raw_xml_path", "nunique"),
        )
        .reset_index()
        .sort_values(["issuer", "year", "month"])
    )


def compare_raw_vs_lifecycle(raw_summary, lifecycle_summary):
    comp = pd.merge(
        raw_summary,
        lifecycle_summary,
        how="outer",
        on=["issuer", "year", "month"]
    ).fillna(0)

    numeric_cols = [c for c in comp.columns if c.endswith("_count") or c.endswith("_rows")]
    for col in numeric_cols:
        comp[col] = comp[col].astype(int)

    comp["enrollment_reduction"] = comp["raw_enrollment_count"] - comp["business_enrollment_count"]
    comp["enrollee_reduction"] = comp["raw_enrollee_count"] - comp["business_enrollee_count"]
    comp["subscriber_reduction"] = comp["raw_subscriber_count"] - comp["business_subscriber_count"]

    return comp.sort_values(["issuer", "year", "month"])


def lifecycle_quality_checks(events, states):
    multi_policy_members = (
        events.groupby(["issuer", "insurance_type", "member_id"], dropna=False)
        .agg(
            policy_count=("enrollment_key", "nunique"),
            event_rows=("member_id", "size"),
            first_event=("event_date", "min"),
            last_event=("event_date", "max"),
        )
        .reset_index()
        .query("policy_count > 1")
        .sort_values(["policy_count", "event_rows"], ascending=False)
        .head(1000)
    )

    superseded_candidates = (
        states.groupby(["issuer", "report_year", "report_month"], dropna=False)
        .agg(
            current_persons=("person_key", "nunique"),
            current_enrollments=("enrollment_key", "nunique"),
            confirm=("business_status", lambda x: (x == "CONFIRM").sum()),
            cancel=("business_status", lambda x: (x == "CANCEL").sum()),
            term=("business_status", lambda x: (x == "TERM").sum()),
        )
        .reset_index()
        .rename(columns={"report_year": "year", "report_month": "month"})
    )

    return multi_policy_members, superseded_candidates


def write_excel(path, sheets):
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for sheet_name, df in sheets.items():
            safe = sheet_name[:31]
            if df is None or df.empty:
                pd.DataFrame({"message": ["No data"]}).to_excel(writer, sheet_name=safe, index=False)
            else:
                df.head(1_048_000).to_excel(writer, sheet_name=safe, index=False)

        for sheet in writer.book.sheetnames:
            ws = writer.book[sheet]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions

            for col in ws.columns:
                width = min(max(len(str(cell.value)) if cell.value is not None else 0 for cell in col) + 2, 45)
                ws.column_dimensions[col[0].column_letter].width = width


def main():
    print("Reading events...")
    raw = get_events()
    print(f"Raw events: {len(raw)}")

    print("Cleaning events...")
    events = clean_events(raw)

    print("Building lifecycle states...")
    states = build_lifecycle_states(events)
    print(f"Lifecycle states: {len(states)}")

    print("Creating summaries...")
    raw_summary = raw_month_summary(events)

    lifecycle_latest_status = summarize_current(states, "status", "latest")
    lifecycle_business_status = summarize_current(states, "business_status", "business")

    issuer_month_latest = issuer_month_summary(states, "status", "latest")
    issuer_month_business = issuer_month_summary(states, "business_status", "business")

    comparison = compare_raw_vs_lifecycle(raw_summary, issuer_month_business)

    multi_policy_members, lifecycle_check = lifecycle_quality_checks(events, states)

    print("Writing Excel...")
    write_excel(
        OUTPUT_EXCEL,
        {
            "Raw_vs_Lifecycle_Compare": comparison,
            "Issuer_Month_Business": issuer_month_business,
            "Issuer_Month_Latest": issuer_month_latest,
            "Lifecycle_Business_Status": lifecycle_business_status,
            "Lifecycle_Latest_Status": lifecycle_latest_status,
            "Lifecycle_Check": lifecycle_check,
            "Multi_Policy_Members": multi_policy_members,
            "Lifecycle_Entity_State": states,
            "Raw_Month_Summary": raw_summary,
            "Raw_Events_Sample": events.head(100000),
        }
    )

    print("\nDone cicim:")
    print(OUTPUT_EXCEL.resolve())


if __name__ == "__main__":
    main()
