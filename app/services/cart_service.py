"""
Shopping cart service: application layer for business logic related to item removal.
"""

from app.repositories.shopping_cart_repository import ShoppingCartRepository


class CartService:
    """Service layer to handle shopping cart logic."""

    @staticmethod
    def remove_item(cart_id: int, item_id: int) -> dict:
        """Remove an item from the cart and update the total price."""
        cart = ShoppingCartRepository.get_cart_by_id(cart_id)
        if not cart:
            raise ValueError("Shopping cart not found")

        items = ShoppingCartRepository.get_items_in_cart(cart_id=cart_id)
        if not any(item.id == item_id for item in items):
            raise ValueError("Item not found in cart")

        ShoppingCartRepository.remove_item_from_cart(cart_id=cart_id, item_id=item_id)
        return cart.to_dict()