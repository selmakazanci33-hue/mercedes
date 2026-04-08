from __future__ import annotations

import logging
from typing import Any

import pandas as pd


logger = logging.getLogger(__name__)


def extract_excel_tables(source_path: str) -> dict[str, pd.DataFrame]:
    """
    Reads every sheet from the Excel file into a dict of DataFrames.
    Sheet names are normalized into safe table keys.
    """
    xl = pd.ExcelFile(source_path)
    tables: dict[str, pd.DataFrame] = {}
    for sheet in xl.sheet_names:
        df = xl.parse(sheet_name=sheet)
        key = _canonical_sheet_key(sheet)
        tables[key] = df
        logger.info("Extracted sheet=%s key=%s rows=%s cols=%s", sheet, key, len(df), len(df.columns))
    if not tables:
        raise ValueError("No sheets found in Excel file")

    _enforce_expected_sheets(tables)
    return tables


def _normalize_sheet_name(name: str) -> str:
    safe = "".join(ch.lower() if ch.isalnum() else "_" for ch in name).strip("_")
    safe = "_".join([p for p in safe.split("_") if p])
    return safe[:120]


def _canonical_sheet_key(sheet_name: str) -> str:
    """
    Maps the known workbook sheets to stable keys used by the rest of the pipeline.
    Anything unknown falls back to a normalized key.
    """
    n = _normalize_sheet_name(sheet_name)
    mapping = {
        "dealers": "dealers",
        "models": "models",
        "inventory": "inventory",
        "sales": "sales",
        "interest_rates": "interest_rates",
        "interest_rate": "interest_rates",
        "forecast_assumptions": "forecast_assumptions",
        "forecast_assumption": "forecast_assumptions",
    }
    return mapping.get(n, n)


def _enforce_expected_sheets(tables: dict[str, pd.DataFrame]) -> None:
    expected = {
        "dealers",
        "models",
        "inventory",
        "sales",
        "interest_rates",
        "forecast_assumptions",
    }
    missing = sorted(expected - set(tables.keys()))
    if missing:
        raise ValueError(
            "Missing required sheet(s): "
            + ", ".join(missing)
            + ". Expected: Dealers, Models, Inventory, Sales, Interest_Rates, Forecast_Assumptions."
        )

