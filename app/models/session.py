"""
Session model definition.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

db = SQLAlchemy()


class Session(db.Model):
    """Representation of user sessions."""

    __tablename__ = "sessions"

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, nullable=False)
    session_token: str = Column(String(200), unique=True, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    last_activity_at: datetime = Column(DateTime, nullable=True)

    def is_active(self, timeout_minutes: int = 30) -> bool:
        """Check if the session is active based on inactivity timeout."""
        if self.last_activity_at:
            inactivity_period = (datetime.utcnow() - self.last_activity_at).total_seconds() / 60
            return inactivity_period <= timeout_minutes
        return False