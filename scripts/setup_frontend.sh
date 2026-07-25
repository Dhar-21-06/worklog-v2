#!/usr/bin/env bash
# One-time frontend setup: installs npm dependencies.
set -euo pipefail
cd "$(dirname "$0")/../frontend"
npm install
echo "Frontend setup complete."
