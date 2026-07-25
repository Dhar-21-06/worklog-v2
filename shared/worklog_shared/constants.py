"""
Constants shared between the backend and desktop-agent processes.

Anything that both processes must agree on (default ports, reminder timing
defaults, report status values) lives here so there is exactly one place to
change it.
"""

# Local networking
DEFAULT_BACKEND_HOST = "127.0.0.1"
DEFAULT_BACKEND_PORT = 8000
DEFAULT_FRONTEND_PORT = 3000

# Reminder defaults (overridable via Settings, these are just fallbacks)
DEFAULT_REMINDER_TIME = "18:00"
DEFAULT_SNOOZE_MINUTES = 10

# Report status values (kept as plain strings here; see enums.py for the
# typed version used in code)
REPORT_STATUS_COMPLETED = "completed"
REPORT_STATUS_DRAFT = "draft"
REPORT_STATUS_MISSED = "missed"
