"""
Shopping cart service: application layer for business logic related to quantity modification.
"""

from app.repositories.shopping_cart_repository import ShoppingCartRepository


class CartService:
    """Service layer to handle shopping cart logic."""

    @staticmethod
    def modify_item_quantity(cart_id: int, item_id: int, new_quantity: int) -> dict:
        """Modify the quantity of an item in the cart and update the total price."""
        cart = ShoppingCartRepository.get_cart_by_id(cart_id)
        if not cart:
            raise ValueError("Shopping cart not found")

        items = ShoppingCartRepository.get_items_in_cart(cart_id=cart_id)
        if not any(item.id == item_id for item in items):
            raise ValueError("Item not found in cart")

        ShoppingCartRepository.modify_item_quantity(cart_id=cart_id, item_id=item_id, new_quantity=new_quantity)
        return cart.to_dict()