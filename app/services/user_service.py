"""
User service: application layer for business logic.
"""

from app.repositories.user_repository import UserRepository


class UserService:
    """Service layer to handle user-related logic."""

    @staticmethod
    def register_user(email: str, password: str) -> dict:
        """Register a new user."""
        if UserRepository.get_user_by_email(email):
            raise ValueError("Email must be unique")
        new_user = UserRepository.create_user(email=email, password=password)
        return {"id": new_user.id, "email": new_user.email}