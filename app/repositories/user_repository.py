"""
User Repository: Provides abstraction for database operations for User entities.
"""

from typing import Optional
from app.models.user import User, db

class UserRepository:
    """Encapsulates database operations for User management."""

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Fetch a user by their email."""
        return User.query.filter_by(email=email).first()

    def create_user(self, email: str, password_hash: str) -> User:
        """Create a new user in the database."""
        new_user = User(email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return new_user