Automated 834 Enrollment Processing & Issuer Data Consolidation
Project Plan
Project Overview
This project establishes a centralized enrollment data platform by automating the complete processing of inbound 834 enrollment transactions and consolidating all issuer-related datasets into a single Azure-based repository.
The first phase automates the ingestion, validation, normalization, and reconciliation of all issuer 834 inbound files from October 2025 through June 2026, while collecting operational performance metrics.
Once the 834 foundation is complete, the platform will progressively integrate:
RCNI Monthly Reconciliation Reports
SBMI Monthly Policy-Based Payment (PBP) Files
DDR (Dispute Disposition Reports)
IRS End-of-Month (EOM) Files
IRS End-of-Year (EOY) Files
to provide complete enrollment traceability, reconciliation, discrepancy analysis, financial validation, and tax reporting support.
The platform is designed to become the operational source of truth for enrollment investigations across Georgia Access, issuers, CMS, and IRS.
Objectives
The objective of this project is to build a scalable automated enrollment processing platform that:
Automatically ingests all issuer 834 inbound files into Azure.
Establishes 834 inbound data as the primary source of truth for enrollment history.
Validates row counts, policy counts, enrollee counts, statuses, and column mappings.
Supports complete policy transaction traceability (CONFIRM, CHANGE, TERM, REINSTATE, etc.).
Loads and validates monthly RCNI reconciliation reports against inbound 834 data.
Tracks unresolved reconciliation discrepancies over time.
Integrates monthly SBMI files for issuer-side enrollment and financial validation.
Loads DDR reports to analyze CMS vs. issuer APTC discrepancies.
Integrates IRS EOM and EOY files for tax reporting validation.
Maps Tier 2 record-level errors back to the original 834 transaction history.
Monitors Tier 1 rejected files to proactively identify unprocessed inbound files.
Captures runtime statistics for operational benchmarking.
Provides complete auditability across every enrollment transaction.
Creates a reusable enterprise data foundation for future operational analytics.
Scope
Phase 1 — 834 Inbound Foundation
Automated ingestion of all issuer 834 inbound files
Azure data loading
Validation
Runtime measurements
Policy transaction history
Performance benchmarking
Phase 2 — RCNI Integration
Monthly RCNI loading
Validation against 834
Discrepancy tracking
Issuer trend analysis
Phase 3 — Tier Validation
Tier 2
Map every Tier 2 record back to the original 834 transaction
Validate rejected record behavior
Tier 1
Monitor rejected files
Track pending files
Proactively identify failed inbound files
(Monitoring only — automation is outside the current project scope.)
Phase 4 — SBMI Integration
Load monthly SBMI files containing:
Policy information
Enrollment information
Financial information
APTC payment information
Validate issuer-side data against Georgia Access enrollment history.
Phase 5 — DDR Integration
Load monthly DDR reports to:
Compare issuer vs CMS financial discrepancies
Validate APTC differences
Identify responsibility between:
Georgia Access
CMS
Issuers
Phase 6 — IRS Integration
Load
IRS End-of-Month (EOM)
IRS End-of-Year (EOY)
Support
1095 validation
Customer issue investigation
Tax reporting audit trails
Phase 7 — Operations Search Platform
(Future Phase)
Build a searchable operational interface allowing users to search by:
Policy ID
Member ID
Enrollment ID
and immediately retrieve:
834 transaction history
RCNI discrepancies
SBMI history
DDR financial differences
IRS EOM/EOY records
Tier 2 validation
Root cause analysis
Security Requirements
Read-only automation
Never modify FTP source files
Never delete inbound files
MFA authentication
Controlled production scheduling
Audit logging
Environment protection
Documentation
Maintain documentation for:
Data models
ETL workflows
Validation rules
Reconciliation logic
Runtime metrics
SOPs
Operational procedures
Out of Scope
Changes to issuer systems
CMS regulatory reporting changes
Predictive analytics / ML
Historical manual cleanup
Tier 1 automation
UI development (future phase)
