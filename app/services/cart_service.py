"""
Shopping cart service: application layer for business logic.
"""

from app.repositories.shopping_cart_repository import ShoppingCartRepository
from app.repositories.product_repository import ProductRepository


class CartService:
    """Service layer to handle shopping cart logic."""

    @staticmethod
    def get_or_create_cart(user_id: int = None) -> dict:
        """Retrieve or create a shopping cart."""
        cart = ShoppingCartRepository.get_cart_by_user_id(user_id=user_id)
        if not cart:
            cart = ShoppingCartRepository.create_cart(user_id=user_id)
        return cart.to_dict()

    @staticmethod
    def add_to_cart(cart_id: int, product_id: int, quantity: int = 1) -> dict:
        """Add a product to the cart."""
        product = ProductRepository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        item = ShoppingCartRepository.add_item_to_cart(cart_id=cart_id, product_id=product_id, quantity=quantity)
        return item.to_dict()

    @staticmethod
    def remove_item(cart_id: int, item_id: int) -> None:
        """Remove an item from the cart."""
        items = ShoppingCartRepository.get_items_in_cart(cart_id=cart_id)
        if not any(item.id == item_id for item in items):
            raise ValueError("Item not found in cart")
        ShoppingCartRepository.remove_item_from_cart(item_id=item_id)