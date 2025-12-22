-----------------------------------------------
import os
import logging

logger = logging.getLogger(__name__)

class Config:
    APP_ENV: str
    DB_URL: str

    @staticmethod
    def load() -> None:
        logger.info("Loading configuration...")
        # Load environment variables
        Config.APP_ENV = os.getenv("APP_ENV", "development")
        Config.DB_URL = os.getenv("DB_URL", "sqlite:///:memory:")
        logger.info(f"Configuration loaded: APP_ENV={Config.APP_ENV}, DB_URL={Config.DB_URL}")