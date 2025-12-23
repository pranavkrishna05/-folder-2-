"""
Profile model definition.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class Profile(db.Model):
    """Representation of user profiles."""

    __tablename__ = "profiles"

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, nullable=False, unique=True)
    first_name: str = Column(String(50), nullable=True)
    last_name: str = Column(String(50), nullable=True)
    preferences: str = Column(String(200), nullable=True)

    def update_profile(self, first_name: str = None, last_name: str = None, preferences: str = None) -> None:
        """Update profile fields."""
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if preferences is not None:
            self.preferences = preferences