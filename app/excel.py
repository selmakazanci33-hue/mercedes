import sqlite3
from pathlib import Path

import pandas as pd


# =====================================================
# CONFIG
# =====================================================

SQLITE_DB_PATH = Path("data/issuer_834.db")

OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_EXCEL = OUTPUT_DIR / "xml_timeline_state_engine_2026_jan_may.xlsx"

HISTORY_MONTHS = [
    ("2025", "10"),
    ("2025", "11"),
    ("2025", "12"),
    ("2026", "01"),
    ("2026", "02"),
    ("2026", "03"),
    ("2026", "04"),
    ("2026", "05"),
]

REPORT_MONTHS = [
    ("2026", "01"),
    ("2026", "02"),
    ("2026", "03"),
    ("2026", "04"),
    ("2026", "05"),
]


# =====================================================
# READ XML SQLITE
# =====================================================

def get_xml_events():
    if not SQLITE_DB_PATH.exists():
        raise FileNotFoundError(f"SQLite DB not found: {SQLITE_DB_PATH.resolve()}")

    where_parts = []
    for year, month in HISTORY_MONTHS:
        where_parts.append(f"(year = '{year}' AND month = '{month}')")

    where_sql = " OR ".join(where_parts)

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


# =====================================================
# CLEANUP / NORMALIZATION
# =====================================================

def clean_events(df):
    clean = df.copy()

    clean["issuer"] = clean["issuer"].astype(str)
    clean["year"] = clean["year"].astype(str)
    clean["month"] = clean["month"].astype(str).str.zfill(2)

    clean["status"] = clean["additional_maint_reason_code"].replace({
        "REINSTATE": "CONFIRM"
    })

    clean["insurance_type"] = clean["insurance_type_code"].apply(
        lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
    )

    for col in ["policy_id", "member_id", "subscriber_id", "household_id"]:
        clean[col] = clean[col].astype(str)
        clean[col] = clean[col].replace(["None", "nan", "NaN", ""], pd.NA)

    def enrollment_key(row):
        for col in ["policy_id", "subscriber_id", "household_id"]:
            val = row.get(col)
            if pd.notna(val) and str(val).strip():
                return str(val).strip()
        return None

    clean["enrollment_key"] = clean.apply(enrollment_key, axis=1)

    clean["entity_key"] = (
        clean["issuer"].astype(str) + "|" +
        clean["insurance_type"].astype(str) + "|" +
        clean["enrollment_key"].astype(str) + "|" +
        clean["member_id"].astype(str)
    )

    clean["benefit_effective_date"] = pd.to_datetime(clean["benefit_effective_date"], errors="coerce")
    clean["benefit_end_date"] = pd.to_datetime(clean["benefit_end_date"], errors="coerce")
    clean["member_maint_effective_date"] = pd.to_datetime(clean["member_maint_effective_date"], errors="coerce")

    clean["file_month_date"] = pd.to_datetime(
        clean["year"] + "-" + clean["month"] + "-01",
        errors="coerce"
    )

    clean["event_date"] = (
        clean["member_maint_effective_date"]
        .fillna(clean["benefit_effective_date"])
        .fillna(clean["file_month_date"])
    )

    return clean


# =====================================================
# RAW EVENT SUMMARY
# =====================================================

def raw_event_summary(df):
    return (
        df.groupby(["issuer", "year", "month", "insurance_type", "status"], dropna=False)
        .agg(
            raw_event_rows=("member_id", "size"),
            raw_enrollment_count=("enrollment_key", "nunique"),
            raw_enrollee_count=("member_id", "nunique"),
            raw_subscriber_count=("subscriber_id", "nunique"),
            raw_file_count=("raw_xml_path", "nunique"),
        )
        .reset_index()
        .sort_values(["issuer", "year", "month", "insurance_type", "status"])
    )


# =====================================================
# TIMELINE ENGINE
# =====================================================

def month_start_end(year, month):
    start = pd.Timestamp(f"{year}-{month}-01")
    end = start + pd.offsets.MonthEnd(0)
    return start, end


def build_timeline_states(events):
    all_states = []

    for report_year, report_month in REPORT_MONTHS:
        report_start, report_end = month_start_end(report_year, report_month)

        eligible = events[events["event_date"] <= report_end].copy()

        if eligible.empty:
            continue

        eligible = eligible.sort_values([
            "entity_key",
            "event_date",
            "year",
            "month",
            "raw_xml_path"
        ])

        latest = eligible.drop_duplicates("entity_key", keep="last").copy()

        latest["report_year"] = report_year
        latest["report_month"] = report_month
        latest["report_start"] = report_start
        latest["report_end"] = report_end

        latest["months_since_event"] = (
            (report_end.year - latest["event_date"].dt.year) * 12
            + (report_end.month - latest["event_date"].dt.month)
        )

        latest["business_status_3mo"] = latest["status"]

        latest.loc[
            (latest["status"] == "CANCEL") &
            (latest["months_since_event"] >= 3),
            "business_status_3mo"
        ] = "TERM"

        latest["coverage_active_in_month"] = (
            (latest["benefit_effective_date"].isna() | (latest["benefit_effective_date"] <= report_end))
            &
            (latest["benefit_end_date"].isna() | (latest["benefit_end_date"] >= report_start))
        )

        all_states.append(latest)

    if not all_states:
        return pd.DataFrame()

    return pd.concat(all_states, ignore_index=True)


# =====================================================
# TIMELINE SUMMARIES
# =====================================================

def summarize_timeline_latest(states):
    return (
        states.groupby(
            ["issuer", "report_year", "report_month", "insurance_type", "status"],
            dropna=False
        )
        .agg(
            timeline_entity_rows=("entity_key", "size"),
            timeline_enrollment_count=("enrollment_key", "nunique"),
            timeline_enrollee_count=("member_id", "nunique"),
            timeline_subscriber_count=("subscriber_id", "nunique"),
            latest_event_files=("raw_xml_path", "nunique"),
        )
        .reset_index()
        .rename(columns={
            "report_year": "year",
            "report_month": "month"
        })
        .sort_values(["issuer", "year", "month", "insurance_type", "status"])
    )


def summarize_timeline_business_3mo(states):
    return (
        states.groupby(
            ["issuer", "report_year", "report_month", "insurance_type", "business_status_3mo"],
            dropna=False
        )
        .agg(
            business_entity_rows=("entity_key", "size"),
            business_enrollment_count=("enrollment_key", "nunique"),
            business_enrollee_count=("member_id", "nunique"),
            business_subscriber_count=("subscriber_id", "nunique"),
        )
        .reset_index()
        .rename(columns={
            "report_year": "year",
            "report_month": "month",
            "business_status_3mo": "status"
        })
        .sort_values(["issuer", "year", "month", "insurance_type", "status"])
    )


def summarize_coverage_active(states):
    active = states[states["coverage_active_in_month"] == True].copy()

    return (
        active.groupby(
            ["issuer", "report_year", "report_month", "insurance_type", "status"],
            dropna=False
        )
        .agg(
            active_entity_rows=("entity_key", "size"),
            active_enrollment_count=("enrollment_key", "nunique"),
            active_enrollee_count=("member_id", "nunique"),
            active_subscriber_count=("subscriber_id", "nunique"),
        )
        .reset_index()
        .rename(columns={
            "report_year": "year",
            "report_month": "month"
        })
        .sort_values(["issuer", "year", "month", "insurance_type", "status"])
    )


def issuer_month_summary(states, status_col, prefix):
    return (
        states.groupby(["issuer", "report_year", "report_month"], dropna=False)
        .agg(
            **{
                f"{prefix}_entity_rows": ("entity_key", "size"),
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


# =====================================================
# DATA QUALITY CHECKS
# =====================================================

def month_load_check(events):
    return (
        events.groupby(["issuer", "year", "month"], dropna=False)
        .agg(
            event_rows=("member_id", "size"),
            enrollment_count=("enrollment_key", "nunique"),
            enrollee_count=("member_id", "nunique"),
            file_count=("raw_xml_path", "nunique"),
            min_event_date=("event_date", "min"),
            max_event_date=("event_date", "max"),
        )
        .reset_index()
        .sort_values(["issuer", "year", "month"])
    )


def duplicate_event_check(events):
    return (
        events.groupby(
            ["issuer", "year", "month", "insurance_type", "enrollment_key", "member_id", "status"],
            dropna=False
        )
        .agg(
            duplicate_rows=("raw_xml_path", "size"),
            file_count=("raw_xml_path", "nunique"),
            min_event_date=("event_date", "min"),
            max_event_date=("event_date", "max"),
        )
        .reset_index()
        .query("duplicate_rows > 1")
        .sort_values(["duplicate_rows"], ascending=False)
        .head(1000)
    )


# =====================================================
# EXCEL WRITER
# =====================================================

def write_excel(path, sheets):
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for sheet_name, df in sheets.items():
            safe_name = sheet_name[:31]

            if df is None or df.empty:
                pd.DataFrame({"message": ["No data"]}).to_excel(writer, sheet_name=safe_name, index=False)
            else:
                if len(df) > 1_048_000:
                    df.head(1_048_000).to_excel(writer, sheet_name=safe_name, index=False)
                else:
                    df.to_excel(writer, sheet_name=safe_name, index=False)

        for sheet_name in writer.book.sheetnames:
            ws = writer.book[sheet_name]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions

            for col in ws.columns:
                max_len = 0
                col_letter = col[0].column_letter

                for cell in col:
                    value = "" if cell.value is None else str(cell.value)
                    max_len = max(max_len, len(value))

                ws.column_dimensions[col_letter].width = min(max_len + 2, 45)


# =====================================================
# MAIN
# =====================================================

def main():
    print("Reading XML events from SQLite...")
    raw = get_xml_events()
    print(f"Raw history events: {len(raw)}")

    print("Cleaning events...")
    events = clean_events(raw)
    print(f"Clean history events: {len(events)}")

    print("Creating raw event summary...")
    raw_summary = raw_event_summary(events)

    print("Building timeline states...")
    states = build_timeline_states(events)
    print(f"Timeline state rows: {len(states)}")

    print("Creating timeline summaries...")
    latest_summary = summarize_timeline_latest(states)
    business_3mo_summary = summarize_timeline_business_3mo(states)
    active_summary = summarize_coverage_active(states)

    latest_issuer_month = issuer_month_summary(states, "status", "latest")
    business_issuer_month = issuer_month_summary(states, "business_status_3mo", "business")

    active_states = states[states["coverage_active_in_month"] == True].copy()
    active_issuer_month = issuer_month_summary(active_states, "status", "active")

    print("Creating checks...")
    load_check = month_load_check(events)
    duplicate_check = duplicate_event_check(events)

    print("Writing Excel...")
    write_excel(
        OUTPUT_EXCEL,
        {
            "Load_Check": load_check,
            "Raw_Event_Summary": raw_summary,
            "Timeline_Latest_Summary": latest_summary,
            "Timeline_Business_3mo": business_3mo_summary,
            "Coverage_Active_Summary": active_summary,
            "Issuer_Month_Latest": latest_issuer_month,
            "Issuer_Month_Business_3mo": business_issuer_month,
            "Issuer_Month_Active": active_issuer_month,
            "Timeline_Entity_State": states,
            "Duplicate_Event_Check": duplicate_check,
            "Raw_Events_Sample": events.head(100000),
        }
    )

    print("\nDone cicim:")
    print(OUTPUT_EXCEL.resolve())


if __name__ == "__main__":
    main()
