"""
Product model definition linked with categories.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Product(db.Model):
    """Representation of a product in the inventory."""

    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), unique=True, nullable=False)
    price: float = Column(Float, nullable=False)
    description: str = Column(String(255), nullable=False)
    category_id: int = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category: "Category" = relationship("Category", backref="products")

    def to_dict(self) -> dict:
        """Convert Product object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "category": self.category.to_dict() if self.category else None,
        }