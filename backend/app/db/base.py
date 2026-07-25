"""
SQLAlchemy declarative base.

All ORM models (app/models/*) inherit from `Base`. Kept in its own module,
separate from session.py, so Alembic's env.py can import metadata without
also pulling in engine/session creation.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
