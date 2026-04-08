from __future__ import annotations

import os
from dataclasses import dataclass


def _env(key: str, default: str) -> str:
    v = os.getenv(key)
    return v if v is not None and v != "" else default


@dataclass(frozen=True)
class Settings:
    secret_key: str = _env("SECRET_KEY", "dev-secret-change-me")
    database_url: str = _env("DATABASE_URL", "sqlite:///data/app.db")
    upload_folder: str = _env("UPLOAD_FOLDER", "uploads")
    max_content_length_mb: int = int(_env("MAX_CONTENT_LENGTH_MB", "50"))


settings = Settings()

