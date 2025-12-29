"""
Password reset service for managing password recovery process.
"""

from datetime import datetime, timedelta
import uuid

from auth.models.password_reset_model import PasswordReset
from auth.services.user_service import UserService

class PasswordResetService:
    """
    Handles password reset token creation and validation.
    """

    def __init__(self):
        self.reset_tokens = {}  # Mock in-memory storage for reset tokens
        self.user_service = UserService()

    def create_reset_token(self, email: str) -> str | None:
        """
        Creates a password reset token for the user.
        """
        user = self.user_service.get_user_by_email(email)
        if user:
            token = str(uuid.uuid4())
            expiration_time = datetime.now() + timedelta(hours=24)
            self.reset_tokens[token] = PasswordReset(token=token, user_id=user.id, expires_at=expiration_time)
            return token
        return None

    def reset_password(self, token: str, new_password: str) -> bool:
        """
        Resets the password if the token is valid and not expired.
        """
        reset_info = self.reset_tokens.get(token)
        if reset_info and reset_info.expires_at > datetime.now():
            self.user_service.update_password(reset_info.user_id, new_password)
            del self.reset_tokens[token]
            return True
        return False