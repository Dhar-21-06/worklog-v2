# API Reference

Bootstrap milestone exposes a single endpoint:

| Method | Path                | Description                          |
|--------|---------------------|---------------------------------------|
| GET    | `/api/v1/health`    | Liveness check used by desktop-agent |

FastAPI also serves interactive docs at `/docs` (Swagger) and `/redoc` when
the backend is running. This file will be expanded with each feature
milestone (reports, calendar, analytics, search, export, backup) as those
endpoints are implemented, rather than duplicating what Swagger already shows.
