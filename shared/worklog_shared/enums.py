"""Shared enums, mirrored in shared/frontend-types for the web app."""

from enum import StrEnum


class ReportStatus(StrEnum):
    COMPLETED = "completed"
    DRAFT = "draft"
    MISSED = "missed"
    TODAY = "today"


class ReminderAction(StrEnum):
    SAVE = "save"
    CANCEL = "cancel"
    SKIP = "skip"
    SNOOZE = "snooze"
