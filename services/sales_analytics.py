from __future__ import annotations

import logging
from dataclasses import dataclass

import pandas as pd
from sqlalchemy import inspect
from sqlalchemy.engine import Engine

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class EnrichedSales:
    """Sales rows joined to dealers; same logic as curated SQL views."""

    df: pd.DataFrame
    source: str  # sqlite table description


def table_exists(engine: Engine, name: str) -> bool:
    return inspect(engine).has_table(name)


def load_enriched_sales_from_sqlite(engine: Engine) -> EnrichedSales | None:
    """
    Load clean_sales joined to clean_dealers from SQLite (authoritative store after ETL).
    Aligns dealer_id types so joins match persisted data.
    """
    if not table_exists(engine, "clean_sales"):
        logger.warning("clean_sales table missing; run ETL first")
        return None

    sales = pd.read_sql_query("SELECT * FROM clean_sales", engine)
    if sales.empty:
        return EnrichedSales(df=pd.DataFrame(), source="clean_sales(empty)")

    for col in ("dealer_id", "model_code", "sale_id"):
        if col in sales.columns:
            sales[col] = sales[col].astype("string").str.strip()

    sales["sale_date"] = pd.to_datetime(sales["sale_date"], errors="coerce")
    sales["sale_price"] = pd.to_numeric(sales["sale_price"], errors="coerce")
    sales = sales.dropna(subset=["sale_date", "sale_price"])

    if not table_exists(engine, "clean_dealers"):
        sales["dealer_name"] = pd.NA
        sales["region"] = pd.NA
        return EnrichedSales(df=sales, source="clean_sales only (no clean_dealers)")

    dealers = pd.read_sql_query("SELECT * FROM clean_dealers", engine)
    if "dealer_id" in dealers.columns:
        dealers["dealer_id"] = dealers["dealer_id"].astype("string").str.strip()
    merge_cols = [c for c in ["dealer_id", "dealer_name", "region"] if c in dealers.columns]
    out = sales.merge(dealers[merge_cols].drop_duplicates("dealer_id"), on="dealer_id", how="left")
    if "region" in out.columns:
        out["region"] = out["region"].astype("string").str.upper()
    if "dealer_name" in out.columns:
        out["dealer_name"] = out["dealer_name"].astype("string")

    return EnrichedSales(df=out, source="clean_sales JOIN clean_dealers")


def load_dq_summary(engine: Engine) -> pd.DataFrame | None:
    if not table_exists(engine, "dq_issues"):
        return None
    q = """
    SELECT severity, COUNT(*) AS issue_count
    FROM dq_issues
    GROUP BY severity
    ORDER BY severity
    """
    return pd.read_sql_query(q, engine)
