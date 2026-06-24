# Cleaned Export Definition — Investigation

**Issuer / year:** 15105 / 2026
**Generated:** 2026-06-24T03:59:15+00:00

## Executive answers

### 1. What exactly is exported as "cleaned"?

`cleaned_all_months.xlsx` exports **every row from `result.canonical`** after
`apply_business_month_basis()` — the same record-level dataset the business pipeline
uses before deduplication, collapse, and Model H aggregation. Export adds metadata
and boolean flags (duplicate, maintenance-only, superseded, latest-state, Model H
inclusion) but **does not remove rows**.

### 2. Which option?

| Option | Matches export? |
|--------|-----------------|
| **A) Normalized canonical** | **YES** — primary answer |
| B) Business-cleaned (rows removed) | NO — flags only, all rows kept |
| C) Latest-state | NO — separate flag column |
| D) Model H input | NO — smaller subset; see stage 9 |

Yearly raw count == yearly cleaned count because both are **full record-level**
exports filtered to the same source year with **no row removal**.

### 3. When do record counts actually decrease?

Counts first decrease at **stage 7 (dedupe)**. Further decreases at latest-state
selection, business-transaction collapse, and Model H aggregation (stages 8–10).

## Stage-by-stage row counts

| Stage | Row Count | Rows Removed? | Description |
|-------|-----------|---------------|-------------|
| 1. Raw Parsed XML | 12,848 | No | Direct parser output from source_data XML files. |
| 2. Canonical (build_canonical_xml_records) | 12,848 | No | Normalized field names, IDs, status, dates — 1:1 with raw rows. |
| 3. Enriched Month Bases (enrich_month_bases) | 12,848 | No | Adds coverage/file/benefit/maint year-month columns; year/month still source fol |
| 4. Pre-Business Canonical (partition-filtered) | 12,848 | Only if partition filter excludes folder | Canonical + month bases, filtered to issuer/year/month partitions. |
| 5. Business Canonical (apply_business_month_basis) | 12,848 | No | year/month OVERWRITTEN for Model H grouping; month_basis_used recorded. |
| 6. Cleanup Diagnostics (flags only) | 12,848 | No — flags only | Duplicate, maintenance-only, superseded classifications. |
| 7. Deduped Transactions (_dedupe_transactions) | 12,837 | Yes | Removes exact duplicate XML transactions (same PK + status + dates). |
| 8. Latest State per Business Month | 12,756 | Yes | Latest transaction per PK within each business year/month after dedupe. |
| 9. Model H Input (lifecycle_input after collapse) | 12,756 | Yes (collapse + maintenance-only removal) | Business-transaction-collapsed rows fed to Model H aggregation. |
| 10. Model H Monthly Summary (aggregated) | 0 | Yes (aggregation) | Distinct enrollment counts by status/month — NOT record-level. |

## Detailed stage table

| Stage Name | Row Count | Description | Purpose | Columns Added | Columns Removed | Rows Removed | Notes |
|------------|-----------|-------------|---------|---------------|-----------------|--------------|-------|
| 1. Raw Parsed XML | 12,848 | Direct parser output from source_data XML files. | Source of truth for inbound 834 transaction events. | Parser fields (policy_id, member_id, dates, codes, file_name, …) | None | No | Full-data export RAW_ALL_MONTHS sheet. |
| 2. Canonical (build_canonical_xml_records) | 12,848 | Normalized field names, IDs, status, dates — 1:1 with raw rows. | Common schema for reconciliation and lifecycle. | normalized_status, action_code, _record_key, source_file | None (raw columns not carried forward) | No | Row count should equal raw unless parser drops empty files. |
| 3. Enriched Month Bases (enrich_month_bases) | 12,848 | Adds coverage/file/benefit/maint year-month columns; year/month still source folder. | Candidate month bases for business-month selection. | coverage_year_month, file_event_year_month, benefit_effective_year_month, member_maint_year_month | None | No | Partition filter may drop rows outside discovered partitions. |
| 4. Pre-Business Canonical (partition-filtered) | 12,848 | Canonical + month bases, filtered to issuer/year/month partitions. | Input to apply_business_month_basis. | snapshot_source | None | Only if partition filter excludes folder | Partitions: 6 |
| 5. Business Canonical (apply_business_month_basis) | 12,848 | year/month OVERWRITTEN for Model H grouping; month_basis_used recorded. | Assign business load month per production priority (file → maint → benefit → coverage). | month_basis_used, insurance_type, status | None | No | THIS is what full-data export calls CLEANED_ALL_MONTHS (answer: A — normalized canonical with business month). |
| 6. Cleanup Diagnostics (flags only) | 12,848 | Duplicate, maintenance-only, superseded classifications. | Explain cleanup; rows are flagged, not removed from canonical. | cleanup_reason (on diagnostic subsets) | None | No — flags only | dup=11, maint=12848, superseded=364 |
| 7. Deduped Transactions (_dedupe_transactions) | 12,837 | Removes exact duplicate XML transactions (same PK + status + dates). | Collapse redundant events before lifecycle / Model H. | None | None | Yes | Removed 11 rows in 2026 |
| 8. Latest State per Business Month | 12,756 | Latest transaction per PK within each business year/month after dedupe. | Representative row per enrollment per business month. | None | None | Yes |  |
| 9. Model H Input (lifecycle_input after collapse) | 12,756 | Business-transaction-collapsed rows fed to Model H aggregation. | Final record-level input before enrollment counting. | Collapse audit fields (when applied) | None | Yes (collapse + maintenance-only removal) |  |
| 10. Model H Monthly Summary (aggregated) | 0 | Distinct enrollment counts by status/month — NOT record-level. | Chandra-like dashboard output. | Enrollment_Count, Enrollee_Count, … | Record detail | Yes (aggregation) | 18 summary row(s); enrollment sum=0 |

## Production impact

This investigation does **not** recommend changing production logic.

