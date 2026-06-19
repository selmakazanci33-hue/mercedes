import urllib.parse
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

# =========================
# AZURE SQL CONNECTION
# =========================
SERVER = "ga......"       # Data Source
DATABASE = "ga......"     # Initial Catalog
USERNAME = "sk..."        # User ID
DRIVER = "ODBC Driver 18 for SQL Server"

OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

EXCEL_PATH = OUTPUT_DIR / "azure_834_2026_jan_may_all_issuers.xlsx"

# Read-only candidate tables
TABLES_TO_EXPORT = [
    ("dbo", "834_Inbound_header_test"),
    ("dbo", "834_Inbound_test"),
    ("dbo", "Enrollments_PY2026"),
    ("dbo", "PY2026-Enrollments_All"),
    ("dbo", "hh_demographics_enrollees_PY2026"),
    ("dbo", "concurrent_enrollments_cms"),
    ("dbo", "DuplicateEnrollment_Overlap"),
]


def get_engine():
    conn_str = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"Authentication=ActiveDirectoryInteractive;"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Connection Timeout=30;"
    )

    params = urllib.parse.quote_plus(conn_str)

    return create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}",
        fast_executemany=False
    )


def read_df(engine, sql):
    with engine.connect() as conn:
        return pd.read_sql_query(text(sql), conn)


def get_columns(engine, schema, table):
    sql = f"""
    SELECT
        COLUMN_NAME,
        DATA_TYPE,
        ORDINAL_POSITION
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = '{schema}'
      AND TABLE_NAME = '{table}'
    ORDER BY ORDINAL_POSITION
    """
    return read_df(engine, sql)


def pick_date_column(columns):
    candidates = [
        "GAA_834_File_Date",
        "file_date",
        "coverage_effective_date",
        "benefit_effective_date",
        "member_maint_effective_date",
        "EffectiveDate",
        "effective_date",
        "created_date",
        "load_date",
        "GAA_Load_Date",
    ]

    existing = set(columns["COLUMN_NAME"].tolist())

    for col in candidates:
        if col in existing:
            return col

    for col in existing:
        lower = col.lower()
        if "date" in lower or "effective" in lower:
            return col

    return None


def pick_issuer_column(columns):
    candidates = [
        "GAA_HIOS_ID",
        "issuer",
        "issuer_id",
        "hios_id",
        "HIOS_ID",
        "Issuer_ID",
    ]

    existing = set(columns["COLUMN_NAME"].tolist())

    for col in candidates:
        if col in existing:
            return col

    for col in existing:
        lower = col.lower()
        if "hios" in lower or "issuer" in lower:
            return col

    return None


def export_table(engine, schema, table):
    columns = get_columns(engine, schema, table)

    if columns.empty:
        print(f"Skipping {schema}.{table}: no columns found")
        return None, columns

    date_col = pick_date_column(columns)
    issuer_col = pick_issuer_column(columns)

    full_name = f"[{schema}].[{table}]"

    where_clauses = []

    # Jan-May 2026
    if date_col:
        where_clauses.append(
            f"TRY_CONVERT(date, [{date_col}]) >= '2026-01-01'"
        )
        where_clauses.append(
            f"TRY_CONVERT(date, [{date_col}]) < '2026-06-01'"
        )

    where_sql = ""
    if where_clauses:
        where_sql = "WHERE " + " AND ".join(where_clauses)

    sql = f"""
    SELECT *
    FROM {full_name}
    {where_sql}
    """

    print(f"\nExporting {schema}.{table}")
    print(f"Date column used: {date_col}")
    print(f"Issuer column detected: {issuer_col}")

    df = read_df(engine, sql)

    df.insert(0, "_source_table", f"{schema}.{table}")

    if date_col:
        df.insert(1, "_filter_date_column", date_col)

    if issuer_col:
        df.insert(2, "_issuer_column_detected", issuer_col)

    print(f"Rows exported: {len(df)}")

    return df, columns


def normalize_and_cleanup(df):
    clean = df.copy()

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
    }

    clean = clean.rename(columns={k: v for k, v in rename_map.items() if k in clean.columns})

    possible_status_cols = [
        "additional_maint_reason_code",
        "status",
        "enrolleeStatus",
        "maintenance_reason_code",
    ]

    status_col = next((c for c in possible_status_cols if c in clean.columns), None)

    if status_col:
        clean["normalized_status"] = clean[status_col].replace({
            "REINSTATE": "CONFIRM"
        })
    else:
        clean["normalized_status"] = None

    if "insurance_type_code" in clean.columns:
        clean["Insurance_Type"] = clean["insurance_type_code"].apply(
            lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
        )

    def enrollment_key(row):
        for col, prefix in [
            ("policy_id", "policy"),
            ("subscriber_id", "subscriber"),
            ("household_or_employee_case_id", "household"),
        ]:
            if col in clean.columns:
                val = row.get(col)
                if pd.notna(val) and str(val).strip():
                    return f"{prefix}:{val}"
        return None

    clean["enrollment_key"] = clean.apply(enrollment_key, axis=1)

    return clean


def write_excel(all_exports, all_columns):
    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl") as writer:
        # Table columns metadata
        columns_df = pd.concat(all_columns, ignore_index=True) if all_columns else pd.DataFrame()
        columns_df.to_excel(writer, sheet_name="Table_Columns", index=False)

        for sheet_name, df in all_exports.items():
            safe_name = sheet_name[:31]

            # Excel sheet limit protection
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


def main():
    engine = get_engine()

    all_exports = {}
    all_columns = []

    for schema, table in TABLES_TO_EXPORT:
        try:
            df, columns = export_table(engine, schema, table)

            if columns is not None and not columns.empty:
                columns.insert(0, "TABLE_SCHEMA", schema)
                columns.insert(1, "TABLE_NAME", table)
                all_columns.append(columns)

            if df is not None:
                sheet_base = table.replace("-", "_")[:25]
                all_exports[f"{sheet_base}_Raw"] = df

                clean_df = normalize_and_cleanup(df)
                all_exports[f"{sheet_base}_Clean"] = clean_df

        except Exception as e:
            print(f"ERROR exporting {schema}.{table}: {e}")

    write_excel(all_exports, all_columns)

    print("\nExcel created successfully:")
    print(EXCEL_PATH.resolve())


if __name__ == "__main__":
    main()
