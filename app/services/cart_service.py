"""
Shopping cart service: application layer for persistent cart state management.
"""

from app.repositories.shopping_cart_repository import ShoppingCartRepository
from app.repositories.product_repository import ProductRepository


class CartService:
    """Service layer to handle shopping cart logic."""

    @staticmethod
    def get_or_create_user_cart(user_id: int) -> dict:
        """Retrieve or create a persistent shopping cart for a user."""
        if not user_id:
            raise ValueError("User ID is required for retrieving or creating a cart")

        cart = ShoppingCartRepository.get_cart_by_user_id(user_id)
        if not cart:
            cart = ShoppingCartRepository.create_cart_for_user(user_id)
        return cart.to_dict()

    @staticmethod
    def add_to_cart(cart_id: int, product_id: int, quantity: int = 1) -> dict:
        """Add an item to the user's shopping cart."""
        product = ProductRepository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        item = ShoppingCartRepository.add_item_to_cart(cart_id=cart_id, product_id=product_id, quantity=quantity)
        return item.to_dict()