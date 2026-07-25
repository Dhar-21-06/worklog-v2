#!/usr/bin/env bash
# Runs backend and frontend dev servers together for local development.
# (Desktop agent normally launches the backend itself - this script is for
# frontend-focused work where you don't want to run the full agent.)
set -euo pipefail
cd "$(dirname "$0")/.."

trap 'kill 0' EXIT

(cd backend && uvicorn app.main:app --reload --port 8000) &
(cd frontend && npm run dev) &

wait
