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

EXCEL_PATH = OUTPUT_DIR / "azure_production_table_discovery.xlsx"


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
    return create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


def read_sql(engine, sql):
    with engine.connect() as conn:
        return pd.read_sql_query(text(sql), conn)


def get_connection_info(engine):
    sql = """
    SELECT
        @@SERVERNAME AS server_name,
        DB_NAME() AS database_name,
        SUSER_SNAME() AS login_name,
        CURRENT_USER AS database_user,
        @@VERSION AS sql_version;
    """
    return read_sql(engine, sql)


def get_all_tables(engine):
    sql = """
    SELECT
        TABLE_SCHEMA,
        TABLE_NAME,
        TABLE_TYPE
    FROM INFORMATION_SCHEMA.TABLES
    ORDER BY TABLE_SCHEMA, TABLE_NAME;
    """
    return read_sql(engine, sql)


def get_all_columns(engine):
    sql = """
    SELECT
        TABLE_SCHEMA,
        TABLE_NAME,
        COLUMN_NAME,
        DATA_TYPE,
        IS_NULLABLE,
        ORDINAL_POSITION
    FROM INFORMATION_SCHEMA.COLUMNS
    ORDER BY TABLE_SCHEMA, TABLE_NAME, ORDINAL_POSITION;
    """
    return read_sql(engine, sql)


def get_candidate_tables(engine):
    sql = """
    SELECT
        c.TABLE_SCHEMA,
        c.TABLE_NAME,
        COUNT(*) AS matching_columns,
        STRING_AGG(c.COLUMN_NAME, ', ') AS matched_columns
    FROM INFORMATION_SCHEMA.COLUMNS c
    WHERE
           LOWER(c.COLUMN_NAME) LIKE '%issuer%'
        OR LOWER(c.COLUMN_NAME) LIKE '%hios%'
        OR LOWER(c.COLUMN_NAME) LIKE '%policy%'
        OR LOWER(c.COLUMN_NAME) LIKE '%member%'
        OR LOWER(c.COLUMN_NAME) LIKE '%subscriber%'
        OR LOWER(c.COLUMN_NAME) LIKE '%enrollee%'
        OR LOWER(c.COLUMN_NAME) LIKE '%enrollment%'
        OR LOWER(c.COLUMN_NAME) LIKE '%status%'
        OR LOWER(c.COLUMN_NAME) LIKE '%maint%'
        OR LOWER(c.COLUMN_NAME) LIKE '%effective%'
        OR LOWER(c.COLUMN_NAME) LIKE '%benefit%'
        OR LOWER(c.COLUMN_NAME) LIKE '%coverage%'
        OR LOWER(c.COLUMN_NAME) LIKE '%application%'
    GROUP BY
        c.TABLE_SCHEMA,
        c.TABLE_NAME
    HAVING COUNT(*) >= 5
    ORDER BY matching_columns DESC;
    """
    return read_sql(engine, sql)


def get_table_row_counts(engine, candidate_tables):
    results = []

    for _, row in candidate_tables.iterrows():
        schema = row["TABLE_SCHEMA"]
        table = row["TABLE_NAME"]

        try:
            sql = f"SELECT COUNT(*) AS row_count FROM [{schema}].[{table}]"
            df = read_sql(engine, sql)
            row_count = int(df.iloc[0]["row_count"])

            print(f"{schema}.{table}: {row_count}")

            results.append({
                "TABLE_SCHEMA": schema,
                "TABLE_NAME": table,
                "row_count": row_count,
                "status": "OK",
                "error": None
            })

        except Exception as e:
            print(f"ERROR {schema}.{table}: {e}")

            results.append({
                "TABLE_SCHEMA": schema,
                "TABLE_NAME": table,
                "row_count": None,
                "status": "ERROR",
                "error": str(e)
            })

    return pd.DataFrame(results)


def get_sample_data(engine, candidate_tables, max_tables=12):
    samples = {}

    for _, row in candidate_tables.head(max_tables).iterrows():
        schema = row["TABLE_SCHEMA"]
        table = row["TABLE_NAME"]
        sheet_name = f"{table[:25]}_Sample"

        try:
            sql = f"""
            SELECT TOP 50 *
            FROM [{schema}].[{table}]
            """
            df = read_sql(engine, sql)
            samples[sheet_name] = df

            print(f"Sample pulled: {schema}.{table}")

        except Exception as e:
            samples[sheet_name] = pd.DataFrame({
                "error": [str(e)]
            })

    return samples


def write_excel(sheets):
    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl") as writer:
        for sheet_name, df in sheets.items():
            safe_name = sheet_name[:31]
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
    print("Connecting to Azure SQL...")
    engine = get_engine()

    print("Reading connection info...")
    connection_info = get_connection_info(engine)

    print("Reading all tables...")
    all_tables = get_all_tables(engine)

    print("Reading all columns...")
    all_columns = get_all_columns(engine)

    print("Finding candidate production tables...")
    candidate_tables = get_candidate_tables(engine)

    print("Counting rows for candidate tables...")
    row_counts = get_table_row_counts(engine, candidate_tables)

    print("Pulling TOP 50 sample rows from top candidate tables...")
    samples = get_sample_data(engine, candidate_tables, max_tables=12)

    sheets = {
        "Connection_Info": connection_info,
        "All_Tables": all_tables,
        "All_Columns": all_columns,
        "Candidate_Tables": candidate_tables,
        "Candidate_Row_Counts": row_counts,
    }

    sheets.update(samples)

    print("Writing Excel...")
    write_excel(sheets)

    print("\nDiscovery completed successfully:")
    print(EXCEL_PATH.resolve())


if __name__ == "__main__":
    main()
