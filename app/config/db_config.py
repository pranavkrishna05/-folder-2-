"""
Database configuration for the Flask application
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

DATABASE_URL = "sqlite:///app.db"  # Replace with the actual database URL

def get_engine():
    """
    Get the database engine.
    
    Returns:
        SQLAlchemy engine instance.
    """
    return create_engine(DATABASE_URL)

def get_db_session():
    """
    Get a new session for database interaction.
    
    Returns:
        SQLAlchemy session object.
    """
    Session = sessionmaker(bind=get_engine(), autoflush=False, autocommit=False)
    return Session()