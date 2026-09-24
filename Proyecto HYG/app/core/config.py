import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = "HYG GASTRO-SOFT API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "API para la gestión integral de operaciones gastronómicas."
    )

    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"


settings = Settings()