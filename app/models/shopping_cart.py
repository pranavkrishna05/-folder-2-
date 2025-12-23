"""
ShoppingCart model definition.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class ShoppingCart(db.Model):
    """Representation of a shopping cart."""

    __tablename__ = "shopping_carts"

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=True)
    cart_items = relationship("CartItem", backref="shopping_cart", cascade="all, delete-orphan")

    def to_dict(self) -> dict:
        """Convert ShoppingCart object to dictionary."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "cart_items": [item.to_dict() for item in self.cart_items],
        }


class CartItem(db.Model):
    """Representation of a single product in the shopping cart."""

    __tablename__ = "cart_items"

    id: int = Column(Integer, primary_key=True)
    product_id: int = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: int = Column(Integer, nullable=False)
    shopping_cart_id: int = Column(Integer, ForeignKey("shopping_carts.id"), nullable=False)

    def to_dict(self) -> dict:
        """Convert CartItem object to dictionary."""
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity,
        }