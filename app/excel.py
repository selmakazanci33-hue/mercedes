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
END_DATE = "2026-06-01"   # Jan-May

SQLITE_DB_PATH = Path("data/issuer_834.db")

OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_EXCEL = OUTPUT_DIR / "final_db_vs_xml_834_comparison_jan_may_2026.xlsx"

# Azure SQL - replace with your real values
SERVER = "ga......"
DATABASE = "ga......"
USERNAME = "sk..."
DRIVER = "ODBC Driver 18 for SQL Server"


# =========================
# CONNECTIONS
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
# AZURE DB DATA
# =========================
def get_db_834_raw(engine):
    sql = f"""
    SELECT
        Coverage_Year AS year,
        GAA_HIOS_ID AS issuer,
        GAA_834_File_Name AS file_name,
        GAA_834_File_Date AS file_date,

        exchgAssignedPolicyID AS policy_id,
        exchgIndivIdentifier AS member_id,
        exchgSubscriberIdentifier AS subscriber_id,
        householdOrEmployeeCaseID AS household_id,

        Insurance_Type AS insurance_type,
        enrolleeStatus AS status,

        subscriberFlag AS subscriber_flag,
        member_relationship AS relationship,

        benefitEffectiveBeginDate AS benefit_effective_date,
        benefitEffectiveEndDate AS benefit_end_date,
        memberMaintEffectiveDate AS member_maint_effective_date,

        memberFirstName AS first_name,
        memberLastName AS last_name,
        memberBirthDate AS birth_date,

        healthCoveragePremiumAmt AS premium_amount,
        totalIndivResponsibilityAmt AS responsibility_amount,
        aptcAmt AS aptc_amount,
        csrAmt AS csr_amount
    FROM dbo.834_Inbound_test
    WHERE Coverage_Year = {YEAR}
      AND GAA_834_File_Date >= '{START_DATE}'
      AND GAA_834_File_Date < '{END_DATE}'
      AND enrolleeStatus IN ('CONFIRM', 'REINSTATE', 'CANCEL', 'TERM')
    """
    return read_azure(engine, sql)


def get_db_header_summary(engine):
    sql = f"""
    SELECT
        GAA_HIOS_ID AS issuer,
        GAA_834_File_Name AS file_name,
        GAA_834_File_Date AS file_date,
        record_count,
        enrollment_count,
        enrollee_count,
        confirm_count,
        cancel_count,
        term_count
    FROM dbo.834_Inbound_header_test
    WHERE GAA_834_File_Date >= '{START_DATE}'
      AND GAA_834_File_Date < '{END_DATE}'
    """
    return read_azure(engine, sql)


# =========================
# XML / SQLITE DATA
# =========================
def get_xml_raw():
    if not SQLITE_DB_PATH.exists():
        raise FileNotFoundError(f"SQLite DB not found: {SQLITE_DB_PATH.resolve()}")

    conn = sqlite3.connect(SQLITE_DB_PATH)

    sql = f"""
    SELECT
        year,
        issuer,
        month,
        raw_xml_path AS file_name,

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
        member_maint_effective_date
    FROM stg_834_records
    WHERE year = '{YEAR}'
      AND month IN ('01','02','03','04','05')
      AND additional_maint_reason_code IN ('CONFIRM', 'REINSTATE', 'CANCEL', 'TERM')
    """

    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


# =========================
# CLEANUP
# =========================
def clean_db_834(df):
    clean = df.copy()

    clean["source"] = "AZURE_DB"
    clean["issuer"] = clean["issuer"].astype(str)
    clean["year"] = clean["year"].astype(str)
    clean["month"] = pd.to_datetime(clean["file_date"], errors="coerce").dt.strftime("%m")

    clean["status"] = clean["status"].replace({
        "REINSTATE": "CONFIRM"
    })

    clean["insurance_type"] = clean["insurance_type"].fillna("Unknown")

    clean["enrollment_key"] = clean["policy_id"].astype(str)

    return clean


def clean_xml(df):
    clean = df.copy()

    clean["source"] = "XML_SQLITE"
    clean["issuer"] = clean["issuer"].astype(str)
    clean["year"] = clean["year"].astype(str)
    clean["month"] = clean["month"].astype(str).str.zfill(2)

    clean["status"] = clean["additional_maint_reason_code"].replace({
        "REINSTATE": "CONFIRM"
    })

    clean["insurance_type"] = clean["insurance_type_code"].apply(
        lambda x: "Dental" if str(x).upper() == "DEN" else "Health"
    )

    def enrollment_key(row):
        for col in ["policy_id", "subscriber_id", "household_id"]:
            val = row.get(col)
            if pd.notna(val) and str(val).strip() not in ["", "None", "nan"]:
                return str(val)
        return None

    clean["enrollment_key"] = clean.apply(enrollment_key, axis=1)

    return clean


# =========================
# SUMMARIES
# =========================
def summarize_records(df, prefix):
    return (
        df.groupby(
            ["issuer", "year", "month", "insurance_type", "status"],
            dropna=False
        )
        .agg(
            **{
                f"{prefix}_raw_rows": ("member_id", "size"),
                f"{prefix}_enrollment_count": ("enrollment_key", "nunique"),
                f"{prefix}_enrollee_count": ("member_id", "nunique"),
                f"{prefix}_subscriber_count": ("subscriber_id", "nunique"),
                f"{prefix}_file_count": ("file_name", "nunique"),
            }
        )
        .reset_index()
    )


def summarize_by_file(df, prefix):
    return (
        df.groupby(
            ["issuer", "year", "month", "file_name"],
            dropna=False
        )
        .agg(
            **{
                f"{prefix}_raw_rows": ("member_id", "size"),
                f"{prefix}_enrollment_count": ("enrollment_key", "nunique"),
                f"{prefix}_enrollee_count": ("member_id", "nunique"),
                f"{prefix}_confirm_count": ("status", lambda x: (x == "CONFIRM").sum()),
                f"{prefix}_cancel_count": ("status", lambda x: (x == "CANCEL").sum()),
                f"{prefix}_term_count": ("status", lambda x: (x == "TERM").sum()),
            }
        )
        .reset_index()
    )


# =========================
# COMPARISON
# =========================
def compare_summaries(db_summary, xml_summary):
    comparison = pd.merge(
        db_summary,
        xml_summary,
        how="outer",
        on=["issuer", "year", "month", "insurance_type", "status"]
    )

    numeric_cols = [
        "db_raw_rows", "db_enrollment_count", "db_enrollee_count", "db_subscriber_count", "db_file_count",
        "xml_raw_rows", "xml_enrollment_count", "xml_enrollee_count", "xml_subscriber_count", "xml_file_count",
    ]

    for col in numeric_cols:
        if col in comparison.columns:
            comparison[col] = comparison[col].fillna(0).astype(int)

    comparison["raw_row_diff"] = comparison["db_raw_rows"] - comparison["xml_raw_rows"]
    comparison["enrollment_diff"] = comparison["db_enrollment_count"] - comparison["xml_enrollment_count"]
    comparison["enrollee_diff"] = comparison["db_enrollee_count"] - comparison["xml_enrollee_count"]
    comparison["subscriber_diff"] = comparison["db_subscriber_count"] - comparison["xml_subscriber_count"]

    comparison["match_status"] = comparison.apply(
        lambda r: "MATCH"
        if r["raw_row_diff"] == 0
        and r["enrollment_diff"] == 0
        and r["enrollee_diff"] == 0
        else "MISMATCH",
        axis=1
    )

    return comparison.sort_values(
        ["match_status", "issuer", "year", "month", "insurance_type", "status"]
    )


def issuer_month_comparison(db_clean, xml_clean):
    db_issuer = (
        db_clean.groupby(["issuer", "year", "month"], dropna=False)
        .agg(
            db_raw_rows=("member_id", "size"),
            db_enrollment_count=("enrollment_key", "nunique"),
            db_enrollee_count=("member_id", "nunique"),
            db_file_count=("file_name", "nunique"),
        )
        .reset_index()
    )

    xml_issuer = (
        xml_clean.groupby(["issuer", "year", "month"], dropna=False)
        .agg(
            xml_raw_rows=("member_id", "size"),
            xml_enrollment_count=("enrollment_key", "nunique"),
            xml_enrollee_count=("member_id", "nunique"),
            xml_file_count=("file_name", "nunique"),
        )
        .reset_index()
    )

    comp = pd.merge(
        db_issuer,
        xml_issuer,
        how="outer",
        on=["issuer", "year", "month"]
    ).fillna(0)

    for col in comp.columns:
        if col.endswith("_count") or col.endswith("_rows"):
            comp[col] = comp[col].astype(int)

    comp["raw_row_diff"] = comp["db_raw_rows"] - comp["xml_raw_rows"]
    comp["enrollment_diff"] = comp["db_enrollment_count"] - comp["xml_enrollment_count"]
    comp["enrollee_diff"] = comp["db_enrollee_count"] - comp["xml_enrollee_count"]
    comp["file_count_diff"] = comp["db_file_count"] - comp["xml_file_count"]

    comp["match_status"] = comp.apply(
        lambda r: "MATCH"
        if r["raw_row_diff"] == 0
        and r["enrollment_diff"] == 0
        and r["enrollee_diff"] == 0
        else "MISMATCH",
        axis=1
    )

    return comp.sort_values(["match_status", "issuer", "year", "month"])


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
    print("Connecting to Azure...")
    engine = get_azure_engine()

    print("Reading Azure 834 raw data...")
    db_raw = get_db_834_raw(engine)
    db_clean = clean_db_834(db_raw)

    print("Reading Azure 834 header summary...")
    db_header = get_db_header_summary(engine)

    print("Reading XML / SQLite data...")
    xml_raw = get_xml_raw()
    xml_clean = clean_xml(xml_raw)

    print("Creating summaries...")
    db_summary = summarize_records(db_clean, "db")
    xml_summary = summarize_records(xml_clean, "xml")

    db_file_summary = summarize_by_file(db_clean, "db")
    xml_file_summary = summarize_by_file(xml_clean, "xml")

    comparison = compare_summaries(db_summary, xml_summary)
    issuer_month_comp = issuer_month_comparison(db_clean, xml_clean)

    print("Writing Excel...")
    write_excel(OUTPUT_EXCEL, {
        "DB_834_Raw": db_raw,
        "DB_834_Clean": db_clean,
        "DB_Header_Summary": db_header,
        "XML_Raw": xml_raw,
        "XML_Clean": xml_clean,
        "DB_Summary": db_summary,
        "XML_Summary": xml_summary,
        "DB_vs_XML_Status": comparison,
        "Issuer_Month_Comparison": issuer_month_comp,
        "DB_File_Summary": db_file_summary,
        "XML_File_Summary": xml_file_summary,
    })

    print("\nDone cicim:")
    print(OUTPUT_EXCEL.resolve())


if __name__ == "__main__":
    main()
