import sqlite3
import urllib.parse
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text


# =====================================================
# CONFIG - keep same credential style
# =====================================================

SERVER = "YOUR_SERVER"
DATABASE = "YOUR_DATABASE"
USERNAME = "YOUR_USERNAME"
DRIVER = "ODBC Driver 18 for SQL Server"

SQLITE_DB_PATH = Path("data/issuer_834.db")

OUTPUT_DIR = Path("query_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_EXCEL = OUTPUT_DIR / "FINAL_XML_vs_AZURE_ORACLE.xlsx"

HISTORY_MONTHS = [
    ("2025", "10"), ("2025", "11"), ("2025", "12"),
    ("2026", "01"), ("2026", "02"), ("2026", "03"),
    ("2026", "04"), ("2026", "05"),
]


# =====================================================
# CONNECTIONS
# =====================================================

def get_azure_engine():
    conn_str = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        "Authentication=ActiveDirectoryInteractive;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=30;"
    )
    quoted = urllib.parse.quote_plus(conn_str)
    return create_engine(f"mssql+pyodbc:///?odbc_connect={quoted}")


# =====================================================
# NORMALIZATION
# =====================================================

def norm_status(x):
    if pd.isna(x):
        return None
    v = str(x).strip().upper()
    if v in {"CONFIRM", "REINSTATE", "ENROLLED", "ENROLL", "ACTIVE"}:
        return "ENROLLED"
    if v in {"CANCEL", "CANCELLED", "CANCELED"}:
        return "CANCELLED"
    if v in {"TERM", "TERMINATED"}:
        return "TERMINATED"
    if v in {"PENDING", "PEND"}:
        return "PENDING"
    return v


def norm_insurance(x):
    if pd.isna(x):
        return None
    v = str(x).strip().upper()
    if v in {"DEN", "DENTAL"} or "DENTAL" in v:
        return "DENTAL"
    return "HEALTH"


def clean_id(x):
    if pd.isna(x):
        return None
    v = str(x).strip()
    if v in {"", "None", "nan", "NaN"}:
        return None
    if v.endswith(".0"):
        v = v[:-2]
    return v


# =====================================================
# XML SQLITE SNAPSHOT
# =====================================================

def read_xml_from_sqlite():
    where_sql = " OR ".join(
        [f"(year='{y}' AND month='{m}')" for y, m in HISTORY_MONTHS]
    )

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
        additional_maint_reason_code AS xml_raw_status,
        benefit_effective_date,
        benefit_end_date,
        member_maint_effective_date,
        raw_xml_path
    FROM stg_834_records
    WHERE ({where_sql})
      AND additional_maint_reason_code IN ('CONFIRM','REINSTATE','CANCEL','TERM')
    """

    conn = sqlite3.connect(SQLITE_DB_PATH)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def build_xml_latest_snapshot(df):
    df = df.copy()

    df["issuer"] = df["issuer"].apply(clean_id)
    df["policy_id"] = df["policy_id"].apply(clean_id)
    df["member_id"] = df["member_id"].apply(clean_id)
    df["subscriber_id"] = df["subscriber_id"].apply(clean_id)
    df["insurance_type"] = df["insurance_type_code"].apply(norm_insurance)
    df["xml_status"] = df["xml_raw_status"].apply(norm_status)

    for c in ["benefit_effective_date", "benefit_end_date", "member_maint_effective_date"]:
        df[c] = pd.to_datetime(df[c], errors="coerce")

    df["event_month_date"] = pd.to_datetime(
        df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-01",
        errors="coerce"
    )

    df["event_date"] = (
        df["member_maint_effective_date"]
        .fillna(df["benefit_effective_date"])
        .fillna(df["event_month_date"])
    )

    df = df.dropna(subset=["issuer", "policy_id", "member_id", "insurance_type"])

    df["join_key"] = (
        df["issuer"] + "|" +
        df["policy_id"] + "|" +
        df["member_id"] + "|" +
        df["insurance_type"]
    )

    df = df.sort_values([
        "join_key",
        "event_date",
        "year",
        "month",
        "raw_xml_path"
    ])

    latest = df.drop_duplicates("join_key", keep="last").copy()
    return latest


# =====================================================
# AZURE FINAL SNAPSHOT
# =====================================================

def read_azure_enrollments(engine):
    sql = """
    SELECT
        CAST(hios_issuer_id AS varchar(30)) AS issuer,
        CAST(coverage_year AS varchar(10)) AS coverage_year,
        CAST(enrollment_id AS varchar(50)) AS policy_id,
        CAST(enrollee_id AS varchar(50)) AS member_id,
        CAST(Insurance_Type AS varchar(50)) AS insurance_type,
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
      AND hios_issuer_id IS NOT NULL
      AND enrollment_id IS NOT NULL
      AND enrollee_id IS NOT NULL
    """

    with engine.connect() as conn:
        return pd.read_sql_query(text(sql), conn)


def build_azure_snapshot(df):
    df = df.copy()

    df["issuer"] = df["issuer"].apply(clean_id)
    df["policy_id"] = df["policy_id"].apply(clean_id)
    df["member_id"] = df["member_id"].apply(clean_id)
    df["insurance_type"] = df["insurance_type"].apply(norm_insurance)

    df["azure_status"] = (
        df["enrollee_status_description"]
        .fillna(df["enrollment_status_description"])
        .apply(norm_status)
    )

    for c in [
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
        df[c] = pd.to_datetime(df[c], errors="coerce")

    df = df.dropna(subset=["issuer", "policy_id", "member_id", "insurance_type"])

    df["join_key"] = (
        df["issuer"] + "|" +
        df["policy_id"] + "|" +
        df["member_id"] + "|" +
        df["insurance_type"]
    )

    df = df.sort_values([
        "join_key",
        "enrollment_last_update_date",
        "enrollee_last_update_date",
        "benefit_effective_date",
    ])

    latest = df.drop_duplicates("join_key", keep="last").copy()
    return latest


# =====================================================
# RECONCILIATION
# =====================================================

def reconcile(xml, azure):
    xml_cols = [
        "join_key", "issuer", "policy_id", "member_id", "subscriber_id",
        "insurance_type", "xml_status", "xml_raw_status",
        "benefit_effective_date", "benefit_end_date",
        "event_date", "year", "month", "raw_xml_path"
    ]

    azure_cols = [
        "join_key", "issuer", "policy_id", "member_id",
        "insurance_type", "azure_status",
        "enrollment_status_description", "enrollee_status_description",
        "benefit_effective_date", "benefit_end_date",
        "enrollment_confirmation_date", "enrollment_create_date",
        "enrollment_last_update_date",
        "enrollee_start_date", "enrollee_end_date",
        "enrollee_create_date", "enrollee_last_update_date"
    ]

    merged = xml[xml_cols].merge(
        azure[azure_cols],
        on="join_key",
        how="outer",
        suffixes=("_xml", "_azure"),
        indicator=True
    )

    def result(row):
        if row["_merge"] == "left_only":
            return "XML_NOT_IN_AZURE"
        if row["_merge"] == "right_only":
            return "AZURE_NOT_IN_XML"
        if row["xml_status"] != row["azure_status"]:
            return "STATUS_DIFF"
        return "MATCH"

    merged["reconciliation_result"] = merged.apply(result, axis=1)

    merged["issuer_final"] = merged["issuer_xml"].fillna(merged["issuer_azure"])
    merged["policy_final"] = merged["policy_id_xml"].fillna(merged["policy_id_azure"])
    merged["member_final"] = merged["member_id_xml"].fillna(merged["member_id_azure"])
    merged["insurance_final"] = merged["insurance_type_xml"].fillna(merged["insurance_type_azure"])

    return merged


def build_summaries(recon):
    final_summary = (
        recon.groupby("reconciliation_result")
        .size()
        .reset_index(name="rows")
        .sort_values("rows", ascending=False)
    )

    issuer_summary = (
        recon.groupby(["issuer_final", "reconciliation_result"], dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values(["issuer_final", "rows"], ascending=[True, False])
    )

    status_summary = (
        recon.groupby(["xml_status", "azure_status", "reconciliation_result"], dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values("rows", ascending=False)
    )

    return final_summary, issuer_summary, status_summary


# =====================================================
# EXPORT
# =====================================================

def write_excel(xml_latest, azure_latest, recon, final_summary, issuer_summary, status_summary):
    with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
        final_summary.to_excel(writer, sheet_name="Final_Result_Summary", index=False)
        issuer_summary.to_excel(writer, sheet_name="Issuer_Result_Summary", index=False)
        status_summary.to_excel(writer, sheet_name="Status_Result_Summary", index=False)

        recon[recon["reconciliation_result"] == "MATCH"].head(100000).to_excel(
            writer, sheet_name="MATCH_sample", index=False
        )
        recon[recon["reconciliation_result"] == "STATUS_DIFF"].head(100000).to_excel(
            writer, sheet_name="STATUS_DIFF", index=False
        )
        recon[recon["reconciliation_result"] == "XML_NOT_IN_AZURE"].head(100000).to_excel(
            writer, sheet_name="XML_NOT_IN_AZURE", index=False
        )
        recon[recon["reconciliation_result"] == "AZURE_NOT_IN_XML"].head(100000).to_excel(
            writer, sheet_name="AZURE_NOT_IN_XML", index=False
        )

        xml_latest.head(100000).to_excel(writer, sheet_name="XML_Latest_Snapshot", index=False)
        azure_latest.head(100000).to_excel(writer, sheet_name="Azure_Latest_Snapshot", index=False)

    print(f"Created: {OUTPUT_EXCEL.resolve()}")


# =====================================================
# RUNNER
# =====================================================

def runner():
    print("Reading XML SQLite...")
    xml_raw = read_xml_from_sqlite()
    print(f"XML raw rows: {len(xml_raw)}")

    print("Building XML latest snapshot...")
    xml_latest = build_xml_latest_snapshot(xml_raw)
    print(f"XML latest rows: {len(xml_latest)}")

    print("Connecting Azure with SQLAlchemy...")
    engine = get_azure_engine()

    print("Reading Azure Enrollments_PY2026...")
    azure_raw = read_azure_enrollments(engine)
    print(f"Azure raw rows: {len(azure_raw)}")

    print("Building Azure latest snapshot...")
    azure_latest = build_azure_snapshot(azure_raw)
    print(f"Azure latest rows: {len(azure_latest)}")

    print("Reconciling...")
    recon = reconcile(xml_latest, azure_latest)

    final_summary, issuer_summary, status_summary = build_summaries(recon)

    print("\nFINAL SUMMARY")
    print(final_summary)

    print("Writing Excel...")
    write_excel(xml_latest, azure_latest, recon, final_summary, issuer_summary, status_summary)

    print("Done.")


if __name__ == "__main__":
    runner()
