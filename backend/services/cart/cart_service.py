# cart_service.py
from backend.repositories.cart.cart_repository import CartRepository
from backend.repositories.products.product_repository import ProductRepository

class CartService:
    def __init__(self, cart_repository, product_repository):
        self.cart_repository = cart_repository
        self.product_repository = product_repository

    def add_to_cart(self, data):
        product = self.product_repository.get_by_id(data['product_id'])
        if not product or product.is_deleted:
            raise ValueError('Product not found or is deleted')
        cart_item = CartItem(
            user_id=data.get('user_id'),
            session_id=data.get('session_id'),
            product_id=data['product_id'],
            quantity=data['quantity']
        )
        self.cart_repository.save(cart_item)
        return cart_item

    def view_cart(self, user_id=None, session_id=None):
        if user_id:
            return self.cart_repository.get_by_user_id(user_id)
        elif session_id:
            return self.cart_repository.get_by_session_id(session_id)
        else:
            raise ValueError('Either user_id or session_id must be provided')

    def remove_from_cart(self, item_id):
        cart_item = self.cart_repository.get_by_id(item_id)
        if not cart_item:
            raise ValueError('Cart item not found')
        self.cart_repository.delete(cart_item)
