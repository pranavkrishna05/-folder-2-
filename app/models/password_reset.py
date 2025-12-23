"""
Password reset model definition.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, DateTime

db = SQLAlchemy()


class PasswordReset(db.Model):
    """Representation of password reset requests."""

    __tablename__ = "password_resets"

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, nullable=False)
    reset_token: str = Column(String(200), unique=True, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    expires_at: datetime = Column(DateTime, nullable=False)

    def has_expired(self) -> bool:
        """Check if the reset token has expired."""
        return datetime.utcnow() > self.expires_at