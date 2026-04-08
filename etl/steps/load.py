from __future__ import annotations

from datetime import datetime

import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import Session

from models.audit import EtlAuditLog
from models.dq import DqIssue, DqTableScore


def load_all_layers(
    *,
    session: Session,
    run_id: str,
    source_file_name: str,
    raw: dict[str, pd.DataFrame],
    clean: dict[str, pd.DataFrame],
    curated: dict[str, pd.DataFrame],
    dq,
) -> None:
    _load_layer_tables(session, run_id, source_file_name, raw, layer="raw")
    _load_layer_tables(session, run_id, source_file_name, clean, layer="clean")
    _load_layer_tables(session, run_id, source_file_name, curated, layer="curated")
    _load_dq(session, run_id, dq)


def _load_layer_tables(
    session: Session,
    run_id: str,
    source_file_name: str,
    tables: dict[str, pd.DataFrame],
    *,
    layer: str,
) -> None:
    for name, df in tables.items():
        table_name = f"{layer}_{name}" if not name.startswith(f"{layer}_") else name

        inserted = 0
        rejected = 0
        status = "success"
        err = None

        try:
            if layer == "clean" and name == "sales":
                inserted = _upsert_sales_by_sale_id(session, table_name, df)
            else:
                inserted = _replace_table(session, table_name, df)
        except Exception as e:  # noqa: BLE001
            status = "failed"
            err = str(e)
        finally:
            session.add(
                EtlAuditLog(
                    pipeline_run_id=run_id,
                    run_timestamp_utc=datetime.utcnow(),
                    source_file_name=source_file_name,
                    table_name=table_name,
                    layer=layer,
                    raw_row_count=int(len(df)) if df is not None else 0,
                    clean_row_count=int(len(df)) if df is not None else 0,
                    inserted_count=int(inserted),
                    updated_count=0,
                    rejected_count=int(rejected),
                    status=status,
                    error_message=err,
                )
            )


def _replace_table(session: Session, table_name: str, df: pd.DataFrame) -> int:
    """
    Default: replace entire table (safe baseline for dimension/snapshot tables).
    """
    if df is None:
        df = pd.DataFrame()
    df.to_sql(table_name, session.get_bind(), if_exists="replace", index=False)
    return int(len(df))


def _upsert_sales_by_sale_id(session: Session, table_name: str, df: pd.DataFrame) -> int:
    """
    Incremental/idempotent load for Sales using sale_id as the business key.
    - If the table doesn't exist yet, create it and load all rows.
    - If it exists, append only sale_id values not already present.
    """
    if df is None or df.empty:
        _replace_table(session, table_name, pd.DataFrame(columns=df.columns if df is not None else []))
        return 0

    if "sale_id" not in df.columns:
        # Cannot increment without key; fall back to replace (still deterministic).
        _replace_table(session, table_name, df)
        return int(len(df))

    bind = session.get_bind()
    # Detect existing table
    exists = bool(
        session.execute(
            text("SELECT name FROM sqlite_master WHERE type='table' AND name=:t"),
            {"t": table_name},
        ).fetchone()
    )
    if not exists:
        df.to_sql(table_name, bind, if_exists="replace", index=False)
        return int(len(df))

    existing_ids = pd.read_sql_query(f"SELECT sale_id FROM {table_name}", bind)
    existing_set = set(existing_ids["sale_id"].astype(str).tolist())
    incoming = df.copy()
    incoming["sale_id"] = incoming["sale_id"].astype(str)
    to_insert = incoming.loc[~incoming["sale_id"].isin(existing_set)].copy()
    if to_insert.empty:
        return 0
    to_insert.to_sql(table_name, bind, if_exists="append", index=False)
    return int(len(to_insert))


def _load_dq(session: Session, run_id: str, dq) -> None:
    # Clear old DQ for the run_id if re-run with same id (rare but safe)
    session.query(DqIssue).filter(DqIssue.pipeline_run_id == run_id).delete()
    session.query(DqTableScore).filter(DqTableScore.pipeline_run_id == run_id).delete()

    if dq.issues is not None and not dq.issues.empty:
        for _, r in dq.issues.iterrows():
            session.add(
                DqIssue(
                    pipeline_run_id=run_id,
                    table_name=str(r["table_name"]),
                    severity=str(r["severity"]),
                    issue_type=str(r["issue_type"]),
                    column_name=None if pd.isna(r["column_name"]) else str(r["column_name"]),
                    row_identifier=None if pd.isna(r["row_identifier"]) else str(r["row_identifier"]),
                    message=str(r["message"]),
                    business_impact=str(r["business_impact"]),
                    recommended_action=str(r["recommended_action"]),
                )
            )

    if dq.table_scores is not None and not dq.table_scores.empty:
        for _, r in dq.table_scores.iterrows():
            session.add(
                DqTableScore(
                    pipeline_run_id=run_id,
                    table_name=str(r["table_name"]),
                    quality_score=float(r["quality_score"]),
                    critical_issue_count=int(r["critical_issue_count"]),
                    medium_issue_count=int(r["medium_issue_count"]),
                    low_issue_count=int(r["low_issue_count"]),
                    notes=None if pd.isna(r["notes"]) else str(r["notes"]),
                )
            )

