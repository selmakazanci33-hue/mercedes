from __future__ import annotations

import os

import pandas as pd


def export_run_artifacts(*, run_id: str, raw, clean, curated, dq) -> None:
    run_dir = os.path.join("exports", run_id)
    os.makedirs(run_dir, exist_ok=True)

    _export_tables(os.path.join(run_dir, "raw"), raw)
    _export_tables(os.path.join(run_dir, "clean"), clean)
    _export_tables(os.path.join(run_dir, "curated"), curated)

    if dq is not None:
        if getattr(dq, "issues", None) is not None:
            dq.issues.to_csv(os.path.join(run_dir, "dq_issues.csv"), index=False)
        if getattr(dq, "table_scores", None) is not None:
            dq.table_scores.to_csv(os.path.join(run_dir, "dq_table_scores.csv"), index=False)


def _export_tables(dir_path: str, tables: dict[str, pd.DataFrame]) -> None:
    os.makedirs(dir_path, exist_ok=True)
    for name, df in tables.items():
        if df is None:
            continue
        out = os.path.join(dir_path, f"{name}.csv")
        df.to_csv(out, index=False)

