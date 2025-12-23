"""
Repository layer for shopping cart data interactions, including quantity modification and total price update.
"""

from app.models.shopping_cart import ShoppingCart, CartItem, db


class ShoppingCartRepository:
    """Provides ShoppingCart model-related database functionality."""

    @staticmethod
    def get_cart_by_id(cart_id: int) -> ShoppingCart | None:
        """Retrieve a shopping cart by its ID."""
        return ShoppingCart.query.get(cart_id)

    @staticmethod
    def modify_item_quantity(cart_id: int, item_id: int, new_quantity: int) -> None:
        """Modify the quantity of an item in the shopping cart."""
        cart = ShoppingCartRepository.get_cart_by_id(cart_id)
        if not cart:
            raise ValueError("Shopping cart not found")

        item = CartItem.query.get(item_id)
        if not item:
            raise ValueError("Item not found in cart")

        if new_quantity < 1:
            raise ValueError("Quantity must be a positive integer")

        item.quantity = new_quantity
        db.session.commit()
        cart.update_total_price()

    @staticmethod
    def get_items_in_cart(cart_id: int) -> list[CartItem]:
        """Retrieve all items in a shopping cart."""
        cart = ShoppingCart.query.get(cart_id)
        return cart.cart_items if cart else []