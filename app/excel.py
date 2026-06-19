import pyodbc
import pandas as pd
from pathlib import Path

# =========================
# AZURE SQL CONNECTION
# =========================
SERVER = "ga......"       # Data Source
DATABASE = "ga......"     # Initial Catalog
USERNAME = "sk..."        # User ID
DRIVER = "ODBC Driver 18 for SQL Server"

OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

EXCEL_PATH = OUTPUT_DIR / "azure_db_discovery.xlsx"


def connect_to_azure_sql():
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
    return pyodbc.connect(conn_str)


def read_sql(conn, sql):
    return pd.read_sql_query(sql, conn)


def main():
    conn = connect_to_azure_sql()
    print("Connected successfully.")

    connection_info_sql = """
    SELECT
        @@SERVERNAME AS server_name,
        DB_NAME() AS database_name,
        SUSER_SNAME() AS login_name,
        CURRENT_USER AS database_user,
        @@VERSION AS sql_version;
    """

    tables_sql = """
    SELECT
        TABLE_SCHEMA,
        TABLE_NAME,
        TABLE_TYPE
    FROM INFORMATION_SCHEMA.TABLES
    ORDER BY TABLE_SCHEMA, TABLE_NAME;
    """

    columns_sql = """
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

    search_834_tables_sql = """
    SELECT
        TABLE_SCHEMA,
        TABLE_NAME,
        TABLE_TYPE
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME LIKE '%834%'
       OR TABLE_NAME LIKE '%Inbound%'
       OR TABLE_NAME LIKE '%enroll%'
       OR TABLE_NAME LIKE '%member%'
       OR TABLE_NAME LIKE '%policy%'
       OR TABLE_NAME LIKE '%detail%'
       OR TABLE_NAME LIKE '%header%'
    ORDER BY TABLE_SCHEMA, TABLE_NAME;
    """

    connection_info = read_sql(conn, connection_info_sql)
    tables = read_sql(conn, tables_sql)
    columns = read_sql(conn, columns_sql)
    candidate_tables = read_sql(conn, search_834_tables_sql)

    # Row counts for candidate tables only
    row_counts = []

    for _, row in candidate_tables.iterrows():
        schema = row["TABLE_SCHEMA"]
        table = row["TABLE_NAME"]

        try:
            sql = f"SELECT COUNT(*) AS row_count FROM [{schema}].[{table}]"
            count_df = read_sql(conn, sql)

            row_counts.append({
                "TABLE_SCHEMA": schema,
                "TABLE_NAME": table,
                "row_count": int(count_df.iloc[0]["row_count"])
            })

            print(f"{schema}.{table}: {int(count_df.iloc[0]['row_count'])}")

        except Exception as e:
            row_counts.append({
                "TABLE_SCHEMA": schema,
                "TABLE_NAME": table,
                "row_count": "ERROR",
                "error": str(e)
            })

    row_counts_df = pd.DataFrame(row_counts)

    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl") as writer:
        connection_info.to_excel(writer, sheet_name="Connection_Info", index=False)
        tables.to_excel(writer, sheet_name="All_Tables", index=False)
        columns.to_excel(writer, sheet_name="All_Columns", index=False)
        candidate_tables.to_excel(writer, sheet_name="Candidate_834_Tables", index=False)
        row_counts_df.to_excel(writer, sheet_name="Candidate_Row_Counts", index=False)

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

    conn.close()

    print("\nDiscovery completed.")
    print(EXCEL_PATH.resolve())


if __name__ == "__main__":
    main()
