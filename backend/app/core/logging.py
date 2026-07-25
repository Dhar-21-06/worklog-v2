"""
Application-wide logging setup.

Called once at startup from app.main. Uses stdlib logging so it composes
cleanly with uvicorn's own loggers instead of fighting them.
"""

import logging
import sys

from app.core.config import settings

_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def configure_logging() -> None:
    root = logging.getLogger()
    root.setLevel(settings.log_level)

    if root.handlers:
        # Already configured (e.g. reloader re-import) - avoid duplicate handlers.
        return

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(_LOG_FORMAT))
    root.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
