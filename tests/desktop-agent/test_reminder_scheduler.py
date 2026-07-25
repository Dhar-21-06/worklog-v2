"""Smoke test for reminder scheduling logic."""

from app.scheduler.reminder_scheduler import REMINDER_JOB_ID, ReminderScheduler


def test_scheduler_registers_daily_job():
    calls = []
    scheduler = ReminderScheduler(on_reminder_due=lambda: calls.append(True))
    scheduler.start()

    job = scheduler._scheduler.get_job(REMINDER_JOB_ID)
    assert job is not None

    scheduler.shutdown()
