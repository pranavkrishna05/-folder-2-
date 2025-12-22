import os

class Config:
    """
    Base configuration class containing default settings.
    """
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_DATABASE_URI: str = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    DEBUG: bool = False

class DevelopmentConfig(Config):
    """
    Development configuration class.
    """
    DEBUG: bool = True

class TestingConfig(Config):
    """
    Testing configuration class.
    """
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///test.db'

class ProductionConfig(Config):
    """
    Production configuration class.
    """
    DEBUG: bool = False

config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}