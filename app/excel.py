import sqlite3
from pathlib import Path
import pandas as pd


SQLITE_DB_PATH = Path("data/issuer_834.db")

OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_EXCEL = OUTPUT_DIR / "monthly_event_with_lookback_engine_jan_may_2026.xlsx"

HISTORY_MONTHS = [
    ("2025", "10"), ("2025", "11"), ("2025", "12"),
    ("2026", "01"), ("2026", "02"), ("2026", "03"), ("2026", "04"), ("2026", "05"),
]

REPORT_MONTHS = [
    ("2026", "01"),
    ("2026", "02"),
    ("2026", "03"),
    ("2026", "04"),
    ("2026", "05"),
]


def read_events():
    where_sql = " OR ".join([f"(year='{y}' AND month='{m}')" for y, m in HISTORY_MONTHS])

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


def clean(df):
    df = df.copy()

    df["issuer"] = df["issuer"].astype(str)
    df["year"] = df["year"].astype(str)
    df["month"] = df["month"].astype(str).str.zfill(2)

    df["status"] = df["additional_maint_reason_code"].replace({"REINSTATE": "CONFIRM"})

    df["insurance_type"] = df["insurance_type_code"].apply(
        lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
    )

    for col in ["policy_id", "member_id", "subscriber_id", "household_id"]:
        df[col] = df[col].astype(str).replace(["None", "nan", "NaN", ""], pd.NA)

    df["enrollment_key"] = df["policy_id"].fillna(df["subscriber_id"]).fillna(df["household_id"])

    df["entity_key"] = (
        df["issuer"].astype(str) + "|" +
        df["insurance_type"].astype(str) + "|" +
        df["enrollment_key"].astype(str) + "|" +
        df["member_id"].astype(str)
    )

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
        "CANCEL": 3,
        "TERM": 2
    }).fillna(1)

    return df


def month_bounds(year, month):
    start = pd.Timestamp(f"{year}-{month}-01")
    end = start + pd.offsets.MonthEnd(0)
    return start, end


def build_monthly_lookback(events):
    outputs = []

    for report_year, report_month in REPORT_MONTHS:
        report_start, report_end = month_bounds(report_year, report_month)

        current_month = events[
            (events["year"] == report_year) &
            (events["month"] == report_month)
        ].copy()

        history = events[
            events["event_date"] <= report_end
        ].copy()

        if current_month.empty:
            continue

        # latest policy/member state from history
        history = history.sort_values([
            "entity_key",
            "event_date",
            "year",
            "month",
            "status_rank",
            "raw_xml_path"
        ])

        latest_entity_state = history.drop_duplicates("entity_key", keep="last").copy()

        # current valid policy per person from history
        latest_entity_state["coverage_active_in_report_month"] = (
            (latest_entity_state["benefit_effective_date"].isna() |
             (latest_entity_state["benefit_effective_date"] <= report_end))
            &
            (latest_entity_state["benefit_end_date"].isna() |
             (latest_entity_state["benefit_end_date"] >= report_start))
        )

        latest_entity_state["priority_date"] = (
            latest_entity_state["benefit_effective_date"]
            .fillna(latest_entity_state["event_date"])
            .fillna(latest_entity_state["file_month_date"])
        )

        current_policy_per_person = latest_entity_state.sort_values([
            "person_key",
            "coverage_active_in_report_month",
            "priority_date",
            "event_date",
            "status_rank"
        ]).drop_duplicates("person_key", keep="last")[
            ["person_key", "enrollment_key"]
        ].rename(columns={"enrollment_key": "current_enrollment_key"})

        enriched = current_month.merge(
            current_policy_per_person,
            on="person_key",
            how="left"
        )

        enriched["is_current_enrollment_for_person"] = (
            enriched["enrollment_key"] == enriched["current_enrollment_key"]
        )

        # monthly base dedup: same entity inside same month should count once
        enriched = enriched.sort_values([
            "entity_key",
            "event_date",
            "status_rank",
            "raw_xml_path"
        ])

        deduped = enriched.drop_duplicates("entity_key", keep="last").copy()

        deduped["report_year"] = report_year
        deduped["report_month"] = report_month

        deduped["months_since_event"] = (
            (report_end.year - deduped["event_date"].dt.year) * 12
            + (report_end.month - deduped["event_date"].dt.month)
        )

        deduped["business_status"] = deduped["status"]

        # REINSTATE already mapped to CONFIRM
        # 3-month cancel rule
        deduped.loc[
            (deduped["status"] == "CANCEL") &
            (deduped["months_since_event"] >= 3),
            "business_status"
        ] = "TERM"

        # Exclude superseded current-month records
        deduped["include_in_business_count"] = deduped["is_current_enrollment_for_person"]

        outputs.append(deduped)

    if not outputs:
        return pd.DataFrame()

    return pd.concat(outputs, ignore_index=True)


def summarize(df, status_col, prefix, only_included=False):
    work = df.copy()

    if only_included:
        work = work[work["include_in_business_count"] == True].copy()

    return (
        work.groupby(["issuer", "report_year", "report_month", "insurance_type", status_col], dropna=False)
        .agg(
            **{
                f"{prefix}_rows": ("member_id", "size"),
                f"{prefix}_enrollment_count": ("enrollment_key", "nunique"),
                f"{prefix}_enrollee_count": ("member_id", "nunique"),
                f"{prefix}_subscriber_count": ("subscriber_id", "nunique"),
                f"{prefix}_file_count": ("raw_xml_path", "nunique"),
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


def issuer_month_summary(df, prefix, only_included=False):
    work = df.copy()

    if only_included:
        work = work[work["include_in_business_count"] == True].copy()

    return (
        work.groupby(["issuer", "report_year", "report_month"], dropna=False)
        .agg(
            **{
                f"{prefix}_rows": ("member_id", "size"),
                f"{prefix}_enrollment_count": ("enrollment_key", "nunique"),
                f"{prefix}_enrollee_count": ("member_id", "nunique"),
                f"{prefix}_subscriber_count": ("subscriber_id", "nunique"),
                f"{prefix}_file_count": ("raw_xml_path", "nunique"),
                f"{prefix}_confirm_count": ("business_status", lambda x: (x == "CONFIRM").sum()),
                f"{prefix}_cancel_count": ("business_status", lambda x: (x == "CANCEL").sum()),
                f"{prefix}_term_count": ("business_status", lambda x: (x == "TERM").sum()),
            }
        )
        .reset_index()
        .rename(columns={
            "report_year": "year",
            "report_month": "month"
        })
        .sort_values(["issuer", "year", "month"])
    )


def exclusion_summary(df):
    return (
        df.groupby(["issuer", "report_year", "report_month", "include_in_business_count"], dropna=False)
        .agg(
            rows=("member_id", "size"),
            enrollments=("enrollment_key", "nunique"),
            enrollees=("member_id", "nunique"),
            subscribers=("subscriber_id", "nunique"),
        )
        .reset_index()
        .rename(columns={
            "report_year": "year",
            "report_month": "month"
        })
        .sort_values(["issuer", "year", "month", "include_in_business_count"])
    )


def raw_month_summary(events):
    report_set = set(REPORT_MONTHS)

    work = events[
        events[["year", "month"]].apply(lambda r: (r["year"], r["month"]) in report_set, axis=1)
    ].copy()

    return (
        work.groupby(["issuer", "year", "month"], dropna=False)
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


def compare_raw_business(raw, business):
    comp = raw.merge(
        business,
        on=["issuer", "year", "month"],
        how="outer"
    ).fillna(0)

    for col in comp.columns:
        if col.endswith("_count") or col.endswith("_rows"):
            comp[col] = comp[col].astype(int)

    comp["row_reduction"] = comp["raw_rows"] - comp["business_rows"]
    comp["enrollment_reduction"] = comp["raw_enrollment_count"] - comp["business_enrollment_count"]
    comp["enrollee_reduction"] = comp["raw_enrollee_count"] - comp["business_enrollee_count"]
    comp["subscriber_reduction"] = comp["raw_subscriber_count"] - comp["business_subscriber_count"]

    return comp.sort_values(["issuer", "year", "month"])


def write_excel(path, sheets):
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for name, df in sheets.items():
            sheet = name[:31]

            if df is None or df.empty:
                pd.DataFrame({"message": ["No data"]}).to_excel(writer, sheet_name=sheet, index=False)
            else:
                df.head(1_048_000).to_excel(writer, sheet_name=sheet, index=False)

        for sheet in writer.book.sheetnames:
            ws = writer.book[sheet]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions

            for col in ws.columns:
                width = min(max(len(str(cell.value)) if cell.value is not None else 0 for cell in col) + 2, 45)
                ws.column_dimensions[col[0].column_letter].width = width


def main():
    print("Reading events...")
    raw = read_events()
    print(f"Raw events: {len(raw)}")

    print("Cleaning...")
    events = clean(raw)

    print("Building monthly lookback business records...")
    monthly = build_monthly_lookback(events)
    print(f"Monthly lookback rows: {len(monthly)}")

    print("Summarizing...")
    raw_summary = raw_month_summary(events)
    business_summary = summarize(monthly, "business_status", "business", only_included=True)
    monthly_all_summary = summarize(monthly, "business_status", "monthly_all", only_included=False)

    business_issuer_month = issuer_month_summary(monthly, "business", only_included=True)
    all_issuer_month = issuer_month_summary(monthly, "monthly_all", only_included=False)

    excluded = exclusion_summary(monthly)

    comparison = compare_raw_business(raw_summary, business_issuer_month)

    excluded_records = monthly[monthly["include_in_business_count"] == False].copy()

    print("Writing Excel...")
    write_excel(
        OUTPUT_EXCEL,
        {
            "Raw_vs_Business_Compare": comparison,
            "Business_Issuer_Month": business_issuer_month,
            "All_Current_Month_Records": all_issuer_month,
            "Business_Status_Summary": business_summary,
            "All_Status_Summary": monthly_all_summary,
            "Exclusion_Summary": excluded,
            "Excluded_Records_Sample": excluded_records.head(5000),
            "Monthly_Lookback_Sample": monthly.head(20000),
            "Raw_Month_Summary": raw_summary,
        }
    )

    print("\nDone cicim:")
    print(OUTPUT_EXCEL.resolve())


if __name__ == "__main__":
    main()
