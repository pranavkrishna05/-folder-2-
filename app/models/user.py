"""
User Model: Represents the user entity in the database.
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

db = SQLAlchemy()

class User(db.Model):
    """Defines the User database schema."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email})>"