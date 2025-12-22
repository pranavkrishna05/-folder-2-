"""
Account model definition.
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from app.config.db_config import Base

class Account(Base):
    """
    Represents an account entity tied to a user.

    Attributes:
        id: Unique identifier for the account.
        user_id: Foreign key linking the account to a user.
        account_name: Name of the account.
    """
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_name = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<Account(id={self.id}, account_name={self.account_name})>"