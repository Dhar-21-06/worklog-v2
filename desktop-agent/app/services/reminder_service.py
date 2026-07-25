"""
Reminder service.

Coordinates what happens when a reminder fires: showing the native popup
(added in a later milestone alongside the actual PySide6 popup widget) and
posting the resulting draft/report to the backend. Kept separate from
ReminderScheduler so scheduling policy and reminder behavior can evolve
independently.
"""

from app.core.logging import get_logger

logger = get_logger(__name__)


class ReminderService:
    def __init__(self) -> None:
        pass

    def trigger_reminder(self) -> None:
        """
        Called by the scheduler when a reminder is due.

        Bootstrap milestone: just logs. The native popup (rounded corners,
        animations, autosave-draft, keyboard shortcuts per the design spec)
        is implemented in the "Reminder Popup" milestone.
        """
        logger.info("Reminder triggered - popup UI not yet implemented")
