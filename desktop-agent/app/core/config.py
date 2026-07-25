"""
Desktop-agent configuration.

Mirrors the pattern used in backend/app/core/config.py: one Settings object,
imported everywhere, backed by an .env file for local overrides.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from worklog_shared.constants import (
    DEFAULT_BACKEND_HOST,
    DEFAULT_BACKEND_PORT,
    DEFAULT_FRONTEND_PORT,
    DEFAULT_REMINDER_TIME,
    DEFAULT_SNOOZE_MINUTES,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    log_level: str = "INFO"

    backend_host: str = DEFAULT_BACKEND_HOST
    backend_port: int = DEFAULT_BACKEND_PORT
    frontend_port: int = DEFAULT_FRONTEND_PORT

    reminder_time: str = DEFAULT_REMINDER_TIME
    snooze_minutes: int = DEFAULT_SNOOZE_MINUTES

    launch_on_startup: bool = True

    @property
    def backend_base_url(self) -> str:
        return f"http://{self.backend_host}:{self.backend_port}"

    @property
    def backend_health_url(self) -> str:
        return f"{self.backend_base_url}/api/v1/health"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
