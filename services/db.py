from __future__ import annotations

import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config import settings
from models.base import Base


_engine = create_engine(settings.database_url, future=True)
_SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False, future=True)


def init_db() -> None:
    Base.metadata.create_all(bind=_engine)


@contextlib.contextmanager
def get_session() -> Session:
    session: Session = _SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def engine():
    return _engine

