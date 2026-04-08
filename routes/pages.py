from __future__ import annotations

import logging
import os
from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

from config import settings
from etl.pipeline import run_pipeline
from services.dashboard_charts import build_dashboard_figures, build_dq_figure, compute_kpis
from services.db import engine as db_engine, get_session
from services.repo import latest_pipeline_run
from services.sales_analytics import load_dq_summary, load_enriched_sales_from_sqlite


logger = logging.getLogger(__name__)
pages_bp = Blueprint("pages", __name__)


@pages_bp.get("/")
def home():
    with get_session() as session:
        latest = latest_pipeline_run(session)
    return render_template("home.html", latest=latest)


@pages_bp.route("/upload", methods=["GET", "POST"])
def upload_and_run():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part in request", "error")
            return redirect(url_for("pages.upload_and_run"))

        f = request.files["file"]
        if not f or f.filename is None or f.filename.strip() == "":
            flash("No file selected", "error")
            return redirect(url_for("pages.upload_and_run"))

        filename = secure_filename(f.filename)
        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        stored_name = f"{ts}__{filename}"
        path = os.path.join(settings.upload_folder, stored_name)
        f.save(path)

        try:
            result = run_pipeline(source_path=path)
            flash(f"ETL completed. run_id={result.run_id}", "success")
            return redirect(url_for("pages.etl_status", run_id=result.run_id))
        except Exception as e:  # noqa: BLE001
            logger.exception("ETL failed")
            flash(f"ETL failed: {e}", "error")
            return redirect(url_for("pages.upload_and_run"))

    return render_template("upload.html")


@pages_bp.get("/etl/<run_id>")
def etl_status(run_id: str):
    with get_session() as session:
        latest = latest_pipeline_run(session, run_id=run_id)
    return render_template("etl_status.html", latest=latest)


@pages_bp.get("/dashboards")
def dashboards():
    eng = db_engine()
    enriched = load_enriched_sales_from_sqlite(eng)
    df = enriched.df if enriched is not None else None
    figures = build_dashboard_figures(enriched)
    kpis = compute_kpis(df if df is not None else None)
    dq_df = load_dq_summary(eng)
    dq_fig = build_dq_figure(dq_df)
    data_source = enriched.source if enriched is not None else "—"
    return render_template(
        "dashboards.html",
        figures=figures,
        kpis=kpis,
        dq_fig=dq_fig,
        data_source=data_source,
        has_sales=df is not None and not df.empty,
    )

