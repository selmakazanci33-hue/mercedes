# SQL Forensic Root Cause Report

**Generated:** 2026-06-22T07:21:44+00:00
**Issuer partition:** 37001
**Table:** dbo.834_Inbound_test

## Evidence summary

- Total rows in `834_Inbound_test` (unfiltered): **80755**
  - Query: `SELECT COUNT(*) FROM [dbo].[834_Inbound_test]`
- Rows matching issuer `37001` on GAA_HIOS_ID: **0**
  - Query: `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST(GAA_HIOS_ID AS VARCHAR(20)) = '37001'`

## Answers

### 1. Are XML records physically present in Azure?

**No rows for issuer `37001` on GAA_HIOS_ID.** Table has 80755 total rows. Evidence: issuer filter count = 0.

### 2. If not, why not?

**Issuer `37001` not found in any issuer-like column** (or only via non-GAA_HIOS_ID columns). Best matching issuer column: `none`. See `issuer_existence` / `issuer_column_analysis` sheets.

### 3. Are IDs transformed?

**Best policy mapping:** household_or_employee_case_id -> healthCoveragePolicyID: normalized=0, sql_in=0
**Best member mapping:** member_id -> Subscriber_QTYy: normalized=0, sql_in=0
**Best subscriber mapping:** subscriber_id -> Subscriber_QTYy: normalized=0, sql_in=0

### 4. Are issuers transformed?

- `GAA_HIOS_ID`: distinct=3, matches issuer=False, rows=0, samples=43802; 13535; 15105

### 5. Are dates transformed?

**Best aligning Azure date column:** `ratingAreaDate` with 19 overlapping year-month buckets. Azure months: 2025-01; 2025-02; 2025-03; 2025-04; 2025-05; 2025-06; 2025-07; 2025-08; 2025-09; 2025-10; 2025-11; 2025-12. XML months: 2025-01; 2025-02; 2025-03; 2025-04; 2025-05; 2025-06; 2025-07; 2025-08; 2025-09; 2025-10; 2025-11; 2025-12.

### 6. Are we reading the wrong table?

Primary table is `834_Inbound_test` per FAST_MODE (unchanged). Record lookup checked alternate tables: [].

### 7. Are we filtering incorrectly?

Issuer filter on GAA_HIOS_ID returned **0** rows. Issuer found in issuer-like columns: **False**.

### 8. Is Azure missing data?

**Azure has data (80755 rows) but none for issuer `37001` on standard filter.**

### 9. Is XML ahead of Azure?

**19/20** sampled XML records had no Azure match — consistent with XML ahead or ID mismatch. See record_lookup sheet.

### 10. SQL evidence log

Full query log: `C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\outputs\sql_validation\sql_evidence_log.json`

Top queries executed:

- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test]` → **80755** (total rows)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST(GAA_HIOS_ID AS VARCHAR(20)) = :issuer` → **0** (issuer=37001)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([GAA_HIOS_ID] AS VARCHAR(50)) = :v` → **0** (GAA_HIOS_ID variant=37001.0)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([GAA_HIOS_ID] AS VARCHAR(50)) LIKE :pat` → **0** (GAA_HIOS_ID LIKE variant=37001.0)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([GAA_HIOS_ID] AS VARCHAR(50)) = :v` → **0** (GAA_HIOS_ID variant=37001)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([GAA_HIOS_ID] AS VARCHAR(50)) LIKE :pat` → **0** (GAA_HIOS_ID LIKE variant=37001)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([exchgAssignedPolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5, :p6, :p7, :p8, :p9, :p10, :p11, :p12, :p13, :p14, :p15, :p16, :p17, ` → **0** (policy IN match policy_id->exchgAssignedPolicyID)
- `SELECT DISTINCT TOP 20000 CAST([exchgAssignedPolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [exchgAssignedPolicyID] IS NOT NULL` → **20000 distinct values** (azure ids for exchgAssignedPolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([healthCoveragePolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5, :p6, :p7, :p8, :p9, :p10, :p11, :p12, :p13, :p14, :p15, :p16, :p17,` → **0** (policy IN match policy_id->healthCoveragePolicyID)
- `SELECT DISTINCT TOP 20000 CAST([healthCoveragePolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [healthCoveragePolicyID] IS NOT NULL` → **20000 distinct values** (azure ids for healthCoveragePolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([previousExchgAssignedPolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5, :p6, :p7, :p8, :p9, :p10, :p11, :p12, :p13, :p14, :p15, :p16` → **0** (policy IN match policy_id->previousExchgAssignedPolicyID)
- `SELECT DISTINCT TOP 20000 CAST([previousExchgAssignedPolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [previousExchgAssignedPolicyID] IS NOT NULL` → **6375 distinct values** (azure ids for previousExchgAssignedPolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([exchgAssignedPolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5)` → **0** (policy IN match health_coverage_policy_no->exchgAssignedPolicyID)
- `SELECT DISTINCT TOP 20000 CAST([exchgAssignedPolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [exchgAssignedPolicyID] IS NOT NULL` → **20000 distinct values** (azure ids for exchgAssignedPolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([healthCoveragePolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5)` → **0** (policy IN match health_coverage_policy_no->healthCoveragePolicyID)
- `SELECT DISTINCT TOP 20000 CAST([healthCoveragePolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [healthCoveragePolicyID] IS NOT NULL` → **20000 distinct values** (azure ids for healthCoveragePolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([previousExchgAssignedPolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5)` → **0** (policy IN match health_coverage_policy_no->previousExchgAssignedPolicyID)
- `SELECT DISTINCT TOP 20000 CAST([previousExchgAssignedPolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [previousExchgAssignedPolicyID] IS NOT NULL` → **6375 distinct values** (azure ids for previousExchgAssignedPolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([exchgAssignedPolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5, :p6, :p7, :p8, :p9, :p10, :p11, :p12, :p13, :p14, :p15, :p16, :p17, ` → **0** (policy IN match household_or_employee_case_id->exchgAssignedPolicyID)
- `SELECT DISTINCT TOP 20000 CAST([exchgAssignedPolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [exchgAssignedPolicyID] IS NOT NULL` → **20000 distinct values** (azure ids for exchgAssignedPolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([healthCoveragePolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5, :p6, :p7, :p8, :p9, :p10, :p11, :p12, :p13, :p14, :p15, :p16, :p17,` → **0** (policy IN match household_or_employee_case_id->healthCoveragePolicyID)
- `SELECT DISTINCT TOP 20000 CAST([healthCoveragePolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [healthCoveragePolicyID] IS NOT NULL` → **20000 distinct values** (azure ids for healthCoveragePolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([previousExchgAssignedPolicyID] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5, :p6, :p7, :p8, :p9, :p10, :p11, :p12, :p13, :p14, :p15, :p16` → **0** (policy IN match household_or_employee_case_id->previousExchgAssignedPolicyID)
- `SELECT DISTINCT TOP 20000 CAST([previousExchgAssignedPolicyID] AS VARCHAR(200)) AS v FROM [dbo].[834_Inbound_test] WHERE [previousExchgAssignedPolicyID] IS NOT NULL` → **6375 distinct values** (azure ids for previousExchgAssignedPolicyID)
- `SELECT COUNT(*) FROM [dbo].[834_Inbound_test] WHERE CAST([exchgIndivIdentifier] AS VARCHAR(200)) IN (:p0, :p1, :p2, :p3, :p4, :p5, :p6, :p7, :p8, :p9, :p10, :p11, :p12, :p13, :p14, :p15, :p16, :p17, :` → **6** (member IN match member_id->exchgIndivIdentifier)
