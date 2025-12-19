import os

class Config:
    """
    Base configuration class.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    DEBUG = os.environ.get('DEBUG', False)
    DATABASE_URI = os.environ.get('DATABASE_URI', 'mysql+pymysql://username:password@localhost/dbname')
