"""
Service layer handling User business logic.
"""

import bcrypt
from app.repositories.user_repository import UserRepository

class UserService:
    """
    Provides functionality for validating and managing users.
    """

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, email: str, password: str) -> dict:
        """
        Handle user registration by validating and creating them securely.

        Args:
            email (str): User's unique email.
            password (str): Plain text password.

        Returns:
            dict: Confirmation of successful registration or errors.
        """
        if self.user_repository.get_user_by_email(email):
            return {"error": "Email must be unique"}
        
        if len(password) < 8 or not any(char.isdigit() for char in password):
            return {"error": "Password must meet security criteria"}

        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = self.user_repository.create_user(email=email, password_hash=password_hash.decode('utf-8'))
        return {"message": f"User {user.email} registered successfully"}