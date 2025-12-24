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

    @staticmethod
    def remove_item_from_cart(cart_id: int, item_id: int) -> bool:
        """Remove an item from the shopping cart."""
        cart = ShoppingCart.query.get(cart_id)
        if not cart:
            return False

        item = next((i for i in cart.cart_items if i.id == item_id), None)
        if item:
            db.session.delete(item)
            db.session.commit()
            cart.update_total_price()
            return True
        return False

    @staticmethod
    def clear_cart(cart_id: int) -> bool:
        """Clear all items from a shopping cart."""
        cart = ShoppingCart.query.get(cart_id)
        if not cart:
            return False

        for item in cart.cart_items:
            db.session.delete(item)
        db.session.commit()
        cart.update_total_price()
        return True

    @staticmethod
    def update_item_quantity(cart_id: int, item_id: int, quantity: int) -> bool:
        """Update the quantity of an item in the cart."""
        cart = ShoppingCart.query.get(cart_id)
        if not cart:
            return False

        item = next((i for i in cart.cart_items if i.id == item_id), None)
        if item:
            item.quantity = quantity
            db.session.commit()
            cart.update_total_price()
            return True
        return False
