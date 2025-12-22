"""
Service layer for user authentication and session management.
"""

import secrets
import datetime
from app.repositories.session_repository import SessionRepository
from app.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class AuthenticationService:
    """
    Provides authentication logic and session handling.
    """

    def __init__(self, user_repository: UserRepository, session_repository: SessionRepository):
        self.user_repository = user_repository
        self.session_repository = session_repository

    def authenticate_user(self, email: str, password: str) -> dict:
        """
        Authenticate a user based on email and password.

        Args:
            email: User's email address.
            password: Plain-text password.

        Returns:
            dict: Login success or error details.
        """
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return {"error": "Invalid email or password"}

        # Mock for password validation; replace with actual hashed password comparison.
        if user.password_hash != password:  
            return {"error": "Invalid email or password"}

        token = secrets.token_hex(16)
        expiration = (datetime.datetime.now() + datetime.timedelta(hours=2)).isoformat()
        session = self.session_repository.create_session(user_id=user.id, token=token, expiration=expiration)
        return {"message": "Login successful", "token": session.token}