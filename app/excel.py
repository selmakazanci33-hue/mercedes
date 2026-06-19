import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path("data/issuer_834.db")
OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

EXCEL_PATH = OUTPUT_DIR / "issuer_15105_full_record_level_analysis.xlsx"


def connect():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"DB not found: {DB_PATH.resolve()}")
    return sqlite3.connect(DB_PATH)


def export_to_excel():
    conn = connect()

    raw_sql = """
    SELECT
        issuer,
        year,
        month,
        raw_xml_path,
        record_id,

        policy_id,
        member_id,
        subscriber_id,
        household_or_employee_case_id,

        relationship,
        subscriber_flag,
        insurance_type_code,

        additional_maint_reason_code AS status,
        maintenance_type_code,
        enrollee_event_type_code,
        enrollee_event_reason_code,
        transaction_classification,
        coverage_status,

        benefit_effective_date,
        benefit_end_date,
        member_maint_effective_date,
        request_submit_timestamp,

        first_name,
        last_name,
        middle_name,
        name_prefix,
        name_suffix,
        birth_date,
        gender,
        ssn,

        address_line1,
        address_line2,
        city,
        state,
        zip_code,

        plan_id,
        qhp_id,
        csr_variant,
        aptc_amount,
        premium_amount,
        total_responsibility_amount
    FROM stg_834_records
    WHERE issuer = '15105'
      AND year = '2026'
    ORDER BY
        year,
        month,
        status,
        member_id,
        policy_id,
        member_maint_effective_date
    """

    raw_df = pd.read_sql_query(raw_sql, conn)

    duplicate_members_sql = """
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
    FROM stg_834_records
    WHERE issuer = '15105'
      AND year = '2026'
      AND additional_maint_reason_code IN ('CONFIRM', 'CANCEL', 'TERM', 'REINSTATE')
    GROUP BY issuer, year, month, additional_maint_reason_code, member_id
    HAVING COUNT(*) > 1
    ORDER BY month, status, row_count DESC
    """

    duplicate_policies_sql = """
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
    FROM stg_834_records
    WHERE issuer = '15105'
      AND year = '2026'
      AND additional_maint_reason_code IN ('CONFIRM', 'CANCEL', 'TERM', 'REINSTATE')
    GROUP BY issuer, year, month, additional_maint_reason_code, policy_id
    HAVING COUNT(*) > 1
    ORDER BY month, status, row_count DESC
    """

    same_member_multiple_policies_sql = """
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
    FROM stg_834_records
    WHERE issuer = '15105'
      AND year = '2026'
    GROUP BY issuer, year, month, member_id
    HAVING COUNT(DISTINCT policy_id) > 1
    ORDER BY month, policy_count DESC
    """

    same_policy_multiple_members_sql = """
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
    FROM stg_834_records
    WHERE issuer = '15105'
      AND year = '2026'
    GROUP BY issuer, year, month, policy_id
    HAVING COUNT(DISTINCT member_id) > 1
    ORDER BY month, member_count DESC
    """

    status_summary_sql = """
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
    FROM stg_834_records
    WHERE issuer = '15105'
      AND year = '2026'
      AND additional_maint_reason_code IN ('CONFIRM', 'CANCEL', 'TERM', 'REINSTATE')
    GROUP BY issuer, year, month, additional_maint_reason_code
    ORDER BY year, month, status
    """

    dfs = {
        "All_Raw_Data": raw_df,
        "Duplicate_Members": pd.read_sql_query(duplicate_members_sql, conn),
        "Duplicate_Policies": pd.read_sql_query(duplicate_policies_sql, conn),
        "Same_Member_Multiple_Policies": pd.read_sql_query(same_member_multiple_policies_sql, conn),
        "Same_Policy_Multiple_Members": pd.read_sql_query(same_policy_multiple_members_sql, conn),
        "Status_Summary": pd.read_sql_query(status_summary_sql, conn),
    }

    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl") as writer:
        for sheet_name, df in dfs.items():
            df.to_excel(writer, sheet_name=sheet_name[:31], index=False)

            ws = writer.book[sheet_name[:31]]
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

    print(f"Excel exported successfully: {EXCEL_PATH}")


if __name__ == "__main__":
    export_to_excel()
