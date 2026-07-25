# WorkLog v2

WorkLog v2 is an offline-first productivity companion that combines a lightweight Windows desktop agent with a modern local web application.

## Features

- Desktop reminder agent
- Local web dashboard
- Daily work journal
- Analytics
- Calendar
- Weekly & Monthly summaries
- Search
- Exports
- Local backups

## Project Structure

```text
WorkLog-v2/
├── backend/         FastAPI + SQLAlchemy + Alembic REST API
├── desktop-agent/    PySide6 tray app, scheduler, reminder popup
├── frontend/         React + Vite + TypeScript + Tailwind + shadcn/ui
├── shared/           Code shared between backend and desktop-agent
├── docs/             Architecture, API, and setup documentation
├── scripts/          Setup and dev-run scripts
├── tests/            Backend and desktop-agent test suites
└── assets/           Icons, images, fonts
```

See `docs/architecture.md` for the full architecture and `docs/getting-started.md`
to run the project locally.

## Tech Stack

### Backend
- Python 3.11+
- FastAPI, SQLAlchemy, Alembic, Pydantic

### Desktop Agent
- Python 3.11+
- PySide6, APScheduler

### Frontend
- React, TypeScript, Vite
- Tailwind CSS, shadcn/ui, Framer Motion
- TanStack Query, React Router, Recharts

## Status

🚧 Under Development — Milestone 1 (Project Bootstrap) complete. See `ROADMAP.md`.
