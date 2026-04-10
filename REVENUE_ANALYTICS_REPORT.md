# Revenue analytics report — regions & dealers

**Source:** `Pricing Analytics Business Case data vfinal.xlsx` (sheets: Sales, Dealers; other sheets not required for this revenue view).  
**Scope:** 5,000 sales rows, 20 dealers, 4 regions (East, Midwest, South, West), sale dates from **2024-01-01** through **2025-12-31**.  
**Metric:** Revenue = sum of `sale_price`. Region and dealer name come from the **Dealers** sheet joined on `dealer_id`.

---

## Executive summary

- **Regions are tightly clustered** in total revenue over the full period: **West** leads slightly (~$57.5M), then East, Midwest, and South within a narrow band (~$55–57M each). There is **no single “failing” region** on a cumulative basis; differences are modest and warrant **peer benchmarking** more than crisis framing.
- **Dealer spread is also compressed**: the highest dealer is only about **1.16–1.21×** the lowest dealer *within the same region* on total revenue, while national rank spans **#1 (Dealer 312)** to **#20 (Dealer 318)**. The clearest “gap” story is **volume** (number of sales) and **consistency** (daily volatility), not catastrophic underperformance.
- **Dealers doing especially well (national total revenue):** **312, 303, 315, 309, 310** — top five, each above ~$11.8M cumulative.
- **Dealers warranting careful review:** **317, 318, 308, 305, 302** — lowest cumulative revenue and/or meaningfully **fewer transactions** than top peers (see §4).
- **Operational / data-quality red flag:** A single **worst day** total revenue (**$37,774** on **2024-08-09**) vs a **best day** (**$685,781** on **2025-03-26**) implies **heavy daily lumpiness**. That is either real seasonality/promotions or **sparse coverage** on some calendar days — worth validating before attributing performance to dealers or regions.

---

## 1. Methodology (short)

| Step | Detail |
|------|--------|
| Join | `Sales` ⟕ `Dealers` on `dealer_id` (string-normalized). |
| Daily | `sale_date` truncated to calendar day; revenue summed per day (overall and by region in analysis scripts). |
| Monthly | Calendar month start (`Period('M')`). |
| Total | Full date range above. |
| Volatility proxy | Coefficient of variation (CV) of **daily** regional totals: `std/mean` across days with sales in that region. |

---

## 2. Regional performance

### 2.1 Total revenue by region (full period)

| Region  | Total revenue | Share of national (~$224.7M) |
|---------|----------------:|-------------------------------:|
| **West**   | $57,540,724.88 | ~25.6% |
| **East**   | $56,665,405.47 | ~25.2% |
| **Midwest**| $55,468,806.23 | ~24.7% |
| **South**  | $54,980,829.54 | ~24.5% |

**Interpretation:** **West** is the **largest cumulative region** by a **small margin** (~1.0% more than South). **South** is **last on total revenue** but still within **~4.7%** of West — so “South is failing” would be **overstated** without deeper mix (models, financing, inventory) and statistical testing.

### 2.2 Year-over-year split (calendar year totals)

| Year | East | Midwest | South | West |
|------|-----:|--------:|------:|-----:|
| **2024** | $28,425,803 | $28,364,561 | $27,289,078 | $29,824,344 |
| **2025** | $28,239,602 | $27,104,245 | $27,691,751 | $27,716,381 |

**Signals:**

- **West:** **Down** materially **2024 → 2025** (~**−7.1%** in nominal regional total). That is the **largest regional swing** in this cut and deserves **careful consideration** (mix shift, rate programs, dealer execution, or data generation rules in the synthetic workbook).
- **Midwest:** **Down ~4.4%** 2024 vs 2025 — second-largest decline; monitor whether **H2 2025** recovery (see monthly) sustains.
- **South:** **Up ~1.5%** — modest positive momentum vs prior year.
- **East:** **Roughly flat** (~**−0.7%**) — stable share story.

### 2.3 Monthly pattern (high level)

Early 2024 shows **strong March** activity in **South** (notably high March 2024 vs other regions in the same month). Recent months (Oct–Dec 2025) show **Midwest** finishing **strong in December** and **South** spiking in **November** — month-to-month **crossovers** between regions are common, which again points to **volatile monthly revenue** rather than a single dominant region every month.

**Largest single-month national swing (month-over-month % change):** about **+20.8%** (peak month) and about **−21.1%** (trough month). That magnitude suggests **high month-to-month variance**; regional narratives should use **rolling averages** or **quarterly** cuts alongside raw months.

### 2.4 Daily volatility by region (CV of daily regional totals)

Higher CV ⇒ more **day-to-day lumpiness** in recorded regional revenue.

| Region  | CV (approx.) |
|---------|-------------:|
| **South**  | **0.582** |
| **East**   | **0.576** |
| **Midwest**| **0.553** |
| **West**   | **0.538** |

**Interpretation:** **South** and **East** show the **highest daily volatility**. That does not mean they are “worse,” but it does mean **short-window dashboards** can mislead; **West** is comparatively **smoother** day-to-day in this dataset. Combine with **inventory** and **rate** sheets before concluding demand weakness.

### 2.5 Where the “gaps” are (regions)

1. **West 2025 vs West 2024** — clearest **negative year shift**; prioritize **why volume/price mix moved** (dealer 303/315/307/311/319 contribution changes, model mix, incentives).
2. **South / East daily volatility** — prioritize **consistency** diagnostics (sparse sales days vs true closings, weekend effects, reporting cutoffs).
3. **Tight absolute spread** across regions on totals — **avoid over-rotating** on small rank-order differences without confidence intervals.

---

## 3. Daily revenue — what stands out

- **Best single day (national sum):** **2025-03-26** — **~$685,781** (possible campaign, quarter-end, or synthetic spike).
- **Worst single day (national sum):** **2024-08-09** — **~$37,775** (~**18×** gap vs best day).

**Careful considerations:**

- Validate whether **all dealers** report on the same clock and whether **zeros** are “no sales” vs “missing upload.”
- Use **7-day or 28-day rolling** revenue for management review; raw daily extremes will dominate narratives otherwise.

---

## 4. Dealer performance (total revenue & volume)

### 4.1 National ranking (full period)

| Rank | Dealer ID | Name | Region | Total revenue | Sales (n) | Avg ticket |
|-----:|----------|------|--------|---------------:|----------:|-----------:|
| 1 | 312 | MB Dealer 312 | East | $12,598,934.64 | 283 | ~$44,519 |
| 2 | 303 | MB Dealer 303 | West | $12,585,784.63 | 284 | ~$44,316 |
| 3 | 315 | MB Dealer 315 | West | $11,825,725.21 | 259 | ~$45,659 |
| 4 | 309 | MB Dealer 309 | South | $11,776,568.78 | 261 | ~$45,121 |
| 5 | 310 | MB Dealer 310 | Midwest | $11,759,702.26 | 259 | ~$45,404 |
| … | … | … | … | … | … | … |
| 16 | 302 | MB Dealer 302 | Midwest | $10,790,590.95 | 244 | ~$44,224 |
| 17 | 305 | MB Dealer 305 | South | $10,662,531.49 | 241 | ~$44,243 |
| 18 | 308 | MB Dealer 308 | East | $10,593,469.24 | 236 | ~$44,888 |
| 19 | 317 | MB Dealer 317 | South | $9,797,521.66 | **218** | ~$44,943 |
| 20 | 318 | MB Dealer 318 | Midwest | $9,679,179.00 | **213** | ~$45,442 |

### 4.2 Who is “doing great”

**National leaders (312, 303, 315, 309, 310)** combine **high revenue** with **transaction counts at or near the top of the peer set** (250–284 sales in this extract). **Average ticket** is in a **tight band** (~$44k–$46k) across most dealers, so **scale (volume)** is doing more of the ranking work than extreme pricing.

**Regional #1 dealers (by total revenue in region):**

| Region | Top dealer (ID) | Revenue (approx.) |
|--------|-----------------|--------------------:|
| East | **312** | $12,598,934.64 |
| West | **303** | $12,585,784.63 |
| South | **309** | $11,776,568.78 |
| Midwest | **310** | $11,759,702.26 |

These are the **clearest “bright spots”** within each region on a cumulative view.

### 4.3 Who needs careful consideration

**Lowest cumulative revenue:** **318 (Midwest)**, **317 (South)** — also the **lowest sales counts** (**213** and **218** vs **280+** for top dealers). That pattern suggests **throughput / demand capture** more than **pricing failure** (avg tickets remain similar).

**Next tier to watch (still bottom quartile nationally):** **308 (East)**, **305 (South)**, **302 (Midwest)** — revenue **~$10.6–10.8M** with **236–244** transactions; not catastrophic vs leaders, but **persistent gap** if the network expects more balanced throughput.

### 4.4 Within-region spread (top vs bottom dealer)

Approximate **top dealer share** of **regional** revenue is **~21–22%**; **bottom** is **~17–19%**. **Top/bottom revenue ratio within region** is only **~1.16–1.21×**. So **intra-region inequality is moderate**; the story is more about **who sits below the cluster** (317/318) than about a single dominant monopolist dealer.

---

## 5. Monthly revenue — how to read “gaps”

Because regions **trade ranks month to month**, a “monthly gap” should be defined explicitly, for example:

- **Gap vs trailing 3-month average** for each region.
- **Gap vs same month prior year** (YoY) — we already see **West** weaker in **2025** than **2024** at annual level; monthly drill-down would show *which months* drove that.

Without locking a single month as the “target,” the safest statements from this file are:

- **West** needs a **2025 recovery narrative** vs **2024**.
- **South** shows **higher daily volatility**; monthly charts should be interpreted with **smoothing**.

---

## 6. Recommended next steps (analytics + business)

1. **Dealer action list:** deep dive **317, 318** (volume shortfall), then **308, 305, 302** (mid-pack risk).
2. **Regional action list:** explain **West 2025 decline**; validate **South/East volatility** drivers (mix, incentives, reporting).
3. **Data validation:** investigate **2024-08-09** low national day and **2025-03-26** spike; confirm business meaning vs artifact.
4. **Enrich the story** using **Inventory**, **Interest_Rates**, and **Forecast_Assumptions** (not in this revenue-only report) to separate **demand** vs **supply** vs **program** effects.

---

## 7. Limitations

- This report is **descriptive** only (no causal inference, no hypothesis tests).
- **Average ticket** similarity suggests the workbook may be **partially synthesized**; treat findings as **case-study signals**, not audited financials.
- **Git** may ignore local copies of the workbook; the analysis assumes the **`Pricing Analytics Business Case data vfinal.xlsx`** file used here matches your current version.

---

*Generated from the workbook’s Sales + Dealers sheets: totals, ranks, YoY splits, daily extrema, regional daily CV, and month-over-month national swing.*
