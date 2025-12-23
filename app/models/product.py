"""
Product model definition with support for search functionality.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

db = SQLAlchemy()


class Product(db.Model):
    """Representation of a product in the inventory."""

    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), nullable=False)
    price: float = Column(Float, nullable=False)
    description: str = Column(String(255), nullable=False)
    category_name: str = Column(String(50), nullable=False)

    def to_dict(self) -> dict:
        """Convert Product object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "category_name": self.category_name,
        }