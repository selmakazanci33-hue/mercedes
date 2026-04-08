# Mercedes Pricing Analytics (Flask + ETL + DQ + Plotly + SQLite)

This repo is a **file-based analytics + data-quality pipeline** wrapped in a **Flask app**.

## Quickstart

Create a virtualenv, then:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set env vars (optional; defaults work locally):

```bash
cp .env.example .env
```

Run the web app:

```bash
python app.py
```

## Load data

1. Put your Excel dataset in `uploads/` (or upload via the UI).
2. Go to `Upload & Run ETL` and trigger the pipeline.

The pipeline will:
- **retrieve**: read the Excel sheets into raw tables
- **clean**: standardize columns, types, key fields, missing values
- **validate**: create a data quality report (issues + severity + business impact)
- **curate**: build analytical summary tables/views
- **load**: write to SQLite with **idempotent / incremental** logic (where keys exist)

## Output artifacts

- SQLite DB: `data/app.db`
- Exports: `exports/` (CSV extracts + data-quality report)
- Logs: `logs/app.log`

## Project layout (high level)

- `app.py`: Flask entrypoint
- `app/`: Flask app factory, routes, templates wiring
- `etl/`: raw → clean → validate → curated → load pipeline
- `models/`: SQLAlchemy models (audit + DQ + curated tables)
- `services/`: reusable services (db, exports, plotting)
- `sql/`: views and helper SQL
- `uploads/`: source files you upload
- `data/`: SQLite database lives here

## Notes

The repository is structured so SQLite is the default but the DB URL can be swapped later.
