"""
Product model definition with support for soft deletion.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean

db = SQLAlchemy()


class Product(db.Model):
    """Representation of a product in the inventory."""

    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), unique=True, nullable=False)
    price: float = Column(Float, nullable=False)
    description: str = Column(String(255), nullable=False)
    is_deleted: bool = Column(Boolean, default=False)  # Field for soft deletion

    def delete_product(self) -> None:
        """Mark the product as deleted."""
        self.is_deleted = True