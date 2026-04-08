from __future__ import annotations

import json
from typing import Any

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from services.sales_analytics import EnrichedSales

# Consistent styling
_PLOTLY_TEMPLATE = "plotly_white"
_COLOR_SEQUENCE = px.colors.qualitative.Set2


def _fig_to_safe_dict(fig: go.Figure) -> dict[str, Any]:
    """Round-trip through Plotly JSON so Jinja `tojson` has no numpy types."""
    return json.loads(fig.to_json())


def _empty_fig(title: str, message: str) -> go.Figure:
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(size=14),
    )
    fig.update_layout(title=title, template=_PLOTLY_TEMPLATE, height=360)
    return fig


def build_dashboard_figures(enriched: EnrichedSales | None, top_n_dealers: int = 10) -> dict[str, Any]:
    """
    Build Plotly figure dicts (plotly JSON-compatible) for the executive dashboard.
    All series derive from the same enriched DataFrame as SQLite (post-join).
    """
    out: dict[str, Any] = {}
    if enriched is None:
        empty = _empty_fig("No data", "Run ETL and ensure clean_sales has rows.")
        out["daily_total"] = _fig_to_safe_dict(empty)
        out["daily_by_region"] = _fig_to_safe_dict(empty)
        out["daily_by_dealer"] = _fig_to_safe_dict(empty)
        out["monthly_total"] = _fig_to_safe_dict(empty)
        out["monthly_by_region"] = _fig_to_safe_dict(empty)
        out["monthly_by_dealer"] = _fig_to_safe_dict(empty)
        return out
    if enriched.df is None or enriched.df.empty:
        empty = _empty_fig("No data", "Run ETL and ensure clean_sales has rows.")
        out["daily_total"] = _fig_to_safe_dict(empty)
        out["daily_by_region"] = _fig_to_safe_dict(empty)
        out["daily_by_dealer"] = _fig_to_safe_dict(empty)
        out["monthly_total"] = _fig_to_safe_dict(empty)
        out["monthly_by_region"] = _fig_to_safe_dict(empty)
        out["monthly_by_dealer"] = _fig_to_safe_dict(empty)
        return out

    df = enriched.df.copy()
    df["revenue"] = df["sale_price"]
    df["day"] = df["sale_date"].dt.floor("D")
    df["month_period"] = df["sale_date"].dt.to_period("M").dt.to_timestamp()

    # --- Daily ---
    daily_total = df.groupby("day", as_index=False)["revenue"].sum()
    fig_dt = px.line(
        daily_total,
        x="day",
        y="revenue",
        title="Daily revenue (total)",
        labels={"revenue": "Revenue", "day": "Date"},
    )
    fig_dt.update_traces(line=dict(width=2))
    fig_dt.update_layout(template=_PLOTLY_TEMPLATE, height=400, hovermode="x unified")
    out["daily_total"] = _fig_to_safe_dict(fig_dt)

    if "region" in df.columns and df["region"].notna().any():
        daily_reg = df.groupby(["day", "region"], as_index=False)["revenue"].sum()
        fig_dr = px.line(
            daily_reg,
            x="day",
            y="revenue",
            color="region",
            title="Daily revenue by region",
            labels={"revenue": "Revenue", "day": "Date"},
            color_discrete_sequence=_COLOR_SEQUENCE,
        )
        fig_dr.update_layout(template=_PLOTLY_TEMPLATE, height=420, hovermode="x unified", legend_title_text="Region")
        out["daily_by_region"] = _fig_to_safe_dict(fig_dr)
    else:
        out["daily_by_region"] = _fig_to_safe_dict(
            _empty_fig("Daily revenue by region", "Region not available; check clean_dealers join.")
        )

    dealer_label = "dealer_name" if "dealer_name" in df.columns and df["dealer_name"].notna().any() else "dealer_id"
    top_dealers = (
        df.groupby(dealer_label, as_index=False)["revenue"]
        .sum()
        .nlargest(top_n_dealers, "revenue")[dealer_label]
        .tolist()
    )
    sub = df[df[dealer_label].isin(top_dealers)]
    daily_d = sub.groupby(["day", dealer_label], as_index=False)["revenue"].sum()
    fig_dd = px.line(
        daily_d,
        x="day",
        y="revenue",
        color=dealer_label,
        title=f"Daily revenue — top {top_n_dealers} dealers by total revenue",
        labels={"revenue": "Revenue", "day": "Date", dealer_label: "Dealer"},
        color_discrete_sequence=_COLOR_SEQUENCE,
    )
    fig_dd.update_layout(template=_PLOTLY_TEMPLATE, height=460, hovermode="x unified")
    out["daily_by_dealer"] = _fig_to_safe_dict(fig_dd)

    # --- Monthly ---
    monthly_total = df.groupby("month_period", as_index=False)["revenue"].sum()
    fig_mt = px.bar(
        monthly_total,
        x="month_period",
        y="revenue",
        title="Monthly revenue (total)",
        labels={"revenue": "Revenue", "month_period": "Month"},
    )
    fig_mt.update_layout(template=_PLOTLY_TEMPLATE, height=400, xaxis_tickangle=-45)
    out["monthly_total"] = _fig_to_safe_dict(fig_mt)

    if "region" in df.columns and df["region"].notna().any():
        monthly_reg = df.groupby(["month_period", "region"], as_index=False)["revenue"].sum()
        fig_mr = px.bar(
            monthly_reg,
            x="month_period",
            y="revenue",
            color="region",
            title="Monthly revenue by region",
            labels={"revenue": "Revenue", "month_period": "Month"},
            barmode="stack",
            color_discrete_sequence=_COLOR_SEQUENCE,
        )
        fig_mr.update_layout(template=_PLOTLY_TEMPLATE, height=460, xaxis_tickangle=-45, legend_title_text="Region")
        out["monthly_by_region"] = _fig_to_safe_dict(fig_mr)
    else:
        out["monthly_by_region"] = _fig_to_safe_dict(_empty_fig("Monthly revenue by region", "Region not available."))

    monthly_d = sub.groupby(["month_period", dealer_label], as_index=False)["revenue"].sum()
    fig_md = px.bar(
        monthly_d,
        x="month_period",
        y="revenue",
        color=dealer_label,
        title=f"Monthly revenue — top {top_n_dealers} dealers",
        labels={"revenue": "Revenue", "month_period": "Month"},
        barmode="group",
        color_discrete_sequence=_COLOR_SEQUENCE,
    )
    fig_md.update_layout(template=_PLOTLY_TEMPLATE, height=500, xaxis_tickangle=-45)
    out["monthly_by_dealer"] = _fig_to_safe_dict(fig_md)

    return out


def build_dq_figure(dq_df: pd.DataFrame | None) -> dict[str, Any] | None:
    if dq_df is None or dq_df.empty:
        return None
    fig = px.bar(
        dq_df,
        x="severity",
        y="issue_count",
        title="Data quality issues by severity (SQLite: dq_issues)",
        labels={"issue_count": "Count", "severity": "Severity"},
        color="severity",
        color_discrete_map={"critical": "#c0392b", "medium": "#e67e22", "low": "#27ae60"},
    )
    fig.update_layout(template=_PLOTLY_TEMPLATE, height=340, showlegend=False)
    return _fig_to_safe_dict(fig)


def compute_kpis(df: pd.DataFrame) -> dict[str, Any]:
    if df is None or df.empty:
        return {
            "total_revenue": 0.0,
            "sale_count": 0,
            "date_min": None,
            "date_max": None,
            "dealer_count": 0,
            "region_count": 0,
        }
    rev = pd.to_numeric(df["sale_price"], errors="coerce")
    return {
        "total_revenue": float(rev.sum()),
        "sale_count": int(len(df)),
        "date_min": df["sale_date"].min().strftime("%Y-%m-%d") if "sale_date" in df.columns else None,
        "date_max": df["sale_date"].max().strftime("%Y-%m-%d") if "sale_date" in df.columns else None,
        "dealer_count": int(df["dealer_id"].nunique()) if "dealer_id" in df.columns else 0,
        "region_count": int(df["region"].nunique()) if "region" in df.columns else 0,
    }
