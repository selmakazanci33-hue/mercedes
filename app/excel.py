import sqlite3
import urllib.parse
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text


# =========================
# SETTINGS
# =========================
YEAR = 2026
START_DATE = "2026-01-01"
END_DATE = "2026-06-01"   # Jan-May only

OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

AZURE_REPORT = OUTPUT_DIR / "azure_db_report_2026_jan_may.xlsx"
XML_REPORT = OUTPUT_DIR / "xml_834_report_2026_jan_may.xlsx"
COMPARISON_REPORT = OUTPUT_DIR / "db_vs_xml_comparison_2026_jan_may.xlsx"

SQLITE_DB_PATH = Path("data/issuer_834.db")

# Azure SQL
SERVER = "ga......"       # Data Source
DATABASE = "ga......"     # Initial Catalog
USERNAME = "sk..."        # User ID
DRIVER = "ODBC Driver 18 for SQL Server"


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


# =========================
# AZURE DB REPORT
# =========================
def get_azure_detail(engine):
    sql = f"""
    WITH long_data AS (

        SELECT
            'PA' AS source_side,
            PA_hios_issuer_id AS issuer,
            PA_insurer_name AS insurer_name,
            PA_coverage_year AS coverage_year,
            PA_ssap_application_id AS application_id,
            PA_household_id AS household_id,
            PA_enrollment_id AS enrollment_id,
            PA_enrollee_id AS enrollee_id,
            PA_relationship_type AS relationship_type,
            PA_person_type AS person_type,
            PA_Insurance_Type AS insurance_type,
            PA_enrollment_status_description AS enrollment_status,
            PA_enrollee_status_description AS enrollee_status,
            PA_benefit_effective_date AS benefit_effective_date,
            PA_benefit_end_date AS benefit_end_date,
            PA_enrollment_confirmation_date AS enrollment_confirmation_date,
            PA_enrollment_create_date AS enrollment_create_date,
            PA_enrollment_last_update_date AS enrollment_last_update_date
        FROM dbo.DuplicateEnrollment_Overlap

        UNION ALL

        SELECT
            'S' AS source_side,
            S_hios_issuer_id AS issuer,
            S_insurer_name AS insurer_name,
            S_coverage_year AS coverage_year,
            S_ssap_application_id AS application_id,
            S_household_id AS household_id,
            S_enrollment_id AS enrollment_id,
            S_enrollee_id AS enrollee_id,
            S_relationship_type AS relationship_type,
            S_person_type AS person_type,
            S_Insurance_Type AS insurance_type,
            S_enrollment_status_description AS enrollment_status,
            S_enrollee_status_description AS enrollee_status,
            S_benefit_effective_date AS benefit_effective_date,
            S_benefit_end_date AS benefit_end_date,
            S_enrollment_confirmation_date AS enrollment_confirmation_date,
            S_enrollment_create_date AS enrollment_create_date,
            S_enrollment_last_update_date AS enrollment_last_update_date
        FROM dbo.DuplicateEnrollment_Overlap
    )
    SELECT *
    FROM long_data
    WHERE coverage_year = {YEAR}
      AND issuer IS NOT NULL
      AND (
            benefit_effective_date >= '{START_DATE}' AND benefit_effective_date < '{END_DATE}'
         OR enrollment_confirmation_date >= '{START_DATE}' AND enrollment_confirmation_date < '{END_DATE}'
         OR enrollment_create_date >= '{START_DATE}' AND enrollment_create_date < '{END_DATE}'
         OR enrollment_last_update_date >= '{START_DATE}' AND enrollment_last_update_date < '{END_DATE}'
      );
    """

    return pd.read_sql_query(text(sql), engine)


def clean_azure(df):
    clean = df.copy()

    clean["month"] = pd.to_datetime(
        clean["benefit_effective_date"].fillna(clean["enrollment_confirmation_date"]),
        errors="coerce"
    ).dt.strftime("%m")

    clean["normalized_status"] = clean["enrollment_status"].replace({
        "Enrolled": "CONFIRM",
        "Pending": "CONFIRM",
        "Pend": "CONFIRM",
        "Cancelled": "CANCEL",
        "Pend canceled": "CANCEL",
        "Terminated": "TERM",
        "Aborted": "ABORTED"
    })

    clean["normalized_insurance_type"] = clean["insurance_type"].fillna("Unknown")

    return clean


def summarize_azure(clean):
    return (
        clean
        .groupby(
            ["issuer", "coverage_year", "month", "normalized_insurance_type", "normalized_status"],
            dropna=False
        )
        .agg(
            db_raw_rows=("enrollment_id", "size"),
            db_enrollment_count=("enrollment_id", "nunique"),
            db_enrollee_count=("enrollee_id", "nunique"),
            db_application_count=("application_id", "nunique"),
            db_household_count=("household_id", "nunique")
        )
        .reset_index()
        .rename(columns={
            "coverage_year": "year",
            "normalized_insurance_type": "insurance_type",
            "normalized_status": "status"
        })
    )


# =========================
# XML / SQLITE REPORT
# =========================
def get_sqlite_detail():
    if not SQLITE_DB_PATH.exists():
        raise FileNotFoundError(f"SQLite DB not found: {SQLITE_DB_PATH.resolve()}")

    conn = sqlite3.connect(SQLITE_DB_PATH)

    sql = f"""
    SELECT
        issuer,
        year,
        month,
        policy_id,
        member_id,
        subscriber_id,
        household_or_employee_case_id,
        insurance_type_code,
        additional_maint_reason_code,
        benefit_effective_date,
        benefit_end_date,
        member_maint_effective_date,
        raw_xml_path
    FROM stg_834_records
    WHERE year = '{YEAR}'
      AND month IN ('01','02','03','04','05')
      AND additional_maint_reason_code IN ('CONFIRM', 'REINSTATE', 'CANCEL', 'TERM');
    """

    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def clean_xml(df):
    clean = df.copy()

    clean["status"] = clean["additional_maint_reason_code"].replace({
        "REINSTATE": "CONFIRM"
    })

    clean["insurance_type"] = clean["insurance_type_code"].apply(
        lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
    )

    def enrollment_key(row):
        for col, prefix in [
            ("policy_id", "policy"),
            ("subscriber_id", "subscriber"),
            ("household_or_employee_case_id", "household"),
        ]:
            val = row.get(col)
            if pd.notna(val) and str(val).strip():
                return f"{prefix}:{val}"
        return None

    clean["enrollment_key"] = clean.apply(enrollment_key, axis=1)

    return clean


def summarize_xml(clean):
    return (
        clean
        .groupby(["issuer", "year", "month", "insurance_type", "status"], dropna=False)
        .agg(
            xml_raw_rows=("member_id", "size"),
            xml_enrollment_count=("enrollment_key", "nunique"),
            xml_enrollee_count=("member_id", "nunique"),
            xml_policy_count=("policy_id", "nunique"),
            xml_subscriber_count=("subscriber_id", "nunique")
        )
        .reset_index()
    )


# =========================
# COMPARISON
# =========================
def compare_reports(db_summary, xml_summary):
    db_summary["issuer"] = db_summary["issuer"].astype(str)
    db_summary["year"] = db_summary["year"].astype(str)
    db_summary["month"] = db_summary["month"].astype(str).str.zfill(2)

    xml_summary["issuer"] = xml_summary["issuer"].astype(str)
    xml_summary["year"] = xml_summary["year"].astype(str)
    xml_summary["month"] = xml_summary["month"].astype(str).str.zfill(2)

    comparison = pd.merge(
        db_summary,
        xml_summary,
        how="outer",
        on=["issuer", "year", "month", "insurance_type", "status"]
    )

    for col in [
        "db_raw_rows", "db_enrollment_count", "db_enrollee_count",
        "xml_raw_rows", "xml_enrollment_count", "xml_enrollee_count"
    ]:
        if col in comparison.columns:
            comparison[col] = comparison[col].fillna(0).astype(int)

    comparison["enrollment_diff"] = (
        comparison["db_enrollment_count"] - comparison["xml_enrollment_count"]
    )

    comparison["enrollee_diff"] = (
        comparison["db_enrollee_count"] - comparison["xml_enrollee_count"]
    )

    comparison["raw_row_diff"] = (
        comparison["db_raw_rows"] - comparison["xml_raw_rows"]
    )

    comparison["match_status"] = comparison.apply(
        lambda r: "MATCH"
        if r["enrollment_diff"] == 0 and r["enrollee_diff"] == 0
        else "MISMATCH",
        axis=1
    )

    return comparison


# =========================
# EXCEL WRITER
# =========================
def write_excel(path, sheets):
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
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


# =========================
# MAIN
# =========================
def main():
    print("Connecting to Azure DB...")
    engine = get_azure_engine()

    print("Reading Azure DB data...")
    azure_raw = get_azure_detail(engine)
    azure_clean = clean_azure(azure_raw)
    azure_summary = summarize_azure(azure_clean)

    print("Reading XML / SQLite data...")
    xml_raw = get_sqlite_detail()
    xml_clean = clean_xml(xml_raw)
    xml_summary = summarize_xml(xml_clean)

    print("Creating comparison...")
    comparison = compare_reports(azure_summary, xml_summary)

    print("Writing Azure DB report...")
    write_excel(AZURE_REPORT, {
        "Azure_Raw_Data": azure_raw,
        "Azure_Clean_Data": azure_clean,
        "Azure_Summary": azure_summary
    })

    print("Writing XML report...")
    write_excel(XML_REPORT, {
        "XML_Raw_Data": xml_raw,
        "XML_Clean_Data": xml_clean,
        "XML_Summary": xml_summary
    })

    print("Writing comparison report...")
    write_excel(COMPARISON_REPORT, {
        "DB_vs_XML_Comparison": comparison,
        "Azure_Summary": azure_summary,
        "XML_Summary": xml_summary
    })

    print("\nDone.")
    print(AZURE_REPORT.resolve())
    print(XML_REPORT.resolve())
    print(COMPARISON_REPORT.resolve())


if __name__ == "__main__":
    main()
