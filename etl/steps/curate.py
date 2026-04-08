from __future__ import annotations

import pandas as pd


def build_curated(clean: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """
    Creates curated, analyst-friendly summary tables.
    This is intentionally resilient: it will only build outputs when source columns exist.
    """
    curated: dict[str, pd.DataFrame] = {}

    # Canonical tables (from known workbook sheet names)
    dealers = clean.get("dealers")
    models = clean.get("models")
    inventory = clean.get("inventory")
    sales = clean.get("sales")
    interest_rates = clean.get("interest_rates")
    forecast = clean.get("forecast_assumptions")

    if sales is not None:
        curated["monthly_sales_summary"] = _monthly_sales_summary(sales)
        curated["dealer_performance_summary"] = _dealer_perf(sales, dealers)
        curated["model_performance_summary"] = _model_perf(sales, models)
        curated["pricing_variance_summary"] = _pricing_variance(sales)
        curated["regional_performance_summary"] = _regional_perf(sales)

    if inventory is not None and sales is not None:
        curated["inventory_vs_sales_summary"] = _inventory_vs_sales(inventory, sales, dealers, models)

    if forecast is not None and sales is not None:
        curated["forecast_vs_actual_summary"] = _forecast_vs_actual(forecast, sales)

    return curated


def _pick(tables: dict[str, pd.DataFrame], candidates: list[str]) -> pd.DataFrame | None:
    for c in candidates:
        if c in tables:
            return tables[c]
    return None


def _monthly_sales_summary(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.copy()
    month_col = "sale_month" if "sale_month" in df.columns else ("month" if "month" in df.columns else None)
    if month_col is None:
        return pd.DataFrame()
    grp = df.groupby([month_col], dropna=False)
    out = grp.agg(
        sales_count=("sale_id", "count") if "sale_id" in df.columns else (month_col, "count"),
        total_revenue=("sale_price", "sum") if "sale_price" in df.columns else (month_col, "size"),
        avg_sale_price=("sale_price", "mean") if "sale_price" in df.columns else (month_col, "size"),
    ).reset_index()
    out = out.rename(columns={month_col: "month"})
    return out.sort_values("month")


def _dealer_perf(sales: pd.DataFrame, dealers: pd.DataFrame | None) -> pd.DataFrame:
    if "dealer_id" not in sales.columns:
        return pd.DataFrame()
    grp = sales.groupby(["dealer_id"], dropna=False)
    out = grp.agg(
        sales_count=("sale_id", "count") if "sale_id" in sales.columns else ("dealer_id", "count"),
        total_revenue=("sale_price", "sum") if "sale_price" in sales.columns else ("dealer_id", "size"),
        avg_sale_price=("sale_price", "mean") if "sale_price" in sales.columns else ("dealer_id", "size"),
    ).reset_index()
    if dealers is not None and "dealer_id" in dealers.columns:
        out["dealer_id"] = out["dealer_id"].astype("string")
        dealers = dealers.copy()
        dealers["dealer_id"] = dealers["dealer_id"].astype("string")
        join_cols = [c for c in ["dealer_id", "dealer_name", "region"] if c in dealers.columns]
        out = out.merge(dealers[join_cols].drop_duplicates("dealer_id"), on="dealer_id", how="left")
    return out.sort_values(["total_revenue"], ascending=False)


def _model_perf(sales: pd.DataFrame, models: pd.DataFrame | None) -> pd.DataFrame:
    if "model_code" not in sales.columns:
        return pd.DataFrame()
    grp = sales.groupby(["model_code"], dropna=False)
    out = grp.agg(
        sales_count=("sale_id", "count") if "sale_id" in sales.columns else ("model_code", "count"),
        total_revenue=("sale_price", "sum") if "sale_price" in sales.columns else ("model_code", "size"),
        avg_sale_price=("sale_price", "mean") if "sale_price" in sales.columns else ("model_code", "size"),
    ).reset_index()
    if models is not None and "model_code" in models.columns:
        join_cols = [c for c in ["model_code", "model_name", "segment"] if c in models.columns]
        out = out.merge(models[join_cols].drop_duplicates("model_code"), on="model_code", how="left")
    return out.sort_values(["total_revenue"], ascending=False)


def _pricing_variance(sales: pd.DataFrame) -> pd.DataFrame:
    if "model_code" not in sales.columns or "sale_price" not in sales.columns:
        return pd.DataFrame()
    grp_cols = [c for c in ["model_code", "region"] if c in sales.columns]
    if not grp_cols:
        grp_cols = ["model_code"]
    grp = sales.groupby(grp_cols, dropna=False)
    out = grp.agg(
        n=("sale_price", "count"),
        avg_price=("sale_price", "mean"),
        p10=("sale_price", lambda x: x.quantile(0.10)),
        p90=("sale_price", lambda x: x.quantile(0.90)),
        min_price=("sale_price", "min"),
        max_price=("sale_price", "max"),
    ).reset_index()
    out["p90_minus_p10"] = out["p90"] - out["p10"]
    return out.sort_values(["p90_minus_p10"], ascending=False)


def _regional_perf(sales: pd.DataFrame) -> pd.DataFrame:
    if "region" not in sales.columns:
        return pd.DataFrame()
    grp = sales.groupby(["region"], dropna=False)
    out = grp.agg(
        sales_count=("sale_id", "count") if "sale_id" in sales.columns else ("region", "count"),
        total_revenue=("sale_price", "sum") if "sale_price" in sales.columns else ("region", "size"),
        avg_sale_price=("sale_price", "mean") if "sale_price" in sales.columns else ("region", "size"),
    ).reset_index()
    return out.sort_values(["total_revenue"], ascending=False)


def _inventory_vs_sales(
    inventory: pd.DataFrame,
    sales: pd.DataFrame,
    dealers: pd.DataFrame | None,
    models: pd.DataFrame | None,
) -> pd.DataFrame:
    if not {"dealer_id", "model_code"}.issubset(set(inventory.columns)) or not {"dealer_id", "model_code"}.issubset(
        set(sales.columns)
    ):
        return pd.DataFrame()

    inv = inventory.copy()
    inv["dealer_id"] = inv["dealer_id"].astype("string")
    inv["model_code"] = inv["model_code"].astype("string")
    if "on_hand" in inv.columns:
        inv["on_hand"] = pd.to_numeric(inv["on_hand"], errors="coerce")

    # sales volume proxy: count sales per dealer/model
    s = sales.copy()
    s["dealer_id"] = s["dealer_id"].astype("string")
    s["model_code"] = s["model_code"].astype("string")
    s["sales_units"] = 1
    units = s.groupby(["dealer_id", "model_code"], dropna=False).agg(sales_units=("sales_units", "sum")).reset_index()

    out = inv.merge(units, on=["dealer_id", "model_code"], how="left")
    out["sales_units"] = out["sales_units"].fillna(0).astype(int)
    if "on_hand" in out.columns:
        out["inventory_gap"] = out["on_hand"].fillna(0) - out["sales_units"]

    if dealers is not None and "dealer_id" in dealers.columns:
        join_cols = [c for c in ["dealer_id", "dealer_name", "region"] if c in dealers.columns]
        out = out.merge(dealers[join_cols].drop_duplicates("dealer_id"), on="dealer_id", how="left")
    if models is not None and "model_code" in models.columns:
        join_cols = [c for c in ["model_code", "model_name", "segment"] if c in models.columns]
        out = out.merge(models[join_cols].drop_duplicates("model_code"), on="model_code", how="left")

    sort_col = "inventory_gap" if "inventory_gap" in out.columns else ("on_hand" if "on_hand" in out.columns else None)
    return out.sort_values(sort_col, ascending=True) if sort_col else out


def _forecast_vs_actual(forecast: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    if "month" not in forecast.columns or "sale_month" not in sales.columns:
        return pd.DataFrame()

    f = forecast.copy()
    f["month"] = pd.to_datetime(f["month"], errors="coerce").dt.to_period("M").dt.to_timestamp()

    s = sales.copy()
    s["sale_month"] = pd.to_datetime(s["sale_month"], errors="coerce").dt.to_period("M").dt.to_timestamp()
    s["actual_units"] = 1

    grp_cols = [c for c in ["month", "region", "model_code"] if c in f.columns and c in sales.columns or c == "month"]
    # Align sales month column name to 'month' for join
    s = s.rename(columns={"sale_month": "month"})

    actual = s.groupby([c for c in ["month", "region", "model_code"] if c in s.columns], dropna=False).agg(
        actual_units=("actual_units", "sum"),
        actual_avg_price=("sale_price", "mean") if "sale_price" in s.columns else ("actual_units", "sum"),
    ).reset_index()

    join_cols = [c for c in ["month", "region", "model_code"] if c in f.columns and c in actual.columns]
    out = f.merge(actual, on=join_cols, how="left")
    if "units_forecast" in out.columns:
        out["unit_variance"] = out["actual_units"].fillna(0) - out["units_forecast"]
    if "avg_price_assumption" in out.columns and "actual_avg_price" in out.columns:
        out["avg_price_variance"] = out["actual_avg_price"] - out["avg_price_assumption"]
    return out.sort_values(["month"])

