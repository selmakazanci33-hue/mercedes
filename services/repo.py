from __future__ import annotations

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from models.audit import EtlAuditLog


def latest_pipeline_run(session: Session, run_id: str | None = None) -> dict | None:
    stmt = select(EtlAuditLog).order_by(desc(EtlAuditLog.run_timestamp_utc))
    if run_id:
        stmt = stmt.where(EtlAuditLog.pipeline_run_id == run_id)
    rows = session.execute(stmt.limit(200)).scalars().all()
    if not rows:
        return None

    # group the most recent run (or the requested run_id)
    rid = run_id or rows[0].pipeline_run_id
    run_rows = [r for r in rows if r.pipeline_run_id == rid]
    return {
        "pipeline_run_id": rid,
        "run_timestamp_utc": max(r.run_timestamp_utc for r in run_rows),
        "source_file_name": run_rows[0].source_file_name,
        "tables": [
            {
                "table_name": r.table_name,
                "layer": r.layer,
                "raw_row_count": r.raw_row_count,
                "clean_row_count": r.clean_row_count,
                "inserted_count": r.inserted_count,
                "updated_count": r.updated_count,
                "rejected_count": r.rejected_count,
                "status": r.status,
                "error_message": r.error_message,
            }
            for r in sorted(run_rows, key=lambda x: (x.layer, x.table_name))
        ],
    }

