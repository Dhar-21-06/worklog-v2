"""
System tray icon and menu.

Owns the QSystemTrayIcon and its context menu. Delegates all real behavior
(opening the dashboard, triggering a reminder, quitting) to callbacks passed
in from main.py, so this class has no knowledge of the scheduler or backend
process - it's purely a tray UI shell.
"""

from collections.abc import Callable

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMenu, QSystemTrayIcon

from app.core.logging import get_logger

logger = get_logger(__name__)


class TrayService:
    def __init__(
        self,
        icon: QIcon,
        on_open_dashboard: Callable[[], None],
        on_log_now: Callable[[], None],
        on_quit: Callable[[], None],
    ) -> None:
        self._tray_icon = QSystemTrayIcon(icon)
        self._tray_icon.setToolTip("WorkLog")

        menu = QMenu()

        open_action = QAction("Open Dashboard", menu)
        open_action.triggered.connect(on_open_dashboard)
        menu.addAction(open_action)

        log_now_action = QAction("Log Now", menu)
        log_now_action.triggered.connect(on_log_now)
        menu.addAction(log_now_action)

        menu.addSeparator()

        quit_action = QAction("Quit WorkLog", menu)
        quit_action.triggered.connect(on_quit)
        menu.addAction(quit_action)

        self._tray_icon.setContextMenu(menu)

    def show(self) -> None:
        logger.info("Showing system tray icon")
        self._tray_icon.show()

    def show_message(self, title: str, message: str) -> None:
        self._tray_icon.showMessage(title, message)
