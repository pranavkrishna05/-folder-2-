"""
ShoppingCart model definition with persistent cart state.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class ShoppingCart(db.Model):
    """Representation of a shopping cart."""

    __tablename__ = "shopping_carts"

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=True, unique=True)
    total_price: float = Column(Float, default=0.0)
    cart_items = relationship("CartItem", backref="shopping_cart", cascade="all, delete-orphan")

    def update_total_price(self):
        """Update the total price of the shopping cart."""
        self.total_price = sum(item.quantity * item.product.price for item in self.cart_items)
        db.session.commit()

    def to_dict(self):
        """Convert ShoppingCart object to dictionary."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total_price": self.total_price,
            "cart_items": [item.to_dict() for item in self.cart_items],
        }


class CartItem(db.Model):
    """Representation of a single product in the shopping cart."""

    __tablename__ = "cart_items"

    id: int = Column(Integer, primary_key=True)
    product_id: int = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: int = Column(Integer, nullable=False)
    shopping_cart_id: int = Column(Integer, ForeignKey("shopping_carts.id"), nullable=False)

    product = relationship("Product")  # Linking Product model for price and details

    def to_dict(self):
        """Convert CartItem object to dictionary."""
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "product": self.product.to_dict() if self.product else None,
        }