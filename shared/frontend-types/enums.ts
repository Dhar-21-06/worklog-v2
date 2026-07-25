/**
 * Mirrors shared/worklog_shared/enums.py.
 *
 * TEMPORARY: manually kept in sync until the API surface stabilizes, at
 * which point this should be replaced by types generated from the FastAPI
 * OpenAPI schema (e.g. via `openapi-typescript`). Flagged in ROADMAP as a
 * Phase 2/3 tooling improvement.
 */

export enum ReportStatus {
  Completed = "completed",
  Draft = "draft",
  Missed = "missed",
  Today = "today",
}

export enum ReminderAction {
  Save = "save",
  Cancel = "cancel",
  Skip = "skip",
  Snooze = "snooze",
}
