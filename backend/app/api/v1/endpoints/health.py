"""
Health check endpoint.

Used by the desktop-agent to confirm the backend has started before it
opens the local web application (see desktop-agent/app/services/backend_launcher.py).
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
