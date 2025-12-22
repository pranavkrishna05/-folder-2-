"""
User model defining the structure of the User entity.
"""

from app.config.db_config import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    """
    Represents a registered user with personal information and credentials.
    """
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String, unique=True, nullable=False)
    password_hash: str = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.email}>"