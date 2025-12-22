from typing import Optional
from app.models.shopping_cart import ShoppingCart, ShoppingCartItem
from app import db

class ShoppingCartRepository:
    """
    Repository class for interacting with the ShoppingCart model.
    """
    
    def find_by_user_id(self, user_id: int) -> Optional[ShoppingCart]:
        return ShoppingCart.query.filter_by(user_id=user_id).first()

    def find_by_id(self, cart_id: int) -> Optional[ShoppingCart]:
        return ShoppingCart.query.get(cart_id)
    
    def save(self, shopping_cart: ShoppingCart) -> None:
        db.session.add(shopping_cart)
        db.session.commit()

    def save_item(self, shopping_cart_item: ShoppingCartItem) -> None:
        db.session.add(shopping_cart_item)
        db.session.commit()
    
    def delete_item(self, shopping_cart_item: ShoppingCartItem) -> None:
        db.session.delete(shopping_cart_item)
        db.session.commit()