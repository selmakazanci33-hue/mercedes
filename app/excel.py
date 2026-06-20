import os
import glob
import pandas as pd
import pyodbc
import xml.etree.ElementTree as ET


# =====================================================
# OLD CONNECTION STYLE - DO NOT CHANGE YOUR SYSTEM
# =====================================================

SERVER = "YOUR_SERVER"
DATABASE = "YOUR_DATABASE"
USERNAME = "YOUR_USERNAME"
DRIVER = "{ODBC Driver 17 for SQL Server}"

ASSETS_DIR = r"C:\Users\SelmaKazanci\Downloads\gaaccess-develop6\gaaccess-develop6\assets"
OUTPUT_FILE = "final_xml_vs_azure_lifecycle_comparison.xlsx"

START_YEAR_MONTH = "2025-10"
END_YEAR_MONTH = "2026-05"


def get_connection():
    return pyodbc.connect(
        f"DRIVER={DRIVER};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        "Authentication=ActiveDirectoryInteractive;"
        "TrustServerCertificate=yes;"
    )


# =====================================================
# HELPERS
# =====================================================

def normalize_status(value):
    if value is None or pd.isna(value):
        return None

    v = str(value).strip().upper()

    if v in ("CONFIRM", "CONFIRMED", "ENROLL", "ENROLLED", "ACTIVE"):
        return "ENROLLED"
    if v in ("CANCEL", "CANCELED", "CANCELLED"):
        return "CANCELLED"
    if v in ("TERM", "TERMINATED"):
        return "TERMINATED"
    if v in ("PEND", "PENDING"):
        return "PENDING"

    return v


def normalize_insurance(value):
    if value is None or pd.isna(value):
        return None

    v = str(value).strip().upper()

    if "HEALTH" in v:
        return "HEALTH"
    if "DENTAL" in v:
        return "DENTAL"

    return v


def safe_text(root, names):
    wanted = {x.lower() for x in names}

    for elem in root.iter():
        tag = elem.tag.split("}")[-1].lower()
        if tag in wanted and elem.text:
            return elem.text.strip()

    return None


def safe_month(value):
    return str(value).zfill(2)


# =====================================================
# XML PARSER
# =====================================================

def parse_xml_file(file_path, issuer, year, month):
    try:
        root = ET.parse(file_path).getroot()

        policy_id = safe_text(root, [
            "exchgAssignedPolicyID",
            "healthCoveragePolicyID",
            "Exchange_Assigned_Policy_ID",
            "policy_id",
            "policyId"
        ])

        member_id = safe_text(root, [
            "exchgIndivIdentifier",
            "Exchange_Assigned_Member_ID",
            "member_id",
            "memberId",
            "enrollee_id"
        ])

        subscriber_id = safe_text(root, [
            "exchgSubscriberIdentifier",
            "Exchange_Assigned_Subscriber_ID",
            "subscriber_id",
            "subscriberId"
        ])

        insurance_type = safe_text(root, [
            "Insurance_Type",
            "planCoverageDescription",
            "insurance_type",
            "insurance_type_description"
        ])

        raw_status = safe_text(root, [
            "actionCode_desc",
            "event_type_code_desc",
            "enrolleeStatus",
            "enrollment_status_description",
            "enrollee_status_description",
            "status"
        ])

        benefit_start = safe_text(root, [
            "benefitEffectiveBeginDate",
            "memberEligibilityBeginDate",
            "benefit_effective_date"
        ])

        benefit_end = safe_text(root, [
            "benefitEffectiveEndDate",
            "memberEligibilityEndDate",
            "benefit_end_date"
        ])

        file_date = safe_text(root, [
            "GAA_834_File_Date",
            "GS04_date",
            "ISA09_interchange_date"
        ])

        return {
            "issuer": str(issuer),
            "xml_year": str(year),
            "xml_month": safe_month(month),
            "file_name": os.path.basename(file_path),
            "file_path": file_path,
            "file_date": file_date,
            "policy_id": str(policy_id).strip() if policy_id else None,
            "member_id": str(member_id).strip() if member_id else None,
            "subscriber_id": str(subscriber_id).strip() if subscriber_id else None,
            "insurance_type": normalize_insurance(insurance_type),
            "xml_raw_status": raw_status,
            "xml_status": normalize_status(raw_status),
            "benefit_start": benefit_start,
            "benefit_end": benefit_end,
            "parse_error": None
        }

    except Exception as e:
        return {
            "issuer": str(issuer),
            "xml_year": str(year),
            "xml_month": safe_month(month),
            "file_name": os.path.basename(file_path),
            "file_path": file_path,
            "file_date": None,
            "policy_id": None,
            "member_id": None,
            "subscriber_id": None,
            "insurance_type": None,
            "xml_raw_status": None,
            "xml_status": None,
            "benefit_start": None,
            "benefit_end": None,
            "parse_error": str(e)
        }


def load_xml_snapshot():
    rows = []

    for issuer in os.listdir(ASSETS_DIR):
        issuer_path = os.path.join(ASSETS_DIR, issuer)
        if not os.path.isdir(issuer_path):
            continue

        for year in os.listdir(issuer_path):
            year_path = os.path.join(issuer_path, year)
            if not os.path.isdir(year_path):
                continue

            for month in os.listdir(year_path):
                month_path = os.path.join(year_path, month)
                if not os.path.isdir(month_path):
                    continue

                ym = f"{year}-{safe_month(month)}"
                if ym < START_YEAR_MONTH or ym > END_YEAR_MONTH:
                    continue

                xml_files = glob.glob(os.path.join(month_path, "**", "*.xml"), recursive=True)

                for file_path in xml_files:
                    rows.append(parse_xml_file(file_path, issuer, year, month))

    df = pd.DataFrame(rows)

    if df.empty:
        return df

    df = df.dropna(subset=["issuer", "policy_id", "member_id", "insurance_type"])

    df["join_key"] = (
        df["issuer"].astype(str)
        + "|"
        + df["policy_id"].astype(str)
        + "|"
        + df["member_id"].astype(str)
        + "|"
        + df["insurance_type"].astype(str)
    )

    df["event_order"] = (
        df["xml_year"].astype(str)
        + df["xml_month"].astype(str)
        + "|"
        + df["file_name"].astype(str)
    )

    latest = (
        df.sort_values(["join_key", "event_order"])
        .groupby("join_key", as_index=False)
        .tail(1)
    )

    return latest


# =====================================================
# AZURE FINAL SNAPSHOT
# =====================================================

def load_azure_snapshot(conn):
    sql = """
    SELECT
        CAST(hios_issuer_id AS varchar(20)) AS issuer,
        CAST(coverage_year AS varchar(10)) AS azure_year,
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

    df = pd.read_sql(sql, conn)

    df["insurance_type"] = df["insurance_type"].apply(normalize_insurance)
    df["azure_status"] = df["enrollee_status_description"].apply(normalize_status)

    df["join_key"] = (
        df["issuer"].astype(str)
        + "|"
        + df["policy_id"].astype(str)
        + "|"
        + df["member_id"].astype(str)
        + "|"
        + df["insurance_type"].astype(str)
    )

    return df.drop_duplicates(subset=["join_key"])


# =====================================================
# COMPARISON
# =====================================================

def compare_snapshots(xml_df, azure_df):
    comparison = xml_df.merge(
        azure_df,
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

    comparison["reconciliation_result"] = comparison.apply(result, axis=1)

    return comparison


def build_summaries(comparison):
    final_summary = (
        comparison.groupby("reconciliation_result")
        .size()
        .reset_index(name="rows")
        .sort_values("rows", ascending=False)
    )

    comparison["issuer_final"] = comparison["issuer_xml"].fillna(comparison["issuer_azure"])

    issuer_summary = (
        comparison.groupby(["issuer_final", "reconciliation_result"])
        .size()
        .reset_index(name="rows")
        .sort_values(["issuer_final", "rows"], ascending=[True, False])
    )

    return final_summary, issuer_summary


# =====================================================
# RUNNER
# =====================================================

def runner():
    print("Connecting to Azure...")
    conn = get_connection()

    print("Reading XML lifecycle snapshot...")
    xml_latest = load_xml_snapshot()
    print(f"XML latest rows: {len(xml_latest)}")

    print("Reading Azure final snapshot...")
    azure_latest = load_azure_snapshot(conn)
    print(f"Azure latest rows: {len(azure_latest)}")

    print("Comparing XML vs Azure...")
    comparison = compare_snapshots(xml_latest, azure_latest)

    final_summary, issuer_summary = build_summaries(comparison)

    print("Writing Excel output...")
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        final_summary.to_excel(writer, sheet_name="Final_Result_Summary", index=False)
        issuer_summary.to_excel(writer, sheet_name="Issuer_Result_Summary", index=False)
        xml_latest.to_excel(writer, sheet_name="XML_Latest_Snapshot", index=False)
        azure_latest.to_excel(writer, sheet_name="Azure_Final_Snapshot", index=False)
        comparison.to_excel(writer, sheet_name="Detailed_Comparison", index=False)

    print("DONE")
    print(f"Output file: {OUTPUT_FILE}")
    print(final_summary)


if __name__ == "__main__":
    runner()
