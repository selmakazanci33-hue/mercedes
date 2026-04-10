from __future__ import annotations

import html as html_lib
from dataclasses import dataclass
from typing import Any

import pandas as pd

from services.dashboard_charts import _dealer_subset_for_charts


def _esc(x: Any) -> str:
    return html_lib.escape(str(x))


def _money(v: float) -> str:
    return f"${v:,.0f}"


def _month_label(ts: pd.Timestamp) -> str:
    return ts.strftime("%b %Y")


def build_dashboard_narratives(
    df: pd.DataFrame | None,
    *,
    top_n_dealers: int | None = None,
) -> dict[str, str]:
    """
    HTML snippets (safe for Jinja |safe) with analytics below each chart.
    Mirrors the same logic as build_dashboard_figures (dealer subset).
    """
    empty = "<p class='muted'>Run ETL and open this page again when <code>clean_sales</code> has rows.</p>"
    if df is None or df.empty:
        return {k: empty for k in _keys()}

    d = df.copy()
    d["revenue"] = pd.to_numeric(d["sale_price"], errors="coerce")
    d = d.dropna(subset=["revenue"])
    d["sale_date"] = pd.to_datetime(d["sale_date"], errors="coerce")
    d = d.dropna(subset=["sale_date"])
    d["day"] = d["sale_date"].dt.floor("D")
    d["month_period"] = d["sale_date"].dt.to_period("M").dt.to_timestamp()

    dealer_label = "dealer_name" if "dealer_name" in d.columns and d["dealer_name"].notna().any() else "dealer_id"
    sub, dealer_scope = _dealer_subset_for_charts(d, dealer_label, top_n_dealers)

    out: dict[str, str] = {}
    out["daily_total"] = _narrative_daily_total(d)
    out["daily_by_region"] = _narrative_daily_by_region(d)
    out["daily_by_dealer"] = _narrative_daily_by_dealer(sub, dealer_label, dealer_scope)
    out["monthly_total"] = _narrative_monthly_total(d)
    out["monthly_by_region"] = _narrative_monthly_by_region(d)
    out["monthly_by_dealer"] = _narrative_monthly_by_dealer(sub, dealer_label, dealer_scope)
    return out


def _keys() -> list[str]:
    return [
        "daily_total",
        "daily_by_region",
        "daily_by_dealer",
        "monthly_total",
        "monthly_by_region",
        "monthly_by_dealer",
    ]


def _narrative_daily_total(d: pd.DataFrame) -> str:
    daily = d.groupby("day", as_index=False)["revenue"].sum().sort_values("day")
    if daily.empty:
        return "<p>No daily totals.</p>"
    best = daily.loc[daily["revenue"].idxmax()]
    worst = daily.loc[daily["revenue"].idxmin()]
    med = float(daily["revenue"].median())
    worst_pct_med = (float(worst["revenue"]) / med * 100) if med > 0 else 0.0

    monthly = d.groupby("month_period", as_index=False)["revenue"].sum().sort_values("month_period")
    top_m = monthly.nlargest(3, "revenue")
    bot_m = monthly.nsmallest(3, "revenue")
    mom = monthly["revenue"].pct_change().dropna()
    worst_mom_idx = mom.idxmin() if len(mom) else None
    best_mom_idx = mom.idxmax() if len(mom) else None
    worst_mom = float(mom.min()) if len(mom) else None
    best_mom = float(mom.max()) if len(mom) else None

    parts: list[str] = []
    parts.append(
        "<p><strong>Daily total revenue</strong> sums every sale in the dataset per calendar day. "
        "Use it to spot lumpiness (single-day spikes or troughs) before interpreting dealer or region charts.</p>"
    )
    parts.append(
        f"<p><strong>Peak day:</strong> {_esc(best['day'].date())} at <strong>{_money(float(best['revenue']))}</strong>. "
        f"<strong>Weakest day:</strong> {_esc(worst['day'].date())} at <strong>{_money(float(worst['revenue']))}</strong> "
        f"(about <strong>{worst_pct_med:.0f}%</strong> of the median daily total of <strong>{_money(med)}</strong>).</p>"
    )
    if worst_pct_med < 25:
        parts.append(
            "<p><strong>Critical:</strong> The weakest day is far below a “typical” day — validate whether that reflects "
            "<strong>closed stores</strong>, <strong>reporting cutoff</strong>, or <strong>sparse synthetic data</strong> before blaming demand.</p>"
        )

    parts.append("<p><strong>Strong months (top 3 by total revenue):</strong></p><ul>")
    for _, r in top_m.iterrows():
        parts.append(
            f"<li><strong>{_month_label(r['month_period'])}</strong>: {_money(float(r['revenue']))} — candidate to study what worked (mix, campaigns, rates).</li>"
        )
    parts.append("</ul>")

    parts.append("<p><strong>Soft months (bottom 3 — consider tests or promotions):</strong></p><ul>")
    for _, r in bot_m.iterrows():
        parts.append(f"<li><strong>{_month_label(r['month_period'])}</strong>: {_money(float(r['revenue']))}</li>")
    parts.append("</ul>")

    if worst_mom is not None and worst_mom_idx is not None:
        mlab = _month_label(monthly.loc[worst_mom_idx, "month_period"])
        parts.append(
            f"<p><strong>Largest month-over-month drop:</strong> <strong>{mlab}</strong> "
            f"(about <strong>{worst_mom * 100:.1f}%</strong> vs prior month). "
            f"<strong>Largest MoM gain:</strong> about <strong>{best_mom * 100:.1f}%</strong> "
            f"({_month_label(monthly.loc[best_mom_idx, 'month_period']) if best_mom_idx is not None else 'n/a'}).</p>"
        )

    parts.append(
        "<p><em>Promotion idea:</em> Pilot extra demand gen in the <strong>lowest-revenue months</strong> above; "
        "confirm with inventory and rate programs so discounts do not erode margin.</p>"
    )
    return "\n".join(parts)


def _narrative_daily_by_region(d: pd.DataFrame) -> str:
    if "region" not in d.columns or d["region"].isna().all():
        return "<p><strong>Region</strong> is missing from the join — check <code>clean_dealers</code>.</p>"

    reg_tot = d.groupby("region", dropna=False)["revenue"].sum().sort_values(ascending=False)
    daily_reg = d.groupby(["day", "region"], as_index=False)["revenue"].sum()
    cv_rows: list[tuple[str, float, float]] = []
    for reg in reg_tot.index:
        sub = daily_reg[daily_reg["region"] == reg]["revenue"]
        if len(sub) == 0:
            continue
        mu = float(sub.mean())
        sd = float(sub.std(ddof=0))
        cv = sd / mu if mu > 0 else 0.0
        cv_rows.append((str(reg), float(reg_tot.loc[reg]), cv))
    cv_rows.sort(key=lambda x: -x[2])

    best_reg = reg_tot.index[0]
    worst_reg = reg_tot.index[-1]
    high_vol = [x[0] for x in cv_rows[:2]]

    parts: list[str] = []
    parts.append(
        "<p><strong>Daily revenue by region</strong> shows which regions drive each day’s total. "
        "Compare <strong>level</strong> (cumulative strength) vs <strong>volatility</strong> (day-to-day noise).</p>"
    )
    parts.append(
        f"<p><strong>Highest cumulative revenue:</strong> <strong>{_esc(best_reg)}</strong> "
        f"({_money(float(reg_tot.iloc[0]))}). "
        f"<strong>Lowest cumulative revenue:</strong> <strong>{_esc(worst_reg)}</strong> "
        f"({_money(float(reg_tot.iloc[-1]))}).</p>"
    )
    parts.append(
        f"<p><strong>Highest daily volatility (CV of daily regional totals):</strong> "
        f"<strong>{', '.join(_esc(h) for h in high_vol)}</strong> — short windows can look “worse” here even when annual totals are fine. "
        f"Use <strong>rolling 7-day</strong> views for decisions.</p>"
    )
    parts.append(
        "<p><strong>Critical attention</strong> if a region combines <strong>low cumulative revenue</strong> with "
        "<strong>high volatility</strong>: prioritize <strong>data quality</strong>, then <strong>inventory</strong> and "
        "<strong>incentive alignment</strong> vs peers.</p>"
    )
    parts.append(
        "<p><strong>Doing well:</strong> regions near the top on <strong>total revenue</strong> with stable daily patterns — "
        "export playbooks to laggard regions after validating mix (models, financing).</p>"
    )
    return "\n".join(parts)


def _narrative_daily_by_dealer(sub: pd.DataFrame, dealer_label: str, dealer_scope: str) -> str:
    by_d = sub.groupby(dealer_label, as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    if by_d.empty:
        return "<p>No dealer series.</p>"
    top3 = by_d.head(3)
    bot3 = by_d.tail(3)
    parts: list[str] = []
    parts.append(
        f"<p>Scope: <strong>{_esc(dealer_scope)}</strong> (matches the chart). "
        "Lines are daily revenue per dealer — gaps between lines are <strong>level</strong> differences; crossovers are normal.</p>"
    )
    parts.append("<p><strong>Top dealers by total revenue in this view:</strong></p><ul>")
    for _, r in top3.iterrows():
        parts.append(
            f"<li><strong>{_esc(r[dealer_label])}</strong>: {_money(float(r['revenue']))} cumulative in period</li>"
        )
    parts.append("</ul>")
    parts.append("<p><strong>Need careful review (lowest in this view):</strong></p><ul>")
    for _, r in bot3.iterrows():
        parts.append(
            f"<li><strong>{_esc(r[dealer_label])}</strong>: {_money(float(r['revenue']))} — check <strong>volume</strong> (sale count) vs <strong>ticket</strong> in the dealer table.</li>"
        )
    parts.append("</ul>")
    parts.append(
        "<p><strong>Critical:</strong> If bottom dealers also show <strong>fewer transactions</strong> (not just lower price), "
        "prioritize <strong>pipeline / foot traffic</strong> and <strong>allocation</strong> before price cuts.</p>"
    )
    return "\n".join(parts)


def _narrative_monthly_total(d: pd.DataFrame) -> str:
    monthly = d.groupby("month_period", as_index=False)["revenue"].sum().sort_values("month_period")
    if monthly.empty:
        return "<p>No monthly totals.</p>"
    top3 = monthly.nlargest(3, "revenue")
    bot3 = monthly.nsmallest(3, "revenue")
    mom = monthly["revenue"].pct_change()
    parts: list[str] = []
    parts.append(
        "<p><strong>Monthly total revenue</strong> removes daily noise — use it for <strong>seasonality</strong> and "
        "<strong>promotion timing</strong> (stack with inventory and rate sheets).</p>"
    )
    parts.append("<p><strong>Best months (candidates to mirror / extend successful tactics):</strong></p><ul>")
    for _, r in top3.iterrows():
        parts.append(f"<li><strong>{_month_label(r['month_period'])}</strong>: {_money(float(r['revenue']))}</li>")
    parts.append("</ul>")
    parts.append("<p><strong>Weakest months (candidates for targeted promos or demand tests):</strong></p><ul>")
    for _, r in bot3.iterrows():
        parts.append(f"<li><strong>{_month_label(r['month_period'])}</strong>: {_money(float(r['revenue']))}</li>")
    parts.append("</ul>")
    if len(mom.dropna()) > 0:
        idx_min = mom.idxmin()
        idx_max = mom.idxmax()
        parts.append(
            f"<p><strong>Largest MoM decline:</strong> into <strong>{_month_label(monthly.loc[idx_min, 'month_period'])}</strong> "
            f"({mom.loc[idx_min] * 100:.1f}%). "
            f"<strong>Largest MoM gain:</strong> into <strong>{_month_label(monthly.loc[idx_max, 'month_period'])}</strong> "
            f"({mom.loc[idx_max] * 100:.1f}%).</p>"
        )
    return "\n".join(parts)


def _narrative_monthly_by_region(d: pd.DataFrame) -> str:
    if "region" not in d.columns or d["region"].isna().all():
        return "<p>Region not available.</p>"
    mr = d.groupby(["month_period", "region"], as_index=False)["revenue"].sum()
    pivot = mr.pivot_table(index="month_period", columns="region", values="revenue", aggfunc="sum").fillna(0)
    # Latest month leader
    last_m = pivot.index.max()
    if pd.isna(last_m):
        return "<p>No monthly regional data.</p>"
    last_row = pivot.loc[last_m].sort_values(ascending=False)
    leader = last_row.index[0]
    trailer = last_row.index[-1]

    reg_full = d.groupby("region")["revenue"].sum().sort_values(ascending=False)
    parts: list[str] = []
    parts.append(
        "<p><strong>Stacked monthly revenue by region</strong> shows <strong>mix over time</strong>: who contributes each month. "
        "Watch for a region that <strong>shrinks share</strong> for multiple consecutive months.</p>"
    )
    parts.append(
        f"<p><strong>Latest month ({_month_label(last_m)}) — highest slice:</strong> <strong>{_esc(leader)}</strong> "
        f"({_money(float(last_row.loc[leader]))}); "
        f"<strong>lowest slice:</strong> <strong>{_esc(trailer)}</strong> "
        f"({_money(float(last_row.loc[trailer]))}).</p>"
    )
    parts.append(
        f"<p><strong>Full-period regional totals:</strong> strongest <strong>{_esc(reg_full.index[0])}</strong> "
        f"({_money(float(reg_full.iloc[0]))}); "
        f"weakest <strong>{_esc(reg_full.index[-1])}</strong> "
        f"({_money(float(reg_full.iloc[-1]))}).</p>"
    )
    parts.append(
        "<p><strong>Critical:</strong> If one region’s <strong>stack shrinks</strong> while others grow, investigate "
        "<strong>inventory availability</strong>, <strong>local incentives</strong>, and <strong>competitive pressure</strong> — not only “sales effort.”</p>"
    )
    return "\n".join(parts)


def _narrative_monthly_by_dealer(sub: pd.DataFrame, dealer_label: str, dealer_scope: str) -> str:
    md = sub.groupby(["month_period", dealer_label], as_index=False)["revenue"].sum()
    if md.empty:
        return "<p>No monthly dealer data.</p>"
    last_m = md["month_period"].max()
    prev_m = md[md["month_period"] < last_m]["month_period"].max()
    parts: list[str] = []
    parts.append(
        f"<p><strong>Grouped monthly bars</strong> — scope: <strong>{_esc(dealer_scope)}</strong>. "
        "Compare <strong>bar height trends</strong> month to month for the same dealer.</p>"
    )
    last = md[md["month_period"] == last_m].sort_values("revenue", ascending=False)
    parts.append(f"<p><strong>Latest month ({_month_label(last_m)}) — top contributors:</strong></p><ul>")
    for _, r in last.head(5).iterrows():
        parts.append(f"<li><strong>{_esc(r[dealer_label])}</strong>: {_money(float(r['revenue']))}</li>")
    parts.append("</ul>")
    if pd.notna(prev_m):
        p1 = md[md["month_period"] == last_m].set_index(dealer_label)["revenue"]
        p0 = md[md["month_period"] == prev_m].set_index(dealer_label)["revenue"]
        common = p1.index.intersection(p0.index)
        if len(common) > 0:
            chg = (p1.loc[common] - p0.loc[common]) / p0.loc[common].replace(0, float("nan"))
            chg = chg.dropna().sort_values()
            if len(chg) > 0:
                worst_d = chg.index[0]
                best_d = chg.index[-1]
                parts.append(
                    f"<p><strong>MoM change {_month_label(prev_m)} → {_month_label(last_m)}:</strong> "
                    f"largest decline <strong>{_esc(worst_d)}</strong> ({chg.loc[worst_d] * 100:.1f}%); "
                    f"largest gain <strong>{_esc(best_d)}</strong> ({chg.loc[best_d] * 100:.1f}%).</p>"
                )
    parts.append(
        "<p><strong>Critical:</strong> A dealer’s bar <strong>collapsing</strong> for one month may be "
        "<strong>allocation</strong> or <strong>stockout</strong> — pair with <strong>Inventory</strong> sheet before concluding performance failure.</p>"
    )
    return "\n".join(parts)


@dataclass(frozen=True)
class ChecklistSection:
    title: str
    items: list[str]


def build_dashboard_checklist() -> list[ChecklistSection]:
    """
    Structured questions for criteria, ownership, missing data, and improvements.
    """
    return [
        ChecklistSection(
            title="What defines “good” results?",
            items=[
                "Is the target based on <strong>revenue</strong>, <strong>units</strong>, <strong>margin</strong>, or <strong>market share</strong>?",
                "Should we judge performance vs <strong>prior year</strong>, <strong>forecast</strong>, or <strong>peer dealers/regions</strong>?",
                "What is an acceptable <strong>variance band</strong> for monthly revenue (e.g. ±X%) given seasonality?",
            ],
        ),
        ChecklistSection(
            title="Drivers: sales team vs region vs programs",
            items=[
                "How much of the gap is explained by <strong>lead volume</strong> vs <strong>close rate</strong> (sales process)?",
                "Which outcomes are driven by <strong>regional demand</strong>, <strong>competitor intensity</strong>, or <strong>inventory availability</strong>?",
                "How do <strong>OEM incentives</strong>, <strong>APR programs</strong>, and <strong>lease vs finance mix</strong> change the revenue story?",
                "Are <strong>fleet / corporate</strong> sales excluded or included in this dataset?",
            ],
        ),
        ChecklistSection(
            title="Promotions and timing",
            items=[
                "Which <strong>months</strong> underperformed vs forecast — were <strong>promotions</strong> planned there?",
                "Do we have <strong>promotion calendar</strong> and <strong>spend</strong> joined to sales dates?",
                "Should weak months get <strong>pull-forward</strong> campaigns or <strong>margin-preserving</strong> bundles instead of discounts?",
            ],
        ),
        ChecklistSection(
            title="Other services & cross-sell",
            items=[
                "Are <strong>F&amp;I / warranty / service</strong> revenues in scope — if not, are we over-weighting front-end price?",
                "Does <strong>delivery timing</strong> shift revenue across months (pipeline vs recognized revenue)?",
            ],
        ),
        ChecklistSection(
            title="Missing criteria — how to handle",
            items=[
                "If <strong>margin</strong> is missing, should revenue charts be paired with <strong>minimum margin guardrails</strong>?",
                "If <strong>inventory</strong> is not joined, flag <strong>stockout risk</strong> before blaming dealers.",
                "If <strong>rates</strong> are not aligned to sale month, treat finance-led conclusions as <strong>hypotheses</strong> only.",
                "Document <strong>assumptions</strong> when imputing missing fields (e.g. region from dealer master only).",
            ],
        ),
        ChecklistSection(
            title="Missing columns that hurt prediction / forecasting",
            items=[
                "<strong>Vehicle / trim / option</strong> mix — needed for price and margin explanation.",
                "<strong>Channel</strong> (walk-in vs digital) — needed for sales-process attribution.",
                "<strong>Competitive price index</strong> — needed for regional pricing pressure.",
                "<strong>Incentive cost</strong> — needed to separate volume from profitability.",
                "<strong>Order vs delivery date</strong> — needed to align revenue recognition.",
                "<strong>Returns / cancellations</strong> — needed for net demand.",
            ],
        ),
        ChecklistSection(
            title="What looks positive vs what to improve",
            items=[
                "<strong>Positive:</strong> Clear daily and monthly seasonality patterns; strong peer dealers for benchmarking.",
                "<strong>Improve:</strong> Add <strong>forecast vs actual</strong> and <strong>inventory</strong> overlays on the same time axis.",
                "<strong>Improve:</strong> Add <strong>DQ thresholds</strong> (e.g. block charts if critical keys missing).",
                "<strong>Improve:</strong> Standardize <strong>promotion</strong> and <strong>rate</strong> dimensions for causal review.",
            ],
        ),
    ]
