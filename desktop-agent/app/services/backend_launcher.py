"""
Launches and monitors the FastAPI backend as a subprocess.

The agent owns the backend's lifecycle: start it on agent launch, poll
/api/v1/health until it responds, and (in a later milestone) restart it if
it dies. Kept as a plain class rather than a QThread for now - upgraded to
threaded polling once the tray/popup UI needs to stay responsive during checks.
"""

import subprocess
import sys
import time

import requests

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class BackendLauncher:
    def __init__(self) -> None:
        self._process: subprocess.Popen | None = None

    def start(self) -> None:
        logger.info("Starting backend on %s", settings.backend_base_url)
        self._process = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "uvicorn",
                "app.main:app",
                "--host",
                settings.backend_host,
                "--port",
                str(settings.backend_port),
            ],
            cwd="../backend",
        )

    def wait_until_healthy(self, timeout_seconds: int = 15) -> bool:
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            try:
                response = requests.get(settings.backend_health_url, timeout=1)
                if response.status_code == 200:
                    logger.info("Backend is healthy")
                    return True
            except requests.RequestException:
                pass
            time.sleep(0.5)
        logger.warning("Backend did not become healthy within %s seconds", timeout_seconds)
        return False

    def stop(self) -> None:
        if self._process and self._process.poll() is None:
            logger.info("Stopping backend process")
            self._process.terminate()
