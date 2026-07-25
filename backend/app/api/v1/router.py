"""
Aggregates all v1 endpoint routers into a single APIRouter.

Future milestones add new `include_router` calls here (reports, calendar,
analytics, search, settings, export, backup) instead of registering
routers directly on the FastAPI app in main.py.
"""

from fastapi import APIRouter

from app.api.v1.endpoints import health

api_router = APIRouter()
api_router.include_router(health.router)
