from __future__ import annotations

import logging
import os

from flask import Flask

from config import settings
from routes.pages import pages_bp
from services.db import init_db


def create_app() -> Flask:
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config["SECRET_KEY"] = settings.secret_key
    app.config["UPLOAD_FOLDER"] = settings.upload_folder
    app.config["MAX_CONTENT_LENGTH"] = settings.max_content_length_mb * 1024 * 1024

    os.makedirs(settings.upload_folder, exist_ok=True)
    os.makedirs("data", exist_ok=True)
    os.makedirs("exports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    _configure_logging()
    init_db()

    app.register_blueprint(pages_bp)
    return app


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
        handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
    )

