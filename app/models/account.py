"""
Account model defining the structure of the Account entity linked to a user.
"""

from app.config.db_config import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Account(Base):
    """
    Represents an account associated with a user, capable of storing specific user-related data.
    """
    __tablename__ = "accounts"

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_name: str = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"<Account {self.account_name}>"