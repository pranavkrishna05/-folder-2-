"""
Configuration settings for the application.
"""

class Config:
    SECRET_KEY = "your-secret-key"
    SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
```