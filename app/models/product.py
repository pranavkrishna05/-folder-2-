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
    category_id: int = Column(Integer, nullable=False)

    def __init__(self, name: str, price: float, description: str, category_id: int):
        if price <= 0:
            raise ValueError("Price must be a positive number")
        if not description:
            raise ValueError("Description cannot be empty")
        self.name = name
        self.price = price
        self.description = description
        self.category_id = category_id