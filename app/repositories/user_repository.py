"""
Repository layer for user data interactions.
"""

from app.models.user import User, db


class UserRepository:
    """Provides User model-related database functionality."""

    @staticmethod
    def create_user(email: str, password: str) -> User:
        """Create and store a new user in the database."""
        new_user = User(email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_email(email: str) -> User | None:
        """Retrieve a user by email."""
        return User.query.filter_by(email=email).first()