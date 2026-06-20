import os
import glob
import pandas as pd
import pyodbc
import xml.etree.ElementTree as ET
from urllib.parse import quote_plus


# =========================
# CONFIG
# =========================

ASSETS_DIR = r"C:\Users\SelmaKazanci\Downloads\gaaccess-develop6\gaaccess-develop6\assets"
OUTPUT_FILE = "final_xml_vs_azure_lifecycle_comparison.xlsx"

SERVER = "your_server"
DATABASE = "your_database"
USERNAME = "your_username"
PASSWORD = "your_password"
DRIVER = "{ODBC Driver 17 for SQL Server}"

START_YEAR_MONTH = "2025-10"
END_YEAR_MONTH = "2026-05"


# =========================
# DB CONNECTION
# =========================

conn = pyodbc.connect(
    f"DRIVER={DRIVER};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    "TrustServerCertificate=yes;"
)


# =========================
# HELPERS
# =========================

def normalize_status(value):
    if pd.isna(value):
        return None

    v = str(value).strip().upper()

    if v in ["CONFIRM", "CONFIRMED", "ENROLLED", "ENROLL"]:
        return "ENROLLED"
    if v in ["CANCEL", "CANCELLED", "CANCELED"]:
        return "CANCELLED"
    if v in ["TERM", "TERMINATED"]:
        return "TERMINATED"
    if v in ["PEND", "PENDING"]:
        return "PENDING"

    return v


def normalize_insurance(value):
    if pd.isna(value):
        return None

    v = str(value).strip().upper()

    if "HEALTH" in v:
        return "HEALTH"
    if "DENTAL" in v:
        return "DENTAL"

    return v


def safe_text(root, names):
    for elem in root.iter():
        tag = elem.tag.split("}")[-1]
        if tag in names and elem.text:
            return elem.text.strip()
    return None


def parse_xml_file(file_path, issuer, year, month):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        policy_id = safe_text(root, [
            "exchgAssignedPolicyID",
            "healthCoveragePolicyID",
            "policy_id",
            "policyId",
        ])

        member_id = safe_text(root, [
            "exchgIndivIdentifier",
            "member_id",
            "memberId",
            "enrollee_id",
        ])

        subscriber_id = safe_text(root, [
            "exchgSubscriberIdentifier",
            "subscriber_id",
            "subscriberId",
        ])

        insurance_type = safe_text(root, [
            "Insurance_Type",
            "planCoverageDescription",
            "insurance_type",
        ])

        raw_status = safe_text(root, [
            "actionCode_desc",
            "event_type_code_desc",
            "enrolleeStatus",
            "status",
        ])

        benefit_start = safe_text(root, [
            "benefitEffectiveBeginDate",
            "memberEligibilityBeginDate",
        ])

        benefit_end = safe_text(root, [
            "benefitEffectiveEndDate",
            "memberEligibilityEndDate",
        ])

        file_date = safe_text(root, [
            "GAA_834_File_Date",
            "GS04_date",
            "ISA09_interchange_date",
        ])

        return {
            "issuer": str(issuer),
            "xml_year": str(year),
            "xml_month": str(month).zfill(2),
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
        }

    except Exception as e:
        return {
            "issuer": str(issuer),
            "xml_year": str(year),
            "xml_month": str(month).zfill(2),
            "file_name": os.path.basename(file_path),
            "file_path": file_path,
            "parse_error": str(e),
        }


# =========================
# READ XML FILES
# =========================

xml_rows = []

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

            ym = f"{year}-{str(month).zfill(2)}"
            if ym < START_YEAR_MONTH or ym > END_YEAR_MONTH:
                continue

            files = glob.glob(os.path.join(month_path, "**", "*.xml"), recursive=True)

            for file_path in files:
                xml_rows.append(parse_xml_file(file_path, issuer, year, month))

xml_df = pd.DataFrame(xml_rows)

xml_df = xml_df.dropna(subset=["issuer", "policy_id", "member_id"])

xml_df["join_key"] = (
    xml_df["issuer"].astype(str)
    + "|"
    + xml_df["policy_id"].astype(str)
    + "|"
    + xml_df["member_id"].astype(str)
    + "|"
    + xml_df["insurance_type"].astype(str)
)

xml_df["event_order"] = (
    xml_df["xml_year"].astype(str)
    + xml_df["xml_month"].astype(str).str.zfill(2)
    + "_"
    + xml_df["file_name"].astype(str)
)

xml_latest = (
    xml_df.sort_values(["join_key", "event_order"])
    .groupby("join_key", as_index=False)
    .tail(1)
)


# =========================
# READ AZURE FINAL SNAPSHOT
# =========================

azure_sql = """
SELECT
    CAST(hios_issuer_id AS varchar(20)) AS issuer,
    CAST(coverage_year AS varchar(10)) AS coverage_year,
    CAST(enrollment_id AS varchar(50)) AS policy_id,
    CAST(enrollee_id AS varchar(50)) AS member_id,
    UPPER(Insurance_Type) AS insurance_type,
    enrollment_status_description,
    enrollee_status_description,
    benefit_effective_date,
    benefit_end_date,
    enrollment_confirmation_date,
    enrollment_create_date,
    enrollment_last_update_date
FROM dbo.Enrollments_PY2026
WHERE coverage_year = 2026
  AND hios_issuer_id IS NOT NULL
  AND enrollment_id IS NOT NULL
  AND enrollee_id IS NOT NULL;
"""

azure_df = pd.read_sql(azure_sql, conn)

azure_df["insurance_type"] = azure_df["insurance_type"].apply(normalize_insurance)
azure_df["azure_status"] = azure_df["enrollee_status_description"].apply(normalize_status)

azure_df["join_key"] = (
    azure_df["issuer"].astype(str)
    + "|"
    + azure_df["policy_id"].astype(str)
    + "|"
    + azure_df["member_id"].astype(str)
    + "|"
    + azure_df["insurance_type"].astype(str)
)

azure_latest = azure_df.drop_duplicates(subset=["join_key"])


# =========================
# COMPARE
# =========================

comparison = xml_latest.merge(
    azure_latest,
    on="join_key",
    how="outer",
    suffixes=("_xml", "_azure"),
    indicator=True
)

def reconciliation_result(row):
    if row["_merge"] == "left_only":
        return "XML_NOT_IN_AZURE"
    if row["_merge"] == "right_only":
        return "AZURE_NOT_IN_XML"

    if row["xml_status"] != row["azure_status"]:
        return "STATUS_DIFF"

    return "MATCH"


comparison["reconciliation_result"] = comparison.apply(reconciliation_result, axis=1)


# =========================
# SUMMARY
# =========================

summary = (
    comparison.groupby("reconciliation_result")
    .size()
    .reset_index(name="rows")
    .sort_values("rows", ascending=False)
)

issuer_summary = (
    comparison.groupby([
        comparison["issuer_xml"].fillna(comparison["issuer_azure"]),
        "reconciliation_result"
    ])
    .size()
    .reset_index(name="rows")
)

issuer_summary.columns = ["issuer", "reconciliation_result", "rows"]


# =========================
# EXPORT
# =========================

with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="Final_Result_Summary", index=False)
    issuer_summary.to_excel(writer, sheet_name="Issuer_Result_Summary", index=False)
    xml_latest.to_excel(writer, sheet_name="XML_Latest_Snapshot", index=False)
    azure_latest.to_excel(writer, sheet_name="Azure_Final_Snapshot", index=False)
    comparison.to_excel(writer, sheet_name="Detailed_Comparison", index=False)

print("DONE")
print(f"Output generated: {OUTPUT_FILE}")
print(summary)
