# Business Ready Filter Validation

**Issuer / year:** 15105 / 2026
**Reporting year:** 2026
**Generated:** 2026-06-25T20:33:59+00:00

## Raw filter (validated)

- Raw before: (see FILTER_SUMMARY)
- Raw filtered row count in export: 11730
- Raw prior-year excluded (from FILTER_SUMMARY): 1118

## Step 1 — BUSINESS_READY_FILTERED column inventory

See `business_ready_column_inventory.xlsx` sheet `Column_Inventory`.

Key finding:

- `benefit_effective_date` **not exported** in BUSINESS_READY_FILTERED
- `selected_transaction_date` present — non-null: 12763

## Step 2 — Date used for Business Ready

Priority (from `business_ready_exports._selected_transaction_date`):
1. member_maint_effective_date
2. benefit_effective_date
3. file_event_date
4. event_date

Distribution in business-ready records (lifecycle join):

- `member_maint_effective_date`: 12763

Full per-record trace: `business_ready_column_inventory.xlsx` sheet `Date_Trace`.

## Step 3 — Prior-year candidates

- Would filter using **benefit_effective_date** (lifecycle join): **1073**
- Would filter using **selected_transaction_date**: **0**

Full candidate list: `business_ready_prior_year_candidates.xlsx`

## Step 4 — Pipeline stage analysis (benefit_effective_date)

Prior-year counts by stage (read-only pipeline replay):

| Stage | Rows | Prior-year benefit | Null benefit date |
|-------|-----:|-------------------:|------------------:|
| 1_raw_xml | 12848 | 1118 | 0 |
| 2_canonical (business month applied) | 12848 | 1118 | 0 |
| 3_after_dedupe (_dedupe_transactions) | 12837 | 1109 | 0 |
| 4_latest_state_per_business_month | 12756 | 1068 | 0 |
| 5_business_transaction_collapse → lifecycle_input | 12756 | 1068 | 0 |
| 6_business_ready_export (lifecycle-joined benefit dates) | 12763 | 1073 | 0 |

**First stage where prior-year count reaches zero:** 6_business_ready_export (lifecycle-joined benefit dates)

## Step 5 — Method A vs Method B comparison

| Method | Before | Excluded | After |
|--------|-------:|---------:|------:|
| A: benefit_effective_date (from lifecycle join) | 12763 | 1073 | 11690 |
| B: selected_transaction_date (export column) | 12763 | 0 | 12763 |



---

# Business Ready Filter — Engineering Conclusion

**Generated:** 2026-06-25T20:33:59+00:00
**Reporting year:** 2026

## Column evidence (BUSINESS_READY_FILTERED export)

- `benefit_effective_date` in export: **NO**
- `selected_transaction_date` in export: **YES**

## Questions

### 1. Is Business Ready already free of prior-year benefit records?

**NO**

- Prior-year candidates (Method A — benefit_effective_date via lifecycle join): **1073**
- Prior-year candidates (Method B — selected_transaction_date): **0**
- Prior-year count at business_ready pipeline stage (benefit_effective_date): **1073**

### 2. If YES — which pipeline stage removed them?

N/A — prior-year records still present or date column missing in export

### 3. If NO — how many remain?

**1073** (max of Method A, Method B, pipeline-stage count)

### 4. Should Business Ready filtering still exist?

**YES** — prior-year benefit effective records remain in business-ready input when judged
by `benefit_effective_date`. Filter on lifecycle-joined benefit dates, not only
`selected_transaction_date`.
