"""
Application Configuration Module.
Provides centralized configuration management for the Flask Application.
"""

import os
from pydantic import BaseSettings

class AppConfig(BaseSettings):
    """Centralized configuration management using Pydantic."""
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")

    # Database-related configurations
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///default.db")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    
    class Config:
        env_file = ".env"

config = AppConfig()