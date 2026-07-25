"""
Shared FastAPI dependencies.

Endpoint modules import from here rather than constructing sessions/services
inline, so the wiring between layers (API -> Services -> Repositories) has
one place to change.
"""

from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import get_db

__all__ = ["get_db", "DbSession"]


def DbSession() -> Generator[Session, None, None]:  # noqa: N802 - FastAPI dependency convention
    """Alias kept for readability at call sites: `db: Session = Depends(DbSession)`."""
    yield from get_db()
