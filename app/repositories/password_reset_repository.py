"""
Repository layer for password reset data interactions.
"""

from app.models.password_reset import PasswordReset, db
from datetime import datetime, timedelta


class PasswordResetRepository:
    """Provides PasswordReset model-related database functionality."""

    @staticmethod
    def create_password_reset(user_id: int, reset_token: str) -> PasswordReset:
        """Store a new password reset request in the database."""
        expires_at = datetime.utcnow() + timedelta(hours=24)
        password_reset = PasswordReset(user_id=user_id, reset_token=reset_token, expires_at=expires_at)
        db.session.add(password_reset)
        db.session.commit()
        return password_reset

    @staticmethod
    def get_password_reset_by_token(reset_token: str) -> PasswordReset | None:
        """Retrieve a password reset record by its token."""
        return PasswordReset.query.filter_by(reset_token=reset_token).first()

    @staticmethod
    def delete_password_reset(reset_id: int) -> None:
        """Delete a password reset record."""
        password_reset = PasswordReset.query.get(reset_id)
        if password_reset:
            db.session.delete(password_reset)
            db.session.commit()