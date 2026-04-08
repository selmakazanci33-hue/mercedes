Build a complete Flask-based pricing analytics and file-based ETL project for a Mercedes-Benz USA business case study.

Context:
This project is for a pricing analytics / financial services case study. The goal is not just to analyze data, but to demonstrate structured thinking, pricing logic, forecasting awareness, data quality ownership, ETL design, and business insight generation.

I will provide reference files, including:
- Excel dataset with multiple sheets/tables
- case study instruction documents
- job description / role context documents

Use all provided files as the source of truth and build the project around them.

==================================================
BUSINESS CASE CONTEXT
==================================================

Leadership has observed:
- inconsistent dealer pricing behavior
- regional performance differences
- forecast variance

The provided dataset includes these logical tables:
- Dealers: dealer_id, dealer_name, region
- Models: model_code, model_name, segment
- Inventory: dealer_id, model_code, on_hand
- Sales: sale_id, sale_date, dealer_id, model_code, sale_price
- Interest_Rates:
  month, region, model_code, product_type, term_months, credit_tier,
  buy_rate_apr, published_apr, money_factor, residual_pct
- Forecast_Assumptions:
  month, region, model_code, units_forecast, avg_price_assumption, apr_assumption

The project must cover both:
1. what the business case explicitly asks for
2. additional value-added analysis such as data quality, visibility gaps, ETL design, and scalable analytics workflow

==================================================
HIGH-LEVEL GOAL
==================================================

Create a Flask application that:
- reads the real Excel data
- performs a file-based ETL pipeline
- cleans and validates the data
- loads the processed data into a database
- supports incremental load logic
- creates curated analytical outputs
- provides dashboards and downloadable files
- highlights early findings, anomalies, assumptions, risks, and next steps
- demonstrates business-facing analytics and data-engineering thinking together

==================================================
TECHNICAL STACK
==================================================

Use:
- Python
- Flask
- pandas
- SQLAlchemy
- SQLite by default (but structure code so PostgreSQL can be used later)
- Plotly for charts
- openpyxl for Excel reading/writing
- Jinja templates for HTML pages
- modular project structure
- environment variables/config file where useful

==================================================
PROJECT REQUIREMENTS
==================================================

Build the project in a clean, production-style modular structure.

Suggested structure:
- app.py
- config.py
- requirements.txt
- README.md
- /data
- /uploads
- /exports
- /logs
- /templates
- /static
- /etl
- /services
- /models
- /routes
- /utils
- /sql

==================================================
ETL PIPELINE REQUIREMENTS
==================================================

Implement a file-based ETL pipeline with these layers:

1. RAW LAYER
- Read all Excel sheets as raw tables
- Preserve original columns
- Save raw copies to the database
- Log row counts per source

2. CLEAN / TRANSFORM LAYER
- Standardize column names
- Strip whitespace
- Normalize string values
- Parse date fields
- Create derived month fields from sale_date
- Validate numeric columns
- Handle missing values
- Remove or flag duplicates
- Validate business keys and referential integrity

3. CURATED LAYER
Create curated analytical tables/views such as:
- sales_enriched
- inventory_enriched
- monthly_sales_summary
- dealer_performance_summary
- regional_performance_summary
- model_performance_summary
- pricing_variance_summary
- forecast_vs_actual_summary
- inventory_vs_sales_summary
- interest_rate_effect_summary
- data_quality_summary

4. LOAD LAYER
- Load processed outputs into a relational database
- Keep raw and curated tables separate
- Use SQLAlchemy models or clear SQL scripts

==================================================
INCREMENTAL LOAD REQUIREMENTS
==================================================

Implement incremental load logic for sales and other appendable datasets.

Examples:
- use sale_id as unique incremental business key for Sales
- if monthly snapshots are used, combine month + region + model_code + product_type + term_months + credit_tier as appropriate
- avoid duplicate inserts
- allow reruns safely
- support idempotent ETL execution
- maintain ETL metadata/audit table such as:
  - pipeline_run_id
  - run_timestamp
  - source_file_name
  - table_name
  - raw_row_count
  - clean_row_count
  - inserted_count
  - updated_count
  - rejected_count
  - status
  - error_message

==================================================
DATA QUALITY / VISIBILITY REQUIREMENTS
==================================================

This is critical. Build a strong data quality framework, not just simple cleaning.

The app must identify and report:
- missing critical fields
- incomplete records
- duplicate records
- invalid dates
- invalid numeric values
- broken joins / orphan keys
- inconsistent region or model mapping
- conditional completeness issues
- suspicious outliers
- records that reduce business visibility

Critical examples:
- missing dealer_id
- missing model_code
- missing sale_date
- missing sale_price
- missing region
- incomplete sales rows
- interest rate rows where finance records are missing APR values
- lease rows where money_factor or residual_pct is missing
- forecast rows with invalid assumptions

Create a data quality scoring/reporting mechanism:
- column-level missing %
- table-level quality score
- critical vs medium vs low severity issues
- recommended action
- business impact description

Include “visibility blockers” analysis:
Identify fields/data gaps that limit clear business insight, such as:
- inability to analyze regional trends due to missing region
- inability to analyze monthly growth due to missing sale_date
- inability to compare pricing due to missing model or dealer data
- inability to evaluate finance/lease performance due to missing product attributes

==================================================
BUSINESS ANALYSIS REQUIREMENTS
==================================================

The project must produce early findings aligned with the business case.

Include analysis for:

1. Dealer Performance
- total sales count by dealer
- total revenue by dealer
- average sale price by dealer
- monthly sales trend by dealer
- monthly growth by dealer
- top dealers by sales volume
- top dealers by revenue
- top dealers by growth

2. Regional Performance
- total sales by region
- total revenue by region
- average sale price by region
- monthly growth by region
- regional pricing differences
- regional performance differences

3. Model Performance
- top-selling models
- model performance by region
- model performance by dealer
- average price by model
- model inventory vs sales relationship

4. Pricing Consistency / Dealer Pricing Behavior
- compare same model across different dealers
- detect price variance across dealers and regions
- identify unusually high or low pricing
- surface inconsistent dealer pricing behavior
- create pricing variance charts and summary tables

5. Finance / Lease / Rate Impact
- analyze interest rates by month, region, model, product type, term, and credit tier
- compare finance vs lease structures
- examine possible relationship between APR assumptions/rates and actual sales behavior
- highlight whether financing programs may influence performance
- clearly distinguish finance-only and lease-only metrics

6. Forecast Variance
- compare forecast units vs actual sales units
- compare forecast average price assumption vs actual average sale price
- compare forecast APR assumption vs actual available rate context where possible
- calculate variance metrics
- identify where forecast assumptions diverge from actual behavior

7. Inventory vs Demand
- compare on_hand inventory against actual sales
- identify overstock and understock situations
- highlight possible missed opportunities
- highlight possible slow-moving inventory
- identify inventory-demand mismatch by dealer, region, and model

==================================================
ANOMALIES / HYPOTHESES / RISKS
==================================================

Generate business-friendly findings sections such as:
- early trends
- anomalies
- hypotheses
- assumptions
- risks
- open questions
- next steps if more time were available

Examples:
- same model priced differently across dealers
- forecast does not align with actual sales patterns
- some regions appear stronger/weaker than expected
- inventory levels do not align with sales demand
- financing structure may be affecting purchasing behavior
- data quality issues may distort conclusions

==================================================
FLASK APP FEATURES
==================================================

Create a usable Flask web application with pages/routes such as:

1. Home / Project Overview
- describe project purpose
- summarize loaded files
- show ETL status
- show latest pipeline run timestamp

2. Upload / Data Load Page
- upload Excel/reference files
- trigger ETL pipeline manually
- show ETL logs and results

3. Data Quality Dashboard
- table-level quality summary
- issue counts by severity
- missing values heatmap/table
- broken joins/orphan rows report
- visibility blockers section
- downloadable CSV/Excel report

4. Executive Analytics Dashboard
- KPI cards
- dealer performance charts
- regional performance charts
- pricing variance charts
- finance/lease charts
- forecast vs actual charts
- inventory vs demand charts
- Plotly interactive visuals

5. Detail Pages
- dealer detail page
- region detail page
- model detail page
- forecast detail page
- pricing detail page

6. Findings / Notes Page
- early findings
- assumptions
- risks
- open questions
- recommended next steps
- interview-ready summary bullets

7. Export Page
- export cleaned tables
- export curated tables
- export validation reports
- export findings summary
- export Excel workbook with multiple sheets

==================================================
OUTPUT / EXPORT REQUIREMENTS
==================================================

Generate exportable files such as:
- cleaned Excel workbook
- CSV extracts
- validation report
- data quality report
- early findings summary
- assumptions_and_open_questions file
- curated tables exports

Also generate a “working file” style output that matches case-study expectations:
- analyst-friendly tables
- summary tabs
- findings notes
- not overly polished, but clearly structured

==================================================
DATABASE DESIGN REQUIREMENTS
==================================================

Create a normalized but practical schema.

Include tables like:
- raw_dealers
- raw_models
- raw_inventory
- raw_sales
- raw_interest_rates
- raw_forecast_assumptions

- clean_dealers
- clean_models
- clean_inventory
- clean_sales
- clean_interest_rates
- clean_forecast_assumptions

- dq_issues
- etl_audit_log
- curated summaries / materialized tables as needed

Also create useful SQL views such as:
- vw_sales_enriched
- vw_monthly_sales
- vw_dealer_growth
- vw_regional_growth
- vw_forecast_vs_actual
- vw_inventory_vs_sales
- vw_pricing_variance
- vw_finance_lease_summary

==================================================
LOGGING / ERROR HANDLING
==================================================

Add proper logging:
- pipeline start/end
- row counts
- failures
- rejected records
- validation warnings

Handle failures gracefully:
- invalid sheet names
- missing columns
- empty files
- data type issues
- duplicate keys
- inconsistent schemas

==================================================
INTERVIEW / BUSINESS COMMUNICATION SUPPORT
==================================================

This project is also meant to help present findings in a 30-minute case-study discussion.

Generate a business summary that helps answer:
- How the dataset was approached
- Where analysis started
- Early trends, patterns, anomalies, or hypotheses
- Questions, assumptions, and risks identified
- How ambiguity or data gaps were handled
- What would be focused on next with more time

Create concise, interview-friendly notes in plain business language.

==================================================
WHAT TO BUILD NOW
==================================================

Please generate:

1. Complete Flask app code
2. ETL modules and data processing logic
3. Database models and initialization
4. Plotly dashboards
5. Data quality framework
6. Incremental load framework
7. Export functionality
8. README with setup and run instructions
9. requirements.txt
10. sample config/env guidance
11. comments in code explaining important logic
12. sensible defaults for local execution

==================================================
CODING STYLE
==================================================

- Write clean, modular, readable Python
- Use functions and classes where appropriate
- Add docstrings
- Add inline comments for important business logic
- Keep naming consistent
- Make the project runnable locally
- Prefer maintainability over cleverness
- Separate ETL, analytics, routes, templates, and utilities cleanly

==================================================
IMPORTANT BUSINESS EMPHASIS
==================================================

Do not build only a technical ETL.
The final solution must demonstrate:
- pricing analytics thinking
- forecasting awareness
- dealer/regional performance insight
- finance/lease context
- inventory vs demand logic
- data quality ownership
- clear communication of assumptions and risks

The solution should feel like a strong case-study project for a Senior Analyst / Pricing Analytics / Financial Services role.

At the end, provide:
- final project structure
- full code files
- setup steps
- how to run the app
- how to upload the dataset
- how to trigger ETL
- how to view dashboards
- how to export outputs