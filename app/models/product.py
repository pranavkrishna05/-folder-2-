"""
Product model definition.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

db = SQLAlchemy()


class Product(db.Model):
    """Representation of a product in the inventory."""

    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), unique=True, nullable=False)
    price: float = Column(Float, nullable=False)
    description: str = Column(String(255), nullable=False)

    def update_product(self, price: float = None, description: str = None) -> None:
        """Update product details."""
        if price is not None:
            if not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("Price must be a positive numeric value")
            self.price = price
        if description is not None:
            if description.strip() == "":
                raise ValueError("Description cannot be removed")
            self.description = description