# WorkLog v2 — Architecture

## Overview

Two independent local processes communicate over a REST API:

```
Desktop Agent (PySide6)  ──launches & monitors──▶  Backend (FastAPI)
       │                                                  ▲
       │ opens browser to                                 │ REST (localhost)
       ▼                                                  │
Local Web App (React, http://localhost:3000) ─────────────┘
```

## Backend layering

```
API (FastAPI routers)
  ↓
Services (business logic)
  ↓
Repositories (data access)
  ↓
Database (SQLite via SQLAlchemy)
```

- **API** layer only handles HTTP concerns: request/response schemas, status codes.
- **Services** hold business logic and are the only layer services import from each other.
- **Repositories** are the only layer that touches the SQLAlchemy `Session`.
- **Never** skip a layer (e.g. an endpoint calling a repository directly).

## Shared code

`shared/worklog_shared` is a pip-installable package consumed by both `backend`
and `desktop-agent`, holding constants, enums, and cross-process DTOs.
`shared/frontend-types` mirrors the same enums in TypeScript by hand until an
OpenAPI-generated client replaces it.

## Why this structure

- Backend and desktop-agent are separate installable Python packages because
  they will ship on different lifecycles (backend runs as a subprocess of the
  agent; the agent alone gets packaged into a Windows installer via PyInstaller).
- Alembic is wired up from day one so the first real model doesn't require
  retrofitting migration tooling.
- The frontend's provider tree (`QueryClientProvider`, `RouterProvider`) is
  established now so later milestones add routes/queries without restructuring.
