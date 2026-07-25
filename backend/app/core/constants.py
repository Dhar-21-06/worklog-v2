"""
Backend-local constants.

Values shared with the desktop-agent (e.g. report status, reminder defaults)
live in the `worklog_shared` package instead, so both processes stay in sync.
This file is only for constants that are backend-specific (API prefixes, etc).
"""

API_V1_PREFIX = "/api/v1"
APP_TITLE = "WorkLog Backend"
APP_DESCRIPTION = "Local REST API powering the WorkLog v2 desktop experience."
