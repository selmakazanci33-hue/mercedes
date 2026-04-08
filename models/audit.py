from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class EtlAuditLog(Base):
    __tablename__ = "etl_audit_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pipeline_run_id: Mapped[str] = mapped_column(String(64), index=True)
    run_timestamp_utc: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    source_file_name: Mapped[str] = mapped_column(String(512))

    table_name: Mapped[str] = mapped_column(String(128))
    layer: Mapped[str] = mapped_column(String(32))  # raw|clean|curated|dq

    raw_row_count: Mapped[int] = mapped_column(Integer, default=0)
    clean_row_count: Mapped[int] = mapped_column(Integer, default=0)
    inserted_count: Mapped[int] = mapped_column(Integer, default=0)
    updated_count: Mapped[int] = mapped_column(Integer, default=0)
    rejected_count: Mapped[int] = mapped_column(Integer, default=0)

    status: Mapped[str] = mapped_column(String(32), default="success")  # success|failed|warn
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

