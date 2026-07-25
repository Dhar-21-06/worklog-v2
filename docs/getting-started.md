# Getting Started

## Prerequisites

- Python 3.11+
- Node.js 20+
- Windows 10/11 (desktop-agent targets Windows; backend/frontend are OS-agnostic)

## Backend

```bash
cd shared && pip install -e .
cd ../backend && pip install -e ".[dev]"
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload --port 8000
```

## Desktop Agent

```bash
cd shared && pip install -e .
cd ../desktop-agent && pip install -e ".[dev]"
python -m app.main
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000. The web app expects the backend at
http://localhost:8000 (see `frontend/src/lib/api-client.ts`).

## Convenience scripts

See `scripts/` for one-shot setup and dev-run scripts that wrap the steps above.
