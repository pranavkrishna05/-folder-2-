"""
Configuration settings for the Flask application.
"""

from logging.config import dictConfig


class Config:
    """Flask application configuration."""

    DEBUG: bool = False
    TESTING: bool = False
    SECRET_KEY: str = "your-secret-key"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG: bool = True


class TestingConfig(Config):
    """Testing configuration."""

    TESTING: bool = True


def configure_logging() -> None:
    """Configure application logging."""
    dictConfig(
        {
            "version": 1,
            "formatters": {"default": {"format": "%(asctime)s - %(levelname)s - %(message)s"}},
            "handlers": {
                "console": {"class": "logging.StreamHandler", "formatter": "default"}
            },
            "root": {"level": "DEBUG", "handlers": ["console"]},
        }
    )


configure_logging()