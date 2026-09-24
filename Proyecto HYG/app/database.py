from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings


if not settings.DATABASE_URL:
    raise ValueError(
        "No se encontró DATABASE_URL en el archivo .env"
    )


engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()