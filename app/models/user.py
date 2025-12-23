"""
User model definition.
"""

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class User(db.Model):
    """Representation of a user account."""

    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(120), unique=True, nullable=False)
    password_hash: str = Column(String(200), nullable=False)

    def set_password(self, password: str) -> None:
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verify the user's password."""
        return check_password_hash(self.password_hash, password)