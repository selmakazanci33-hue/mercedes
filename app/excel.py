import sqlite3
import urllib.parse
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

# =========================
# CONFIG
# =========================

SERVER = "ga......"
DATABASE = "ga......"
USERNAME = "sk..."
DRIVER = "ODBC Driver 18 for SQL Server"

SQLITE_DB_PATH = Path("data/issuer_834.db")
OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_EXCEL = OUTPUT_DIR / "FINAL_XML_vs_AZURE_ENROLLMENTS_ORACLE.xlsx"

HISTORY_MONTHS = [
    ("2025", "10"), ("2025", "11"), ("2025", "12"),
    ("2026", "01"), ("2026", "02"), ("2026", "03"), ("2026", "04"), ("2026", "05"),
]

REPORT_MONTHS = [
    ("2026", "01"), ("2026", "02"), ("2026", "03"), ("2026", "04"), ("2026", "05"),
]


# =========================
# AZURE CONNECTION
# =========================

def get_azure_engine():
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


def read_azure(engine, sql):
    with engine.connect() as conn:
        return pd.read_sql_query(text(sql), conn)


# =========================
# XML / SQLITE
# =========================

def read_xml_sqlite():
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


def clean_xml(df):
    df = df.copy()

    df["source"] = "XML"
    df["issuer"] = df["issuer"].astype(str)
    df["year"] = df["year"].astype(str)
    df["month"] = df["month"].astype(str).str.zfill(2)

    df["xml_status"] = df["additional_maint_reason_code"].replace({"REINSTATE": "CONFIRM"})

    df["insurance_type"] = df["insurance_type_code"].apply(
        lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
    )

    df["policy_id"] = df["policy_id"].astype(str)
    df["member_id"] = df["member_id"].astype(str)

    df["benefit_effective_date"] = pd.to_datetime(df["benefit_effective_date"], errors="coerce")
    df["benefit_end_date"] = pd.to_datetime(df["benefit_end_date"], errors="coerce")
    df["member_maint_effective_date"] = pd.to_datetime(df["member_maint_effective_date"], errors="coerce")

    df["report_flag"] = df[["year", "month"]].apply(
        lambda r: (r["year"], r["month"]) in REPORT_MONTHS,
        axis=1
    )

    df["join_key"] = (
        df["issuer"] + "|" +
        df["policy_id"] + "|" +
        df["member_id"] + "|" +
        df["insurance_type"]
    )

    # one row per XML business entity
    df = df.sort_values([
        "join_key",
        "member_maint_effective_date",
        "benefit_effective_date",
        "raw_xml_path"
    ])

    df = df.drop_duplicates(["join_key", "year", "month"], keep="last")

    return df


# =========================
# AZURE FINAL BUSINESS TABLE
# =========================

def read_azure_enrollments(engine):
    sql = """
    SELECT
        coverage_year AS year,
        hios_issuer_id AS issuer,
        Insurance_Type AS insurance_type,
        enrollment_id AS policy_id,
        enrollee_id AS member_id,
        enrollment_status_description,
        enrollee_status_description,
        benefit_effective_date,
        benefit_end_date,
        enrollment_confirmation_date,
        enrollment_create_date,
        enrollment_last_update_date,
        enrollee_start_date,
        enrollee_end_date,
        enrollee_create_date,
        enrollee_last_update_date
    FROM dbo.Enrollments_PY2026
    WHERE coverage_year = 2026
    """

    return read_azure(engine, sql)


def clean_azure(df):
    df = df.copy()

    df["source"] = "AZURE_ENROLLMENTS_PY2026"
    df["issuer"] = df["issuer"].astype(str)
    df["year"] = df["year"].astype(str)
    df["policy_id"] = df["policy_id"].astype(str)
    df["member_id"] = df["member_id"].astype(str)

    df["insurance_type"] = df["insurance_type"].apply(
        lambda x: "Dental" if str(x).lower().startswith("dent") else "Health"
    )

    for col in [
        "benefit_effective_date",
        "benefit_end_date",
        "enrollment_confirmation_date",
        "enrollment_create_date",
        "enrollment_last_update_date",
        "enrollee_start_date",
        "enrollee_end_date",
        "enrollee_create_date",
        "enrollee_last_update_date",
    ]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    df["azure_status"] = df["enrollee_status_description"].fillna(
        df["enrollment_status_description"]
    )

    df["join_key"] = (
        df["issuer"] + "|" +
        df["policy_id"] + "|" +
        df["member_id"] + "|" +
        df["insurance_type"]
    )

    # create month rows from benefit window Jan-May
    rows = []

    for year, month in REPORT_MONTHS:
        start = pd.Timestamp(f"{year}-{month}-01")
        end = start + pd.offsets.MonthEnd(0)

        active = df[
            (df["benefit_effective_date"].isna() | (df["benefit_effective_date"] <= end)) &
            (df["benefit_end_date"].isna() | (df["benefit_end_date"] >= start))
        ].copy()

        active["report_year"] = year
        active["report_month"] = month
        rows.append(active)

    if rows:
        out = pd.concat(rows, ignore_index=True)
    else:
        out = pd.DataFrame()

    return out


# =========================
# RECONCILIATION
# =========================

def reconcile(xml, azure):
    xml_report = xml[xml["report_flag"] == True].copy()

    xml_keys = xml_report[[
        "join_key", "issuer", "year", "month", "policy_id", "member_id",
        "insurance_type", "xml_status", "benefit_effective_date",
        "benefit_end_date", "raw_xml_path"
    ]].rename(columns={
        "year": "xml_year",
        "month": "xml_month",
        "benefit_effective_date": "xml_benefit_effective_date",
        "benefit_end_date": "xml_benefit_end_date",
    })

    azure_keys = azure[[
        "join_key", "issuer", "report_year", "report_month",
        "policy_id", "member_id", "insurance_type",
        "azure_status", "enrollment_status_description",
        "enrollee_status_description",
        "benefit_effective_date",
        "benefit_end_date"
    ]].rename(columns={
        "report_year": "azure_year",
        "report_month": "azure_month",
        "benefit_effective_date": "azure_benefit_effective_date",
        "benefit_end_date": "azure_benefit_end_date",
    })

    merged = xml_keys.merge(
        azure_keys,
        how="outer",
        left_on=["join_key", "xml_year", "xml_month"],
        right_on=["join_key", "azure_year", "azure_month"],
        suffixes=("_xml", "_azure"),
        indicator=True
    )

    def reason(row):
        if row["_merge"] == "left_only":
            return "XML_NOT_IN_AZURE_FINAL_TABLE"
        if row["_merge"] == "right_only":
            return "AZURE_FINAL_NOT_IN_XML_CURRENT_MONTH"
        if str(row.get("xml_status", "")).upper() not in str(row.get("azure_status", "")).upper():
            return "STATUS_DIFFERENCE"
        return "MATCH"

    merged["reconciliation_result"] = merged.apply(reason, axis=1)

    return merged


def summaries(xml, azure, recon):
    xml_summary = (
        xml[xml["report_flag"] == True]
        .groupby(["issuer", "year", "month", "insurance_type", "xml_status"], dropna=False)
        .agg(
            xml_rows=("join_key", "size"),
            xml_enrollment_count=("policy_id", "nunique"),
            xml_enrollee_count=("member_id", "nunique"),
        )
        .reset_index()
    )

    azure_summary = (
        azure
        .groupby(["issuer", "report_year", "report_month", "insurance_type", "azure_status"], dropna=False)
        .agg(
            azure_rows=("join_key", "size"),
            azure_enrollment_count=("policy_id", "nunique"),
            azure_enrollee_count=("member_id", "nunique"),
        )
        .reset_index()
        .rename(columns={
            "report_year": "year",
            "report_month": "month",
            "azure_status": "status"
        })
    )

    result_summary = (
        recon.groupby(["reconciliation_result"], dropna=False)
        .agg(rows=("join_key", "size"))
        .reset_index()
        .sort_values("rows", ascending=False)
    )

    issuer_month_result = (
        recon.groupby([
            recon["issuer_xml"].fillna(recon["issuer_azure"]),
            recon["xml_year"].fillna(recon["azure_year"]),
            recon["xml_month"].fillna(recon["azure_month"]),
            "reconciliation_result"
        ], dropna=False)
        .agg(rows=("join_key", "size"))
        .reset_index()
    )

    issuer_month_result.columns = ["issuer", "year", "month", "reconciliation_result", "rows"]

    return xml_summary, azure_summary, result_summary, issuer_month_result


# =========================
# EXPORT
# =========================

def write_excel(sheets):
    with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
        for name, df in sheets.items():
            df.head(1_048_000).to_excel(writer, sheet_name=name[:31], index=False)

    print(f"Created: {OUTPUT_EXCEL.resolve()}")


# =========================
# MAIN
# =========================

def main():
    print("Reading XML SQLite...")
    xml_raw = read_xml_sqlite()
    xml = clean_xml(xml_raw)
    print(f"XML rows: {len(xml)}")

    print("Connecting Azure...")
    engine = get_azure_engine()

    print("Reading Azure Enrollments_PY2026...")
    azure_raw = read_azure_enrollments(engine)
    azure = clean_azure(azure_raw)
    print(f"Azure report rows: {len(azure)}")

    print("Reconciling XML vs Azure final business table...")
    recon = reconcile(xml, azure)

    xml_summary, azure_summary, result_summary, issuer_month_result = summaries(xml, azure, recon)

    xml_not_azure = recon[recon["reconciliation_result"] == "XML_NOT_IN_AZURE_FINAL_TABLE"]
    azure_not_xml = recon[recon["reconciliation_result"] == "AZURE_FINAL_NOT_IN_XML_CURRENT_MONTH"]
    status_diff = recon[recon["reconciliation_result"] == "STATUS_DIFFERENCE"]

    write_excel({
        "Final_Result_Summary": result_summary,
        "Issuer_Month_Result": issuer_month_result,
        "XML_Summary": xml_summary,
        "Azure_Final_Summary": azure_summary,
        "XML_Not_In_Azure": xml_not_azure,
        "Azure_Not_In_XML": azure_not_xml,
        "Status_Difference": status_diff,
        "Full_Reconciliation": recon,
    })

    print("Done cicim.")


if __name__ == "__main__":
    main()
