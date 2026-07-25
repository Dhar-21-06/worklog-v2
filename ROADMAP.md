# WorkLog v2 Roadmap

## Milestone 1 — Project Bootstrap ✅ Complete
- Canonical folder structure
- Backend scaffold (FastAPI, SQLAlchemy, Alembic, config, logging, health endpoint)
- Desktop-agent scaffold (PySide6 tray, scheduler, reminder service, backend launcher)
- Frontend scaffold (Vite, React, TS, Tailwind, shadcn/ui, TanStack Query, React Router)
- Shared package (`worklog_shared`) for cross-process constants/enums
- Dependency management (pyproject.toml x3, package.json)
- Linting/formatting (ruff, black, eslint, prettier, pre-commit)
- Test scaffolding (pytest, smoke tests for health endpoint and scheduler)

## Phase 1 — Core Backend & Agent
- Report model, schema, repository, service, CRUD API
- Reminder popup UI (PySide6): rounded corners, animations, autosave, keyboard shortcuts
- Backup scheduler, export scheduler

## Phase 2 — Web Application
- Dashboard, Reports, Daily Report, Calendar pages
- Global providers: theme (dark/light), command palette

## Phase 3 — Analytics & Search
- Analytics page (Recharts trends, streaks, snooze frequency)
- Weekly / Monthly summaries
- Global search (Ctrl+K)

## Phase 4 — Polish
- Animations, empty states, accessibility
- Performance passes
- Windows packaging (PyInstaller) for desktop-agent

## Phase 5 — AI Integration
- AI-generated weekly/monthly summaries, manager updates, resume bullets
- Natural-language search
- OpenAPI-generated TypeScript types (replacing `shared/frontend-types`)
