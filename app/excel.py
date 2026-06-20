import sqlite3
from pathlib import Path
import pandas as pd


DB_PATH = Path("data/issuer_834.db")
OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_EXCEL = OUTPUT_DIR / "investigate_15105_jan_2026_lifecycle.xlsx"

ISSUER = "15105"
FOCUS_YEAR = "2026"
FOCUS_MONTH = "01"

HISTORY_MONTHS = [
    ("2025", "10"),
    ("2025", "11"),
    ("2025", "12"),
    ("2026", "01"),
]


def get_columns(conn, table="stg_834_records"):
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    return [row[1] for row in cur.fetchall()]


def col_expr(columns, col_name, alias=None):
    alias = alias or col_name
    if col_name in columns:
        return f"{col_name} AS {alias}"
    return f"NULL AS {alias}"


def load_data():
    conn = sqlite3.connect(DB_PATH)
    columns = get_columns(conn)

    select_cols = [
        col_expr(columns, "issuer"),
        col_expr(columns, "year"),
        col_expr(columns, "month"),
        col_expr(columns, "policy_id"),
        col_expr(columns, "member_id"),
        col_expr(columns, "subscriber_id"),
        col_expr(columns, "household_or_employee_case_id", "household_id"),
        col_expr(columns, "insurance_type_code"),
        col_expr(columns, "additional_maint_reason_code", "status"),
        col_expr(columns, "maintenance_type_code"),
        col_expr(columns, "enrollee_event_type_code"),
        col_expr(columns, "enrollee_event_reason_code"),
        col_expr(columns, "subscriber_flag"),
        col_expr(columns, "relationship"),
        col_expr(columns, "benefit_effective_date"),
        col_expr(columns, "benefit_end_date"),
        col_expr(columns, "member_maint_effective_date"),
        col_expr(columns, "raw_xml_path"),
        col_expr(columns, "previousExchgAssignedPolicyID", "previous_policy_id"),
        col_expr(columns, "previous_exchg_assigned_policy_id", "previous_policy_id_alt"),
        col_expr(columns, "renewalStatus", "renewal_status"),
        col_expr(columns, "renewal_status", "renewal_status_alt"),
    ]

    history_where = " OR ".join(
        [f"(year='{y}' AND month='{m}')" for y, m in HISTORY_MONTHS]
    )

    sql = f"""
    WITH focus_members AS (
        SELECT DISTINCT member_id
        FROM stg_834_records
        WHERE issuer = '{ISSUER}'
          AND year = '{FOCUS_YEAR}'
          AND month = '{FOCUS_MONTH}'
          AND additional_maint_reason_code IN ('CONFIRM','REINSTATE','CANCEL','TERM')
    )
    SELECT
        {", ".join(select_cols)}
    FROM stg_834_records
    WHERE issuer = '{ISSUER}'
      AND ({history_where})
      AND member_id IN (SELECT member_id FROM focus_members)
      AND additional_maint_reason_code IN ('CONFIRM','REINSTATE','CANCEL','TERM')
    """

    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def clean(df):
    df = df.copy()

    df["status_normalized"] = df["status"].replace({"REINSTATE": "CONFIRM"})
    df["insurance_type"] = df["insurance_type_code"].apply(
        lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
    )

    for c in ["policy_id", "member_id", "subscriber_id", "household_id"]:
        df[c] = df[c].astype(str).replace(["None", "nan", "NaN", ""], pd.NA)

    df["enrollment_key"] = df["policy_id"].fillna(df["subscriber_id"]).fillna(df["household_id"])

    df["person_key"] = (
        df["issuer"].astype(str) + "|" +
        df["insurance_type"].astype(str) + "|" +
        df["member_id"].astype(str)
    )

    df["entity_key"] = (
        df["person_key"] + "|" +
        df["enrollment_key"].astype(str)
    )

    df["benefit_effective_date"] = pd.to_datetime(df["benefit_effective_date"], errors="coerce")
    df["benefit_end_date"] = pd.to_datetime(df["benefit_end_date"], errors="coerce")
    df["member_maint_effective_date"] = pd.to_datetime(df["member_maint_effective_date"], errors="coerce")

    df["event_month"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2)

    df["event_date"] = (
        df["member_maint_effective_date"]
        .fillna(df["benefit_effective_date"])
        .fillna(pd.to_datetime(df["event_month"] + "-01", errors="coerce"))
    )

    df["is_focus_month_record"] = (
        (df["year"] == FOCUS_YEAR) &
        (df["month"] == FOCUS_MONTH)
    )

    return df.sort_values(
        ["member_id", "policy_id", "event_date", "year", "month", "raw_xml_path"]
    )


def create_member_policy_summary(df):
    return (
        df.groupby(["member_id", "insurance_type"], dropna=False)
        .agg(
            policy_count=("enrollment_key", "nunique"),
            subscriber_count=("subscriber_id", "nunique"),
            event_rows=("member_id", "size"),
            months_seen=("event_month", lambda x: ", ".join(sorted(set(x.dropna())))),
            statuses_seen=("status_normalized", lambda x: ", ".join(sorted(set(x.dropna())))),
            first_event_date=("event_date", "min"),
            last_event_date=("event_date", "max"),
            jan_records=("is_focus_month_record", "sum"),
        )
        .reset_index()
        .sort_values(["policy_count", "event_rows"], ascending=False)
    )


def create_policy_timeline(df):
    return (
        df.groupby(
            ["member_id", "insurance_type", "enrollment_key"],
            dropna=False
        )
        .agg(
            event_rows=("member_id", "size"),
            months_seen=("event_month", lambda x: ", ".join(sorted(set(x.dropna())))),
            statuses_seen=("status_normalized", lambda x: ", ".join(sorted(set(x.dropna())))),
            first_event_date=("event_date", "min"),
            last_event_date=("event_date", "max"),
            benefit_start=("benefit_effective_date", "min"),
            benefit_end=("benefit_end_date", "max"),
            subscriber_ids=("subscriber_id", lambda x: ", ".join(sorted(set(x.dropna().astype(str))))),
            jan_records=("is_focus_month_record", "sum"),
        )
        .reset_index()
        .sort_values(["member_id", "first_event_date", "enrollment_key"])
    )


def create_possible_superseded(df):
    multi = create_member_policy_summary(df)
    multi_members = set(multi[multi["policy_count"] > 1]["member_id"].astype(str))

    return df[df["member_id"].astype(str).isin(multi_members)].copy()


def write_excel(sheets):
    with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
        for name, data in sheets.items():
            data.to_excel(writer, sheet_name=name[:31], index=False)

        for sheet_name in writer.book.sheetnames:
            ws = writer.book[sheet_name]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions

            for col in ws.columns:
                width = min(max(len(str(cell.value)) if cell.value else 0 for cell in col) + 2, 45)
                ws.column_dimensions[col[0].column_letter].width = width


def main():
    print("Loading 15105 Jan lifecycle investigation data...")
    raw = load_data()
    print(f"Rows loaded: {len(raw)}")

    clean_df = clean(raw)

    member_summary = create_member_policy_summary(clean_df)
    policy_timeline = create_policy_timeline(clean_df)
    superseded_candidates = create_possible_superseded(clean_df)

    write_excel({
        "Member_Policy_Summary": member_summary,
        "Policy_Timeline": policy_timeline,
        "Superseded_Candidates": superseded_candidates,
        "Investigation_Raw": clean_df,
    })

    print("\nDone cicim:")
    print(OUTPUT_EXCEL.resolve())


if __name__ == "__main__":
    main()
