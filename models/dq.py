from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class DqIssue(Base):
    __tablename__ = "dq_issues"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pipeline_run_id: Mapped[str] = mapped_column(String(64), index=True)
    created_at_utc: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    table_name: Mapped[str] = mapped_column(String(128), index=True)
    severity: Mapped[str] = mapped_column(String(16), index=True)  # critical|medium|low
    issue_type: Mapped[str] = mapped_column(String(64), index=True)  # missing|duplicate|orphan|type|outlier|schema

    column_name: Mapped[str | None] = mapped_column(String(128), nullable=True)
    row_identifier: Mapped[str | None] = mapped_column(String(256), nullable=True)

    message: Mapped[str] = mapped_column(Text)
    business_impact: Mapped[str] = mapped_column(Text)
    recommended_action: Mapped[str] = mapped_column(Text)


class DqTableScore(Base):
    __tablename__ = "dq_table_scores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pipeline_run_id: Mapped[str] = mapped_column(String(64), index=True)
    table_name: Mapped[str] = mapped_column(String(128), index=True)
    quality_score: Mapped[float] = mapped_column(Float)
    critical_issue_count: Mapped[int] = mapped_column(Integer, default=0)
    medium_issue_count: Mapped[int] = mapped_column(Integer, default=0)
    low_issue_count: Mapped[int] = mapped_column(Integer, default=0)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

