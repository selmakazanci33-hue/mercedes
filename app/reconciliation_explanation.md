# Reconciliation Explanation

**Issuer:** 15105

## Why XML has more records than Azure

- XML raw rows: **40,509**
- Azure raw rows: **12,788**

XML 834 files contain **multiple transaction events** per member/policy (enrollments, changes, cancellations, maintenance). Each event becomes a row. Azure `dbo.834_Inbound_test` stores **loaded/processed events** — typically one row per inbound file transaction that reached the warehouse, not every intermediate XML maintenance line.

After lifecycle collapse, XML still exceeds Azure when:
- XML includes maintenance-only or superseded events
- XML source_data covers more files/months than Azure has loaded rows for
- Month basis differs (coverage vs GAA_834_File_Date)

## Why Azure can have records not found in XML

Top Azure-only reason buckets:
- **POLICY_EXISTS_XML_MEMBER_DIFF**: 1,241 records
- **POSSIBLE_ID_TRANSFORMATION**: 34 records

Common causes:
- **Policy exists, member ID differs** — join mapping may use subscriber vs individual ID
- **Member exists, policy differs** — policy reassignment or alternate policy column
- **Different month** — Azure file date month ≠ XML maintenance/coverage month
- **Azure-only source** — row in warehouse with no matching XML in current source_data partition
- **Not in lifecycle snapshot** — present in XML raw but filtered by snapshot collapse

## XML-only records (not in Azure)

- **MAINTENANCE_ONLY_EVENT**: 10,787 records
- **DUPLICATE_XML_TRANSACTION**: 3,009 records
- **POSSIBLE_NOT_LOADED_TO_AZURE**: 1,025 records

## Business aggregation model comparison

Models tested (A–H) reverse-engineer how Chandra/dashboard counts may aggregate:

- **Model A** (Raw event level): match rate 32.1%, XML out 40,509, Azure out 12,788
- **Model B** (Latest per policy/member/insurance/month): match rate 34.7%, XML out 32,956, Azure out 12,699
- **Model C** (Latest per policy/member/insurance (no month)): match rate 43.3%, XML out 25,959, Azure out 12,492
- **Model D** (Active/enrolled current-state only): match rate 19.2%, XML out 17,345, Azure out 4,681
- **Model E** (Exclude maintenance-only/no-op): match rate 0.0%, XML out 0, Azure out 12,788
- **Model F** (Exclude duplicate same status/effective): match rate 35.2%, XML out 33,083, Azure out 12,788
- **Model G** (Collapse CANCEL/TERM into final status): match rate 43.3%, XML out 25,959, Azure out 12,492
- **Model H** (Chandra-like dashboard counts (enrollment/enrollee/subscriber by month/status)): match rate 46.2%, XML out 24, Azure out 20

**Best model:** H — Chandra-like dashboard counts (enrollment/enrollee/subscriber by month/status)
**Best overall match rate:** 46.23%

**Selected lifecycle month basis:** join_file_event_month
**Lifecycle snapshot match rate:** 34.66%
**Status match (on matched):** 99.99%

## Root cause assessment

- **ID mapping and status mapping are reliable** (~99% status match on matched records).
- **Date/month basis** is a major factor — Azure uses GAA_834_File_Date month; XML may use coverage or maintenance month.
- **Business aggregation** — XML event grain ≠ Azure load grain; use lifecycle snapshot or Model C/G rather than raw event match.

## Recommended next actions

1. Review ID overlap matrix — subscriber vs individual identifier mapping.
1. Use **Model C or G** (latest state without month) for business accuracy reporting.
2. Treat raw event match rate as diagnostic only.
3. Review `month_basis_diff.csv` for month-only mismatches.
4. Review `azure_not_in_xml_reason_detail.csv` for Azure-only row samples.
