import pyodbc
import pandas as pd
from pathlib import Path

# =========================
# DUMMY AZURE SQL SETTINGS
# =========================
SERVER = "your-server-name.database.windows.net"
DATABASE = "your-database-name"
USERNAME = "your-username"
PASSWORD = "your-password"
DRIVER = "ODBC Driver 18 for SQL Server"

SCHEMA_NAME = "dbo"
TABLE_NAME = "834_Inbound_header_test"   # change if needed

OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

EXCEL_PATH = OUTPUT_DIR / f"azure_{TABLE_NAME}_full_analysis.xlsx"


def connect_to_azure_sql():
    conn_str = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Connection Timeout=30;"
    )
    return pyodbc.connect(conn_str)


def read_table(conn):
    sql = f"""
    SELECT *
    FROM [{SCHEMA_NAME}].[{TABLE_NAME}]
    """
    return pd.read_sql(sql, conn)


def get_table_columns(conn):
    sql = f"""
    SELECT
        COLUMN_NAME,
        DATA_TYPE,
        IS_NULLABLE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '{SCHEMA_NAME}'
      AND TABLE_NAME = '{TABLE_NAME}'
    ORDER BY ORDINAL_POSITION
    """
    return pd.read_sql(sql, conn)


def normalize_columns(df):
    rename_map = {
        "GAA_HIOS_ID": "issuer",
        "GAA_834_File_Name": "file_name",
        "GAA_834_File_Date": "file_date",
        "GAA_Load_Date": "load_date",

        "enrollment_count": "source_enrollment_count",
        "enrollee_count": "source_enrollee_count",
        "confirm_count": "source_confirm_count",
        "term_count": "source_term_count",
        "cancel_count": "source_cancel_count",
        "record_count": "source_record_count",

        "GS02_application_sender_id": "application_sender_id",
        "GS03_application_receiver_id": "application_receiver_id",
        "GS04_date": "gs_date",
        "GS05_time": "gs_time",
        "GS06_group_control_number": "group_control_number",

        "ISA06_interchange_sender_id": "interchange_sender_id",
        "ISA08_interchange_partner_id": "interchange_partner_id",
        "ISA09_interchange_date": "interchange_date",
        "ISA10_interchange_time": "interchange_time",
        "ISA13_control_number": "interchange_control_number",
        "ISA15_usage_indicator_test_or_prod": "usage_indicator",
    }

    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})
    return df


def apply_cleanup_logic(df):
    clean_df = df.copy()

    # REINSTATE -> CONFIRM if status column exists
    possible_status_cols = [
        "additional_maint_reason_code",
        "status",
        "enrolleeStatus",
        "maintenance_reason_code",
    ]

    status_col = next((c for c in possible_status_cols if c in clean_df.columns), None)

    if status_col:
        clean_df["normalized_status"] = clean_df[status_col].replace({
            "REINSTATE": "CONFIRM"
        })
    else:
        clean_df["normalized_status"] = None

    # Health / Dental
    if "insurance_type_code" in clean_df.columns:
        clean_df["Insurance_Type"] = clean_df["insurance_type_code"].apply(
            lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
        )
    else:
        clean_df["Insurance_Type"] = None

    # Enrollment key fallback
    def build_enrollment_key(row):
        for col, prefix in [
            ("policy_id", "policy"),
            ("subscriber_id", "subscriber"),
            ("household_or_employee_case_id", "household"),
        ]:
            if col in clean_df.columns:
                val = row.get(col)
                if pd.notna(val) and str(val).strip() != "":
                    return f"{prefix}:{val}"
        return None

    clean_df["enrollment_key"] = clean_df.apply(build_enrollment_key, axis=1)

    return clean_df


def create_summary_sheets(clean_df):
    sheets = {}

    sheets["Cleaned_Data"] = clean_df

    # Header/source summary if this is header table
    summary_cols = [
        c for c in [
            "issuer",
            "file_name",
            "file_date",
            "load_date",
            "source_record_count",
            "source_enrollment_count",
            "source_enrollee_count",
            "source_confirm_count",
            "source_cancel_count",
            "source_term_count",
        ]
        if c in clean_df.columns
    ]

    if summary_cols:
        sheets["Source_File_Summary"] = clean_df[summary_cols].copy()

    # Status summary if member-level columns exist
    if "normalized_status" in clean_df.columns:
        group_cols = [c for c in ["issuer", "year", "month", "Insurance_Type", "normalized_status"] if c in clean_df.columns]

        if group_cols:
            agg_dict = {}
            if "enrollment_key" in clean_df.columns:
                agg_dict["enrollment_key"] = pd.Series.nunique
            if "member_id" in clean_df.columns:
                agg_dict["member_id"] = pd.Series.nunique
            if "policy_id" in clean_df.columns:
                agg_dict["policy_id"] = pd.Series.nunique

            if agg_dict:
                status_summary = (
                    clean_df
                    .groupby(group_cols, dropna=False)
                    .agg(agg_dict)
                    .reset_index()
                    .rename(columns={
                        "enrollment_key": "Enrollment_Count",
                        "member_id": "Enrollee_Count",
                        "policy_id": "Distinct_Policies",
                    })
                )
                sheets["Cleaned_Status_Summary"] = status_summary

    # Duplicate members
    if "member_id" in clean_df.columns:
        duplicate_members = (
            clean_df
            .groupby(["member_id"], dropna=False)
            .size()
            .reset_index(name="row_count")
        )
        duplicate_members = duplicate_members[duplicate_members["row_count"] > 1]
        sheets["Duplicate_Members"] = duplicate_members

    # Duplicate policies
    if "policy_id" in clean_df.columns:
        duplicate_policies = (
            clean_df
            .groupby(["policy_id"], dropna=False)
            .size()
            .reset_index(name="row_count")
        )
        duplicate_policies = duplicate_policies[duplicate_policies["row_count"] > 1]
        sheets["Duplicate_Policies"] = duplicate_policies

    # Same member multiple policies
    if "member_id" in clean_df.columns and "policy_id" in clean_df.columns:
        member_policy = (
            clean_df
            .groupby("member_id", dropna=False)["policy_id"]
            .nunique()
            .reset_index(name="policy_count")
        )
        member_policy = member_policy[member_policy["policy_count"] > 1]
        sheets["Same_Member_Multiple_Policies"] = member_policy

    return sheets


def export_excel(raw_df, clean_df, table_info, sheets):
    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl") as writer:
        table_info.to_excel(writer, sheet_name="Table_Info", index=False)
        raw_df.to_excel(writer, sheet_name="Raw_Azure_Data", index=False)

        for sheet_name, df in sheets.items():
            safe_name = sheet_name[:31]
            df.to_excel(writer, sheet_name=safe_name, index=False)

            ws = writer.book[safe_name]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions

            for col in ws.columns:
                max_length = 0
                col_letter = col[0].column_letter
                for cell in col:
                    value = "" if cell.value is None else str(cell.value)
                    max_length = max(max_length, len(value))
                ws.column_dimensions[col_letter].width = min(max_length + 2, 45)

        for sheet_name in ["Table_Info", "Raw_Azure_Data"]:
            ws = writer.book[sheet_name]
            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions

            for col in ws.columns:
                max_length = 0
                col_letter = col[0].column_letter
                for cell in col:
                    value = "" if cell.value is None else str(cell.value)
                    max_length = max(max_length, len(value))
                ws.column_dimensions[col_letter].width = min(max_length + 2, 45)


def main():
    conn = connect_to_azure_sql()

    print("Connected to Azure SQL.")

    table_info = get_table_columns(conn)
    raw_df = read_table(conn)

    print(f"Rows pulled from Azure: {len(raw_df)}")

    normalized_df = normalize_columns(raw_df)
    clean_df = apply_cleanup_logic(normalized_df)

    sheets = create_summary_sheets(clean_df)

    export_excel(
        raw_df=raw_df,
        clean_df=clean_df,
        table_info=table_info,
        sheets=sheets
    )

    conn.close()

    print("Excel export completed:")
    print(EXCEL_PATH.resolve())


if __name__ == "__main__":
    main()
