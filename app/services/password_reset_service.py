"""
Password reset service: application layer for recovery logic.
"""

import secrets
from app.repositories.password_reset_repository import PasswordResetRepository
from app.repositories.user_repository import UserRepository
from app.models.password_reset import PasswordReset


class PasswordResetService:
    """Service layer to handle password reset-related logic."""

    @staticmethod
    def initiate_password_reset(email: str) -> dict:
        """Initiate password reset process."""
        user = UserRepository.get_user_by_email(email)
        if not user:
            raise ValueError("Email not registered")

        # Generate reset token
        reset_token = secrets.token_hex(32)
        password_reset = PasswordResetRepository.create_password_reset(user_id=user.id, reset_token=reset_token)
        return {"reset_token": password_reset.reset_token, "expires_at": password_reset.expires_at}

    @staticmethod
    def verify_reset_token(reset_token: str) -> bool:
        """Verify if the reset token is valid and not expired."""
        password_reset = PasswordResetRepository.get_password_reset_by_token(reset_token)
        if not password_reset or password_reset.has_expired():
            return False
        return True

    @staticmethod
    def reset_password(reset_token: str, new_password: str) -> None:
        """Reset user password if the token is valid."""
        password_reset = PasswordResetRepository.get_password_reset_by_token(reset_token)
        if not password_reset or password_reset.has_expired():
            raise ValueError("Invalid or expired reset token")

        user = UserRepository.get_user_by_id(password_reset.user_id)
        user.set_password(new_password)
        db.session.commit()

        # Delete used reset token
        PasswordResetRepository.delete_password_reset(password_reset.id)