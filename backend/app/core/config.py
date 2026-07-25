"""
Centralized application configuration.

All environment-dependent values live here and nowhere else. Services and
repositories should import `settings` from this module rather than reading
os.environ directly, so configuration stays testable and mockable.
"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # App
    app_env: str = "development"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    log_level: str = "INFO"

    # Database
    database_url: str = "sqlite:///./worklog.sqlite"

    # CORS
    cors_origins: list[str] = ["http://localhost:3000"]

    # Filesystem locations
    backup_dir: Path = Path("./backups")
    export_dir: Path = Path("./exports")

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"


@lru_cache
def get_settings() -> Settings:
    """Cached settings accessor. Use as a FastAPI dependency via app.api.deps."""
    return Settings()


settings = get_settings()
