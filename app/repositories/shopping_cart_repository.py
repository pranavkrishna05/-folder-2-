"""
Repository layer for shopping cart data interactions, enhancing persistence across user sessions.
"""

from app.models.shopping_cart import ShoppingCart, CartItem, db


class ShoppingCartRepository:
    """Provides ShoppingCart model-related database functionality."""

    @staticmethod
    def get_cart_by_user_id(user_id: int) -> ShoppingCart | None:
        """Retrieve a shopping cart by user ID."""
        return ShoppingCart.query.filter_by(user_id=user_id).first()

    @staticmethod
    def create_cart_for_user(user_id: int) -> ShoppingCart:
        """Create a shopping cart for a user."""
        existing_cart = ShoppingCartRepository.get_cart_by_user_id(user_id)
        if existing_cart:
            return existing_cart

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
        cart = ShoppingCart.query.get(cart_id)
        cart.update_total_price()
        return item

    @staticmethod
    def get_items_in_cart(cart_id: int) -> list[CartItem]:
        """Retrieve all items in a shopping cart."""
        cart = ShoppingCart.query.get(cart_id)
        return cart.cart_items if cart else []