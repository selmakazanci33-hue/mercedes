from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class DqOutputs:
    table_scores: pd.DataFrame
    issues: pd.DataFrame


def run_data_quality(
    *,
    raw: dict[str, pd.DataFrame],
    clean: dict[str, pd.DataFrame],
    rejects: list,
    run_id: str,
) -> DqOutputs:
    issues = []
    scores = []

    expected_tables = {
        "dealers",
        "models",
        "inventory",
        "sales",
        "interest_rates",
        "forecast_assumptions",
    }
    for t in sorted(expected_tables):
        if t not in clean:
            issues.append(
                _issue(
                    run_id,
                    t,
                    severity="critical",
                    issue_type="missing_sheet",
                    column_name=None,
                    row_identifier=None,
                    message=f"Required sheet '{t}' missing after extract/clean mapping",
                    business_impact="Core subject area missing; KPIs and joins will be incomplete or misleading.",
                    recommended_action="Confirm sheet names and workbook contents; ensure the Excel file is the expected version.",
                )
            )

    # Required columns per canonical sheet
    required_cols = {
        "dealers": ["dealer_id", "dealer_name", "region"],
        "models": ["model_code", "model_name", "segment"],
        "inventory": ["dealer_id", "model_code", "on_hand"],
        "sales": ["sale_id", "sale_date", "dealer_id", "model_code", "sale_price"],
        "interest_rates": ["month", "region", "model_code", "product_type", "term_months", "credit_tier"],
        "forecast_assumptions": ["month", "region", "model_code", "units_forecast", "avg_price_assumption", "apr_assumption"],
    }

    for table_name, df in clean.items():
        # required columns check
        if table_name in required_cols:
            missing_cols = [c for c in required_cols[table_name] if c not in df.columns]
            if missing_cols:
                issues.append(
                    _issue(
                        run_id,
                        table_name,
                        severity="critical",
                        issue_type="missing_columns",
                        column_name=None,
                        row_identifier=None,
                        message=f"Missing required columns: {', '.join(missing_cols)}",
                        business_impact="Cannot reliably build curated analytics and joins; results may be invalid.",
                        recommended_action="Verify the sheet schema matches the business case; update column names or mapping.",
                    )
                )

        if df.empty:
            issues.append(
                _issue(
                    run_id,
                    table_name,
                    severity="critical",
                    issue_type="empty",
                    column_name=None,
                    row_identifier=None,
                    message="Table is empty after cleaning",
                    business_impact="No visibility for this subject area; downstream joins and KPIs may be incomplete.",
                    recommended_action="Confirm sheet mapping and required columns; verify source file is complete.",
                )
            )

        # Uniqueness / duplicates on key columns (when present)
        key_candidates = {
            "dealers": ["dealer_id"],
            "models": ["model_code"],
            "inventory": ["dealer_id", "model_code"],
            "sales": ["sale_id"],
            "interest_rates": ["month", "region", "model_code", "product_type", "term_months", "credit_tier"],
            "forecast_assumptions": ["month", "region", "model_code"],
        }
        keys = key_candidates.get(table_name)
        if keys and all(k in df.columns for k in keys) and len(df) > 0:
            dups = df.duplicated(subset=keys, keep=False)
            if int(dups.sum()) > 0:
                issues.append(
                    _issue(
                        run_id,
                        table_name,
                        severity="medium",
                        issue_type="duplicate_keys",
                        column_name=",".join(keys),
                        row_identifier=None,
                        message=f"Duplicate business keys detected ({int(dups.sum())} rows) on {keys}",
                        business_impact="Duplicates inflate counts and can distort pricing/volume metrics.",
                        recommended_action="Confirm whether duplicates are legitimate; otherwise deduplicate or fix key generation.",
                    )
                )

        missing_pct = df.isna().mean(numeric_only=False)
        for col, pct in missing_pct.items():
            if pct >= 0.25:
                sev = "critical" if pct >= 0.5 else "medium"
                issues.append(
                    _issue(
                        run_id,
                        table_name,
                        severity=sev,
                        issue_type="missing",
                        column_name=str(col),
                        row_identifier=None,
                        message=f"High missingness in column '{col}' ({pct:.1%})",
                        business_impact=_impact_for_column(table_name, str(col)),
                        recommended_action="Backfill from source system or adjust analysis to exclude incomplete records.",
                    )
                )

        score = _score_table(df, table_name, issues_for_table=[i for i in issues if i["table_name"] == table_name])
        scores.append(
            {
                "pipeline_run_id": run_id,
                "table_name": table_name,
                "quality_score": score,
                "critical_issue_count": sum(1 for i in issues if i["table_name"] == table_name and i["severity"] == "critical"),
                "medium_issue_count": sum(1 for i in issues if i["table_name"] == table_name and i["severity"] == "medium"),
                "low_issue_count": sum(1 for i in issues if i["table_name"] == table_name and i["severity"] == "low"),
                "notes": None,
            }
        )

    # Referential integrity checks (Sales/Inventory → Dealers/Models)
    dealers = clean.get("dealers")
    models = clean.get("models")
    sales = clean.get("sales")
    inventory = clean.get("inventory")

    if sales is not None and dealers is not None and "dealer_id" in sales.columns and "dealer_id" in dealers.columns:
        orphan = ~sales["dealer_id"].isin(dealers["dealer_id"])
        orphan_count = int(orphan.fillna(False).sum())
        if orphan_count > 0:
            issues.append(
                _issue(
                    run_id,
                    "sales",
                    severity="critical",
                    issue_type="orphan_key",
                    column_name="dealer_id",
                    row_identifier=None,
                    message=f"{orphan_count} sales rows have dealer_id not found in Dealers",
                    business_impact="Dealer-level performance and regional rollups will be incomplete or misattributed.",
                    recommended_action="Fix dealer_id mapping or load the missing Dealers records; do not drop silently.",
                )
            )

    if sales is not None and models is not None and "model_code" in sales.columns and "model_code" in models.columns:
        orphan = ~sales["model_code"].isin(models["model_code"])
        orphan_count = int(orphan.fillna(False).sum())
        if orphan_count > 0:
            issues.append(
                _issue(
                    run_id,
                    "sales",
                    severity="critical",
                    issue_type="orphan_key",
                    column_name="model_code",
                    row_identifier=None,
                    message=f"{orphan_count} sales rows have model_code not found in Models",
                    business_impact="Model-level pricing and volume analytics will be incomplete or misattributed.",
                    recommended_action="Fix model_code mapping or load the missing Models records; validate code casing/format.",
                )
            )

    if inventory is not None and dealers is not None and "dealer_id" in inventory.columns and "dealer_id" in dealers.columns:
        orphan = ~inventory["dealer_id"].isin(dealers["dealer_id"])
        orphan_count = int(orphan.fillna(False).sum())
        if orphan_count > 0:
            issues.append(
                _issue(
                    run_id,
                    "inventory",
                    severity="medium",
                    issue_type="orphan_key",
                    column_name="dealer_id",
                    row_identifier=None,
                    message=f"{orphan_count} inventory rows have dealer_id not found in Dealers",
                    business_impact="Inventory vs demand analyses may be incomplete for affected dealers.",
                    recommended_action="Reconcile dealer_id mapping and ensure Dealers sheet includes all referenced dealers.",
                )
            )

    if inventory is not None and models is not None and "model_code" in inventory.columns and "model_code" in models.columns:
        orphan = ~inventory["model_code"].isin(models["model_code"])
        orphan_count = int(orphan.fillna(False).sum())
        if orphan_count > 0:
            issues.append(
                _issue(
                    run_id,
                    "inventory",
                    severity="medium",
                    issue_type="orphan_key",
                    column_name="model_code",
                    row_identifier=None,
                    message=f"{orphan_count} inventory rows have model_code not found in Models",
                    business_impact="Inventory vs sales and model availability analyses may be incomplete.",
                    recommended_action="Reconcile model_code formatting; ensure Models sheet includes all referenced models.",
                )
            )

    issues_df = pd.DataFrame(issues) if issues else pd.DataFrame(
        columns=[
            "pipeline_run_id",
            "table_name",
            "severity",
            "issue_type",
            "column_name",
            "row_identifier",
            "message",
            "business_impact",
            "recommended_action",
        ]
    )
    scores_df = pd.DataFrame(scores) if scores else pd.DataFrame(
        columns=[
            "pipeline_run_id",
            "table_name",
            "quality_score",
            "critical_issue_count",
            "medium_issue_count",
            "low_issue_count",
            "notes",
        ]
    )
    return DqOutputs(table_scores=scores_df, issues=issues_df)


def _issue(
    run_id: str,
    table_name: str,
    severity: str,
    issue_type: str,
    column_name: str | None,
    row_identifier: str | None,
    message: str,
    business_impact: str,
    recommended_action: str,
) -> dict:
    return {
        "pipeline_run_id": run_id,
        "table_name": table_name,
        "severity": severity,
        "issue_type": issue_type,
        "column_name": column_name,
        "row_identifier": row_identifier,
        "message": message,
        "business_impact": business_impact,
        "recommended_action": recommended_action,
    }


def _score_table(df: pd.DataFrame, table_name: str, issues_for_table: list[dict]) -> float:
    # 100 - penalties. Keep simple and explainable.
    penalty = 0.0
    penalty += 40.0 if df.empty else 0.0
    penalty += 10.0 * sum(1 for i in issues_for_table if i["severity"] == "critical")
    penalty += 4.0 * sum(1 for i in issues_for_table if i["severity"] == "medium")
    penalty += 1.0 * sum(1 for i in issues_for_table if i["severity"] == "low")

    # mild penalty for overall missingness
    overall_missing = float(df.isna().mean().mean()) if len(df.columns) > 0 else 1.0
    penalty += min(20.0, overall_missing * 20.0)

    return float(max(0.0, min(100.0, 100.0 - penalty)))


def _impact_for_column(table_name: str, col: str) -> str:
    key_cols = {"dealer_id", "model_code", "region", "sale_date", "sale_price", "month"}
    if col in key_cols:
        return f"Missing '{col}' reduces the ability to join and compute reliable KPIs in '{table_name}'."
    return f"Missing '{col}' may bias metrics and segment-level comparisons in '{table_name}'."

