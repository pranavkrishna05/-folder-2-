"""
Repository layer for shopping cart data interactions, including item removal and total price update.
"""

from app.models.shopping_cart import ShoppingCart, CartItem, db


class ShoppingCartRepository:
    """Provides ShoppingCart model-related database functionality."""

    @staticmethod
    def get_cart_by_user_id(user_id: int) -> ShoppingCart | None:
        """Retrieve a shopping cart by user ID."""
        return ShoppingCart.query.filter_by(user_id=user_id).first()

    @staticmethod
    def get_cart_by_id(cart_id: int) -> ShoppingCart | None:
        """Retrieve a shopping cart by its ID."""
        return ShoppingCart.query.get(cart_id)

    @staticmethod
    def remove_item_from_cart(cart_id: int, item_id: int) -> None:
        """Remove an item from the shopping cart."""
        cart = ShoppingCartRepository.get_cart_by_id(cart_id)
        if not cart:
            raise ValueError("Shopping cart not found")
        
        item = CartItem.query.get(item_id)
        if not item:
            raise ValueError("Item not found in cart")

        db.session.delete(item)
        cart.update_total_price()

    @staticmethod
    def get_items_in_cart(cart_id: int) -> list[CartItem]:
        """Retrieve all items in a shopping cart."""
        cart = ShoppingCart.query.get(cart_id)
        return cart.cart_items if cart else []