"""
FastAPI application factory and entrypoint.

Run locally with:
    uvicorn app.main:app --reload --port 8000

The desktop-agent launches this same app as a subprocess in production
(see desktop-agent/app/services/backend_launcher.py).
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.constants import API_V1_PREFIX, APP_DESCRIPTION, APP_TITLE
from app.core.logging import configure_logging, get_logger

configure_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("WorkLog backend starting up (env=%s)", settings.app_env)
    yield
    logger.info("WorkLog backend shutting down")


def create_app() -> FastAPI:
    app = FastAPI(
        title=APP_TITLE,
        description=APP_DESCRIPTION,
        version="0.1.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=API_V1_PREFIX)

    return app


app = create_app()
