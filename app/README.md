# Business Review Package

**Generated:** 2026-06-24T05:44:02+00:00

## What is included

This folder collects engineering validation exports for business review:

- **raw/** — parsed XML transactions (no cleanup)
- **canonical/** — normalized canonical records (1:1 with raw, business month applied)
- **business_ready/** — Model H input records (post dedupe, latest-state, collapse)
- **reports/** — Chandra-like enrollment summaries and rollups
- **investigations/** — read-only engineering investigations

## RAW vs CANONICAL vs BUSINESS READY vs REPORTS

| Layer | Grain | Row removal? |
|-------|-------|--------------|
| RAW | 1 XML transaction | No |
| CANONICAL | 1 normalized transaction | No (flags only) |
| BUSINESS READY | 1 selected business record | Yes (collapse) |
| REPORTS | Aggregated enrollments | Yes (Model H) |

Yearly **raw** and **canonical** counts often match because both are full record-level
exports with no rows removed. **Business ready** counts are lower.

Monthly counts may differ when **source folder month** ≠ **business month**
(see investigations/month_reassignment_matrix.xlsx).

## Trace a dashboard number

1. Open `reports/monthly/<month>/enrollment_summary.xlsx` or `issuer_year_rollup.xlsx`
2. Note issuer, year, month, insurance type, status
3. Open `business_ready/business_ready_summary.xlsx` — match `dashboard_group_key`
4. Filter `business_ready/business_ready_all_months.xlsx` on that key
5. Use `raw_transaction_keys` and `raw_source_files` to trace back to raw XML

## Validation status

- Parser validated against source_data XML
- Canonical is 1:1 with raw at record level
- Business Ready is post-dedupe / latest-state / business-transaction collapse
- Model H summary is aggregated business output
- Month reassignment is real and documented in investigations/

## Known open item

Chandra may apply additional eligibility/reporting logic not fully represented in XML.

## Data lineage

[Interactive lineage diagram](data_lineage_diagram.html)

## Issuer / year packages

- [15105 / 2026](15105/2026/README.md)

## Not Generated / Not Available

- `15105/2026/investigations/final_engineering_conclusion.md`
- `15105/2026/investigations/final_remaining_gap_analysis.xlsx`
