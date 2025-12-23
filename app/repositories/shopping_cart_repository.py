"""
Repository layer for shopping cart data interactions.
"""

from app.models.shopping_cart import ShoppingCart, CartItem, db


class ShoppingCartRepository:
    """Provides ShoppingCart model-related database functionality."""

    @staticmethod
    def get_cart_by_user_id(user_id: int) -> ShoppingCart | None:
        """Retrieve a shopping cart by user ID."""
        return ShoppingCart.query.filter_by(user_id=user_id).first()

    @staticmethod
    def create_cart(user_id: int = None) -> ShoppingCart:
        """Create a new shopping cart."""
        cart = ShoppingCart(user_id=user_id)
        db.session.add(cart)
        db.session.commit()
        return cart

    @staticmethod
    def add_item_to_cart(cart_id: int, product_id: int, quantity: int) -> CartItem:
        """Add an item to the shopping cart."""
        item = CartItem(product_id=product_id, quantity=quantity, shopping_cart_id=cart_id)
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def get_items_in_cart(cart_id: int) -> list[CartItem]:
        """Retrieve all items in a shopping cart."""
        cart = ShoppingCart.query.get(cart_id)
        return cart.cart_items if cart else []

    @staticmethod
    def remove_item_from_cart(item_id: int) -> None:
        """Remove an item from the shopping cart."""
        item = CartItem.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()