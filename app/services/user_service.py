"""
User Service: Implements business logic related to User management.
"""

import bcrypt
from app.repositories.user_repository import UserRepository
from app.models.user import User

class UserService:
    """Service layer for user-related business logic."""

    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user."""
        existing_user = self.user_repository.get_user_by_email(email)
        if existing_user:
            raise ValueError(f"User with email {email} already exists.")

        # Password hashing
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return self.user_repository.create_user(email=email, password_hash=hashed_password)