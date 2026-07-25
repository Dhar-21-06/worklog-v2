#!/usr/bin/env bash
# One-time backend setup: installs shared + backend packages, copies .env, runs migrations.
set -euo pipefail
cd "$(dirname "$0")/.."

pip install -e ./shared
pip install -e "./backend[dev]"

if [ ! -f backend/.env ]; then
  cp backend/.env.example backend/.env
  echo "Created backend/.env from .env.example"
fi

(cd backend && alembic upgrade head)
echo "Backend setup complete."
