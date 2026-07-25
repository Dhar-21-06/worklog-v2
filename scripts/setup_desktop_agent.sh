#!/usr/bin/env bash
# One-time desktop-agent setup: installs shared + agent packages.
set -euo pipefail
cd "$(dirname "$0")/.."

pip install -e ./shared
pip install -e "./desktop-agent[dev]"
echo "Desktop agent setup complete."
