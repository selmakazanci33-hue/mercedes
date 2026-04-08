from __future__ import annotations

import re
from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class CleanRejects:
    table_name: str
    rejects: pd.DataFrame


def clean_tables(raw: dict[str, pd.DataFrame]) -> tuple[dict[str, pd.DataFrame], list[CleanRejects]]:
    cleaned: dict[str, pd.DataFrame] = {}
    rejects: list[CleanRejects] = []
    for name, df in raw.items():
        cdf = df.copy()
        cdf.columns = [_clean_col(c) for c in cdf.columns]
        cdf = _strip_strings(cdf)
        cdf = _parse_dates(cdf)
        cdf = _coerce_numeric(cdf)
        cdf = _table_specific_standardization(name, cdf)
        cdf, rej = _basic_row_rejects(name, cdf)
        cleaned[name] = cdf
        if rej is not None and len(rej) > 0:
            rejects.append(CleanRejects(table_name=name, rejects=rej))
    return cleaned, rejects


def _clean_col(col: str) -> str:
    s = str(col).strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    s = re.sub(r"_+", "_", s)
    return s[:128]


def _strip_strings(df: pd.DataFrame) -> pd.DataFrame:
    obj_cols = [c for c in df.columns if df[c].dtype == "object"]
    for c in obj_cols:
        df[c] = df[c].map(lambda x: x.strip() if isinstance(x, str) else x)
    return df


def _parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    # Heuristic: parse columns that look like dates
    for c in df.columns:
        if any(k in c for k in ("date", "month")) and df[c].dtype == "object":
            parsed = pd.to_datetime(df[c], errors="coerce", utc=False)
            if parsed.notna().sum() > 0:
                df[c] = parsed
    if "sale_date" in df.columns:
        df["sale_month"] = pd.to_datetime(df["sale_date"], errors="coerce").dt.to_period("M").dt.to_timestamp()
    return df


def _coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    numeric_hint = (
        "price",
        "apr",
        "money_factor",
        "residual",
        "pct",
        "units",
        "on_hand",
        "term_months",
    )
    for c in df.columns:
        if any(h in c for h in numeric_hint) and df[c].dtype == "object":
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def _table_specific_standardization(table_name: str, df: pd.DataFrame) -> pd.DataFrame:
    """
    Sheet-aware normalization so downstream joins are consistent.
    Assumes sheet keys are canonical (dealers, models, inventory, sales, interest_rates, forecast_assumptions).
    """
    out = df.copy()

    if table_name in ("dealers", "inventory", "sales"):
        if "dealer_id" in out.columns:
            out["dealer_id"] = out["dealer_id"].astype("string").str.strip()

    if table_name == "sales":
        if "sale_date" in out.columns:
            out["sale_date"] = pd.to_datetime(out["sale_date"], errors="coerce")
            out["sale_month"] = out["sale_date"].dt.to_period("M").dt.to_timestamp()
        for c in ("dealer_id", "model_code", "sale_id"):
            if c in out.columns:
                out[c] = out[c].astype("string")

    if table_name in ("dealers", "inventory", "sales", "forecast_assumptions", "interest_rates"):
        if "region" in out.columns:
            out["region"] = out["region"].astype("string").str.upper().str.strip()

    if table_name in ("models", "inventory", "sales", "interest_rates", "forecast_assumptions"):
        if "model_code" in out.columns:
            out["model_code"] = out["model_code"].astype("string").str.upper().str.strip()

    if table_name in ("interest_rates", "forecast_assumptions"):
        if "month" in out.columns:
            out["month"] = pd.to_datetime(out["month"], errors="coerce").dt.to_period("M").dt.to_timestamp()

    return out


def _basic_row_rejects(table_name: str, df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame | None]:
    """
    Keeps all rows by default; creates a rejects table only for clearly broken records
    (e.g., all-null rows or rows missing every non-nullable key when we can infer them).
    """
    all_null = df.isna().all(axis=1)
    rej = df.loc[all_null].copy()
    kept = df.loc[~all_null].copy()
    if len(rej) == 0:
        return kept, None
    rej["reject_reason"] = "all_columns_null"
    return kept, rej

