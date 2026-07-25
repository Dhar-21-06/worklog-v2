"""
Desktop agent entrypoint.

Run locally with:
    python -m app.main

Responsibilities kept here are wiring only - starting the backend, starting
the scheduler, showing the tray icon. Actual behavior lives in
app/services and app/scheduler.
"""

import sys
import webbrowser

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from app.core.config import settings
from app.core.logging import configure_logging, get_logger
from app.scheduler.reminder_scheduler import ReminderScheduler
from app.services.backend_launcher import BackendLauncher
from app.services.reminder_service import ReminderService
from app.tray.tray_service import TrayService

configure_logging()
logger = get_logger(__name__)


def main() -> None:
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    backend_launcher = BackendLauncher()
    backend_launcher.start()
    backend_launcher.wait_until_healthy()

    reminder_service = ReminderService()
    scheduler = ReminderScheduler(on_reminder_due=reminder_service.trigger_reminder)
    scheduler.start()

    def open_dashboard() -> None:
        webbrowser.open(f"http://localhost:{settings.frontend_port}")

    def quit_app() -> None:
        logger.info("Shutting down WorkLog agent")
        scheduler.shutdown()
        backend_launcher.stop()
        app.quit()

    tray = TrayService(
        icon=QIcon(),  # placeholder - real icon added under assets/icons
        on_open_dashboard=open_dashboard,
        on_log_now=reminder_service.trigger_reminder,
        on_quit=quit_app,
    )
    tray.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
