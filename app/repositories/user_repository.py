"""
Repository layer for User data interaction.
"""

from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    """
    Manages the persistence and retrieval of User instances.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, email: str, password_hash: str) -> User:
        """
        Create a new user entity and persist it in the database.

        Args:
            email (str): User's unique email address.
            password_hash (str): Hashed password for security.

        Returns:
            User: The created User instance.
        """
        new_user = User(email=email, password_hash=password_hash)
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user)
        return new_user

    def get_user_by_email(self, email: str) -> User:
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email address to query.

        Returns:
            User: The User found by email, or None.
        """
        return self.db_session.query(User).filter(User.email == email).first()