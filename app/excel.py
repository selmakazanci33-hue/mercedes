import os
import re
import glob
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


# =========================
# CONFIG
# =========================

load_dotenv()

AZURE_CONN_STR = os.getenv("AZURE_SQL_CONNECTION_STRING")

XML_ROOT_DIR = r"C:\Users\SelmaKazanci\Downloads\gaaccess-develop6\gaaccess-develop6\xml_files"
OUTPUT_FILE = r"C:\Users\SelmaKazanci\Downloads\db_xml_834_comparison.xlsx"

START_DATE = "2026-01-01"
END_DATE = "2026-06-01"   # Jan-May için June 1 exclusive

DB_TABLE = "dbo.[834_Inbound_test]"


# =========================
# HELPERS
# =========================

def normalize_status(value):
    if pd.isna(value):
        return "UNKNOWN"

    v = str(value).strip().upper()

    if v in ["021", "CONFIRM", "CONFIRMED", "ENROLLED", "ACTIVE"]:
        return "CONFIRM"

    if v in ["024", "TERM", "TERMINATED", "TERMINATE"]:
        return "TERM"

    if v in ["001", "CANCEL", "CANCELLED", "CANCELED"]:
        return "CANCEL"

    return v


def normalize_insurance_type(value):
    if pd.isna(value):
        return "UNKNOWN"

    v = str(value).strip().upper()

    if "DENTAL" in v:
        return "Dental"
    if "HEALTH" in v or "QHP" in v:
        return "Health"

    return str(value).strip()


def month2(value):
    return str(value).zfill(2)


# =========================
# DB EXTRACT
# =========================

def get_engine():
    if not AZURE_CONN_STR:
        raise ValueError("AZURE_SQL_CONNECTION_STRING is missing in .env")

    return create_engine(AZURE_CONN_STR, fast_executemany=True)


def extract_db_raw(engine):
    sql = f"""
        SELECT
            Coverage_Year AS year,
            GAA_HIOS_ID AS issuer,
            TRY_CONVERT(date, GAA_834_File_Date) AS file_date,
            GAA_834_File_Name AS file_name,

            Insurance_Type AS insurance_type,

            actionCode AS action_code,
            actionCode_desc AS action_desc,

            event_type_code AS event_type_code,
            event_type_code_desc AS event_type_desc,
            event_reason_code AS event_reason_code,
            event_reason_code_desc AS event_reason_desc,

            exchgAssignedPolicyID AS policy_id,
            exchgIndivIdentifier AS member_id,
            exchgSubscriberIdentifier AS subscriber_id,

            householdOrEmployeeCaseID AS household_id,
            healthCoveragePolicyID AS health_policy_id,

            enrolleeStatus AS enrollee_status,
            enrolleeStatusDate AS enrollee_status_date,

            subscriberFlag AS subscriber_flag,

            memberFirstName AS first_name,
            memberLastName AS last_name,
            memberBirthDate AS birth_date,

            benefitEffectiveBeginDate AS benefit_begin_date,
            benefitEffectiveEndDate AS benefit_end_date,
            memberEligibilityBeginDate AS eligibility_begin_date,
            memberEligibilityEndDate AS eligibility_end_date,
            memberMaintEffectiveDate AS maint_effective_date,

            healthCoveragePremiumAmt AS premium_amt,
            totalIndivResponsibilityAmt AS responsibility_amt,
            aptcAmt AS aptc_amt,
            csrAmt AS csr_amt,
            totalPremiumAmt AS total_premium_amt

        FROM {DB_TABLE}
        WHERE TRY_CONVERT(date, GAA_834_File_Date) >= :start_date
          AND TRY_CONVERT(date, GAA_834_File_Date) < :end_date
    """

    with engine.connect() as conn:
        df = pd.read_sql_query(
            text(sql),
            conn,
            params={"start_date": START_DATE, "end_date": END_DATE}
        )

    df["source"] = "AZURE_DB"
    df["month"] = pd.to_datetime(df["file_date"], errors="coerce").dt.month.astype("Int64").astype(str).str.zfill(2)
    df["status"] = df["action_desc"].combine_first(df["enrollee_status"]).apply(normalize_status)
    df["insurance_type"] = df["insurance_type"].apply(normalize_insurance_type)

    return df


def summarize_db(df):
    return (
        df.groupby(["issuer", "year", "month", "insurance_type", "status"], dropna=False)
        .agg(
            db_raw_row_count=("policy_id", "size"),
            db_policy_count=("policy_id", pd.Series.nunique),
            db_member_count=("member_id", pd.Series.nunique),
            db_subscriber_count=("subscriber_id", pd.Series.nunique),
            db_household_count=("household_id", pd.Series.nunique),
        )
        .reset_index()
    )


# =========================
# XML EXTRACT
# =========================

def clean_xml_text(x):
    if x is None:
        return None
    return str(x).strip()


def find_text_anywhere(root, possible_names):
    possible_names_lower = [x.lower() for x in possible_names]

    for elem in root.iter():
        tag = elem.tag.split("}")[-1].lower()
        if tag in possible_names_lower:
            return clean_xml_text(elem.text)

    return None


def parse_one_xml(file_path):
    file_path = Path(file_path)

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception:
        return []

    file_name = file_path.name

    issuer = find_text_anywhere(
        root,
        [
            "GAA_HIOS_ID",
            "hiosIssuerId",
            "hios_issuer_id",
            "issuerId",
            "HIOSID",
            "issuer"
        ]
    )

    coverage_year = find_text_anywhere(
        root,
        [
            "Coverage_Year",
            "coverageYear",
            "coverage_year"
        ]
    )

    insurance_type = find_text_anywhere(
        root,
        [
            "Insurance_Type",
            "insuranceType",
            "insurance_type",
            "planCoverageDescription"
        ]
    )

    file_date_match = re.search(r"(20\d{2})[-_]?([01]\d)[-_]?([0-3]\d)", file_name)
    file_date = None
    month = None

    if file_date_match:
        y, m, d = file_date_match.groups()
        file_date = f"{y}-{m}-{d}"
        month = m

    records = []

    for elem in root.iter():
        tag = elem.tag.split("}")[-1].lower()

        # Broad member/enrollee/policy-ish nodes
        if tag in [
            "member",
            "enrollee",
            "subscriber",
            "policy",
            "coverage",
            "loop2000",
            "loop2300"
        ]:
            policy_id = find_text_anywhere(
                elem,
                [
                    "exchgAssignedPolicyID",
                    "policyId",
                    "policy_id",
                    "healthCoveragePolicyID"
                ]
            )

            member_id = find_text_anywhere(
                elem,
                [
                    "exchgIndivIdentifier",
                    "memberId",
                    "member_id",
                    "enrolleeId"
                ]
            )

            subscriber_id = find_text_anywhere(
                elem,
                [
                    "exchgSubscriberIdentifier",
                    "subscriberId",
                    "subscriber_id"
                ]
            )

            household_id = find_text_anywhere(
                elem,
                [
                    "householdOrEmployeeCaseID",
                    "householdId",
                    "household_id"
                ]
            )

            status = find_text_anywhere(
                elem,
                [
                    "actionCode_desc",
                    "actionCode",
                    "enrolleeStatus",
                    "status",
                    "maintenanceTypeCode"
                ]
            )

            if policy_id or member_id or subscriber_id or status:
                records.append(
                    {
                        "source": "XML",
                        "file_name": file_name,
                        "file_path": str(file_path),
                        "file_date": file_date,
                        "issuer": issuer,
                        "year": coverage_year,
                        "month": month,
                        "insurance_type": normalize_insurance_type(insurance_type),
                        "status": normalize_status(status),
                        "policy_id": policy_id,
                        "member_id": member_id,
                        "subscriber_id": subscriber_id,
                        "household_id": household_id,
                    }
                )

    # fallback: if no child records found, create file-level row
    if not records:
        records.append(
            {
                "source": "XML",
                "file_name": file_name,
                "file_path": str(file_path),
                "file_date": file_date,
                "issuer": issuer,
                "year": coverage_year,
                "month": month,
                "insurance_type": normalize_insurance_type(insurance_type),
                "status": "UNKNOWN",
                "policy_id": None,
                "member_id": None,
                "subscriber_id": None,
                "household_id": None,
            }
        )

    return records


def extract_xml_raw():
    patterns = [
        "**/*.xml",
        "**/*.XML",
    ]

    files = []
    for pattern in patterns:
        files.extend(glob.glob(str(Path(XML_ROOT_DIR) / pattern), recursive=True))

    all_rows = []

    for file in files:
        all_rows.extend(parse_one_xml(file))

    df = pd.DataFrame(all_rows)

    if df.empty:
        return pd.DataFrame(
            columns=[
                "source", "file_name", "file_path", "file_date", "issuer",
                "year", "month", "insurance_type", "status",
                "policy_id", "member_id", "subscriber_id", "household_id"
            ]
        )

    df["issuer"] = df["issuer"].astype(str).str.extract(r"(\d+)")[0]
    df["year"] = df["year"].astype(str).str.extract(r"(20\d{2})")[0]
    df["month"] = df["month"].apply(lambda x: month2(x) if pd.notna(x) else x)

    return df


def summarize_xml(df):
    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby(["issuer", "year", "month", "insurance_type", "status"], dropna=False)
        .agg(
            xml_raw_row_count=("policy_id", "size"),
            xml_policy_count=("policy_id", pd.Series.nunique),
            xml_member_count=("member_id", pd.Series.nunique),
            xml_subscriber_count=("subscriber_id", pd.Series.nunique),
            xml_household_count=("household_id", pd.Series.nunique),
        )
        .reset_index()
    )


# =========================
# COMPARISON
# =========================

def compare_summaries(db_summary, xml_summary):
    keys = ["issuer", "year", "month", "insurance_type", "status"]

    comparison = db_summary.merge(
        xml_summary,
        on=keys,
        how="outer"
    )

    count_cols = [
        "db_raw_row_count",
        "db_policy_count",
        "db_member_count",
        "db_subscriber_count",
        "db_household_count",
        "xml_raw_row_count",
        "xml_policy_count",
        "xml_member_count",
        "xml_subscriber_count",
        "xml_household_count",
    ]

    for col in count_cols:
        if col not in comparison.columns:
            comparison[col] = 0
        comparison[col] = comparison[col].fillna(0).astype(int)

    comparison["raw_row_diff"] = comparison["db_raw_row_count"] - comparison["xml_raw_row_count"]
    comparison["policy_diff"] = comparison["db_policy_count"] - comparison["xml_policy_count"]
    comparison["member_diff"] = comparison["db_member_count"] - comparison["xml_member_count"]
    comparison["subscriber_diff"] = comparison["db_subscriber_count"] - comparison["xml_subscriber_count"]
    comparison["household_diff"] = comparison["db_household_count"] - comparison["xml_household_count"]

    comparison["comparison_status"] = comparison.apply(
        lambda r: "MATCH"
        if r["raw_row_diff"] == 0
        and r["policy_diff"] == 0
        and r["member_diff"] == 0
        and r["subscriber_diff"] == 0
        and r["household_diff"] == 0
        else "MISMATCH",
        axis=1
    )

    return comparison.sort_values(keys)


def issuer_coverage(db_summary, xml_summary):
    db_issuers = set(db_summary["issuer"].dropna().astype(str))
    xml_issuers = set(xml_summary["issuer"].dropna().astype(str))

    rows = []

    for issuer in sorted(db_issuers | xml_issuers):
        rows.append(
            {
                "issuer": issuer,
                "in_db": issuer in db_issuers,
                "in_xml": issuer in xml_issuers,
                "coverage_status": (
                    "BOTH"
                    if issuer in db_issuers and issuer in xml_issuers
                    else "DB_ONLY"
                    if issuer in db_issuers
                    else "XML_ONLY"
                )
            }
        )

    return pd.DataFrame(rows)


# =========================
# EXPORT
# =========================

def write_excel(db_raw, xml_raw, db_summary, xml_summary, comparison, issuer_cov):
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        comparison.to_excel(writer, sheet_name="DB_vs_XML_Comparison", index=False)
        db_summary.to_excel(writer, sheet_name="Azure_Summary", index=False)
        xml_summary.to_excel(writer, sheet_name="XML_Summary", index=False)
        issuer_cov.to_excel(writer, sheet_name="Issuer_Coverage", index=False)

        db_raw.head(100000).to_excel(writer, sheet_name="Azure_Raw_Sample", index=False)
        xml_raw.head(100000).to_excel(writer, sheet_name="XML_Raw_Sample", index=False)

    print(f"Excel created successfully: {OUTPUT_FILE}")


# =========================
# MAIN
# =========================

def main():
    print("Connecting Azure...")
    engine = get_engine()

    print("Extracting Azure DB 834 data...")
    db_raw = extract_db_raw(engine)
    print(f"DB raw rows: {len(db_raw)}")

    print("Summarizing Azure DB...")
    db_summary = summarize_db(db_raw)
    print(f"DB summary rows: {len(db_summary)}")

    print("Extracting XML data...")
    xml_raw = extract_xml_raw()
    print(f"XML raw rows: {len(xml_raw)}")

    print("Summarizing XML...")
    xml_summary = summarize_xml(xml_raw)
    print(f"XML summary rows: {len(xml_summary)}")

    print("Comparing DB vs XML...")
    comparison = compare_summaries(db_summary, xml_summary)

    print("Checking issuer coverage...")
    issuer_cov = issuer_coverage(db_summary, xml_summary)

    print("Writing Excel...")
    write_excel(db_raw, xml_raw, db_summary, xml_summary, comparison, issuer_cov)

    print("Done.")


if __name__ == "__main__":
    main()
