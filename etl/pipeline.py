from __future__ import annotations

import logging
import os
import uuid
from dataclasses import dataclass
from datetime import datetime

import pandas as pd

from etl.steps.clean import clean_tables
from etl.steps.curate import build_curated
from etl.steps.dq import run_data_quality
from etl.steps.extract import extract_excel_tables
from etl.steps.load import load_all_layers
from services.db import get_session
from services.exports import export_run_artifacts


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class PipelineResult:
    run_id: str
    source_path: str
    started_at_utc: datetime
    finished_at_utc: datetime


def run_pipeline(source_path: str) -> PipelineResult:
    run_id = uuid.uuid4().hex[:12]
    started = datetime.utcnow()
    logger.info("Starting ETL run_id=%s source=%s", run_id, source_path)

    if not os.path.exists(source_path):
        raise FileNotFoundError(source_path)

    raw = extract_excel_tables(source_path)
    clean, clean_rejects = clean_tables(raw)
    dq = run_data_quality(raw=raw, clean=clean, rejects=clean_rejects, run_id=run_id)
    curated = build_curated(clean)

    # persist everything in a transaction
    with get_session() as session:
        load_all_layers(
            session=session,
            run_id=run_id,
            source_file_name=os.path.basename(source_path),
            raw=raw,
            clean=clean,
            curated=curated,
            dq=dq,
        )

    export_run_artifacts(run_id=run_id, raw=raw, clean=clean, curated=curated, dq=dq)
    finished = datetime.utcnow()
    logger.info("Finished ETL run_id=%s", run_id)
    return PipelineResult(
        run_id=run_id,
        source_path=source_path,
        started_at_utc=started,
        finished_at_utc=finished,
    )

