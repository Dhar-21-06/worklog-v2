"""
Reminder scheduling.

Wraps APScheduler's BackgroundScheduler so the rest of the app depends on a
small, purpose-built interface (schedule / reschedule / snooze) rather than
the scheduler library directly. Also owns backup/export scheduling per the
architecture doc, added in a later milestone.
"""

from collections.abc import Callable
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

REMINDER_JOB_ID = "daily_reminder"


class ReminderScheduler:
    def __init__(self, on_reminder_due: Callable[[], None]) -> None:
        self._scheduler = BackgroundScheduler()
        self._on_reminder_due = on_reminder_due

    def start(self) -> None:
        hour, minute = (int(part) for part in settings.reminder_time.split(":"))
        self._scheduler.add_job(
            self._on_reminder_due,
            trigger="cron",
            hour=hour,
            minute=minute,
            id=REMINDER_JOB_ID,
            replace_existing=True,
        )
        self._scheduler.start()
        logger.info("Reminder scheduler started (daily at %s)", settings.reminder_time)

    def snooze(self, minutes: int | None = None) -> None:
        delay = minutes or settings.snooze_minutes
        run_at = datetime.now() + timedelta(minutes=delay)
        self._scheduler.add_job(
            self._on_reminder_due,
            trigger="date",
            run_date=run_at,
            id=f"{REMINDER_JOB_ID}_snooze",
            replace_existing=True,
        )
        logger.info("Reminder snoozed for %s minutes", delay)

    def shutdown(self) -> None:
        self._scheduler.shutdown(wait=False)
