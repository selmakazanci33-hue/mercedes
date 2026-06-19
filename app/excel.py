import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path("data/issuer_834.db")
OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

EXCEL_PATH = OUTPUT_DIR / "issuer_15105_full_record_level_analysis.xlsx"
TABLE_NAME = "stg_834_records"

ISSUER = "15105"
YEAR = "2026"


def connect():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"DB not found: {DB_PATH.resolve()}")
    return sqlite3.connect(DB_PATH)


def get_existing_columns(conn, table_name=TABLE_NAME):
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table_name})")
    return {row[1] for row in cur.fetchall()}


def select_existing_columns(conn, wanted_columns):
    existing = get_existing_columns(conn)
    return [col for col in wanted_columns if col in existing]


def build_select_sql(conn):
    wanted_columns = [
        "issuer",
        "year",
        "month",
        "raw_xml_path",
        "record_id",

        "policy_id",
        "member_id",
        "subscriber_id",
        "household_or_employee_case_id",

        "relationship",
        "subscriber_flag",
        "insurance_type_code",

        "additional_maint_reason_code",
        "maintenance_type_code",
        "enrollee_event_type_code",
        "enrollee_event_reason_code",
        "transaction_classification",
        "coverage_status",

        "benefit_effective_date",
        "benefit_end_date",
        "member_maint_effective_date",
        "request_submit_timestamp",

        "first_name",
        "last_name",
        "middle_name",
        "name_prefix",
        "name_suffix",
        "birth_date",
        "gender",
        "ssn",

        "address_line1",
        "address_line2",
        "city",
        "state",
        "zip_code",

        "plan_id",
        "qhp_id",
        "csr_variant",
        "aptc_amount",
        "premium_amount",
        "total_responsibility_amount",
    ]

    selected_columns = select_existing_columns(conn, wanted_columns)

    if not selected_columns:
        raise ValueError("No matching columns found in stg_834_records.")

    sql = f"""
    SELECT
        {", ".join(selected_columns)}
    FROM {TABLE_NAME}
    WHERE issuer = '{ISSUER}'
      AND year = '{YEAR}'
    ORDER BY
        year,
        month,
        additional_maint_reason_code,
        member_id,
        policy_id
    """

    return sql


def read_sql(conn, sql):
    try:
        return pd.read_sql_query(sql, conn)
    except Exception as e:
        print("\nSQL failed:")
        print(sql)
        raise e


def export_to_excel():
    conn = connect()

    raw_sql = build_select_sql(conn)

    duplicate_members_sql = f"""
    SELECT
        issuer,
        year,
        month,
        additional_maint_reason_code AS status,
        member_id,
        COUNT(*) AS row_count,
        COUNT(DISTINCT policy_id) AS distinct_policy_count,
        COUNT(DISTINCT subscriber_id) AS distinct_subscriber_count,
        MIN(member_maint_effective_date) AS first_maint_date,
        MAX(member_maint_effective_date) AS latest_maint_date
    FROM {TABLE_NAME}
    WHERE issuer = '{ISSUER}'
      AND year = '{YEAR}'
      AND additional_maint_reason_code IN ('CONFIRM', 'CANCEL', 'TERM', 'REINSTATE')
    GROUP BY issuer, year, month, additional_maint_reason_code, member_id
    HAVING COUNT(*) > 1
    ORDER BY month, status, row_count DESC
    """

    duplicate_policies_sql = f"""
    SELECT
        issuer,
        year,
        month,
        additional_maint_reason_code AS status,
        policy_id,
        COUNT(*) AS row_count,
        COUNT(DISTINCT member_id) AS distinct_member_count,
        COUNT(DISTINCT subscriber_id) AS distinct_subscriber_count,
        MIN(member_maint_effective_date) AS first_maint_date,
        MAX(member_maint_effective_date) AS latest_maint_date
    FROM {TABLE_NAME}
    WHERE issuer = '{ISSUER}'
      AND year = '{YEAR}'
      AND additional_maint_reason_code IN ('CONFIRM', 'CANCEL', 'TERM', 'REINSTATE')
    GROUP BY issuer, year, month, additional_maint_reason_code, policy_id
    HAVING COUNT(*) > 1
    ORDER BY month, status, row_count DESC
    """

    same_member_multiple_policies_sql = f"""
    SELECT
        issuer,
        year,
        month,
        member_id,
        COUNT(DISTINCT policy_id) AS policy_count,
        GROUP_CONCAT(DISTINCT policy_id) AS policy_ids,
        GROUP_CONCAT(DISTINCT additional_maint_reason_code) AS statuses,
        MIN(member_maint_effective_date) AS first_maint_date,
        MAX(member_maint_effective_date) AS latest_maint_date
    FROM {TABLE_NAME}
    WHERE issuer = '{ISSUER}'
      AND year = '{YEAR}'
    GROUP BY issuer, year, month, member_id
    HAVING COUNT(DISTINCT policy_id) > 1
    ORDER BY month, policy_count DESC
    """

    same_policy_multiple_members_sql = f"""
    SELECT
        issuer,
        year,
        month,
        policy_id,
        COUNT(DISTINCT member_id) AS member_count,
        GROUP_CONCAT(DISTINCT member_id) AS member_ids,
        GROUP_CONCAT(DISTINCT additional_maint_reason_code) AS statuses,
        MIN(member_maint_effective_date) AS first_maint_date,
        MAX(member_maint_effective_date) AS latest_maint_date
    FROM {TABLE_NAME}
    WHERE issuer = '{ISSUER}'
      AND year = '{YEAR}'
    GROUP BY issuer, year, month, policy_id
    HAVING COUNT(DISTINCT member_id) > 1
    ORDER BY month, member_count DESC
    """

    status_summary_sql = f"""
    SELECT
        issuer,
        year,
        month,
        additional_maint_reason_code AS status,
        COUNT(*) AS raw_rows,
        COUNT(DISTINCT policy_id) AS distinct_policies,
        COUNT(DISTINCT member_id) AS distinct_members,
        COUNT(DISTINCT subscriber_id) AS distinct_subscribers,
        COUNT(DISTINCT household_or_employee_case_id) AS distinct_households
    FROM {TABLE_NAME}
    WHERE issuer = '{ISSUER}'
      AND year = '{YEAR}'
      AND additional_maint_reason_code IN ('CONFIRM', 'CANCEL', 'TERM', 'REINSTATE')
    GROUP BY issuer, year, month, additional_maint_reason_code
    ORDER BY year, month, status
    """

    dfs = {
        "All_Raw_Data": read_sql(conn, raw_sql),
        "Duplicate_Members": read_sql(conn, duplicate_members_sql),
        "Duplicate_Policies": read_sql(conn, duplicate_policies_sql),
        "Same_Member_Multiple_Policies": read_sql(conn, same_member_multiple_policies_sql),
        "Same_Policy_Multiple_Members": read_sql(conn, same_policy_multiple_members_sql),
        "Status_Summary": read_sql(conn, status_summary_sql),
    }

    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl") as writer:
        for sheet_name, df in dfs.items():
            safe_sheet_name = sheet_name[:31]
            df.to_excel(writer, sheet_name=safe_sheet_name, index=False)

            ws = writer.book[safe_sheet_name]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions

            for col in ws.columns:
                max_length = 0
                col_letter = col[0].column_letter

                for cell in col:
                    value = "" if cell.value is None else str(cell.value)
                    max_length = max(max_length, len(value))

                ws.column_dimensions[col_letter].width = min(max_length + 2, 45)

    conn.close()

    print(f"\nExcel export completed successfully:")
    print(EXCEL_PATH.resolve())


if __name__ == "__main__":
    export_to_excel()
