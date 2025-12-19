# cart_repository.py
from backend.models.cart.cart_item import CartItem
from backend.models import db

class CartRepository:
    def get_by_user_id(self, user_id):
        return CartItem.query.filter_by(user_id=user_id).all()

    def get_by_session_id(self, session_id):
        return CartItem.query.filter_by(session_id=session_id).all()

    def get_by_id(self, item_id):
        return CartItem.query.get(item_id)

    def save(self, cart_item):
        db.session.add(cart_item)
        db.session.commit()

    def delete(self, cart_item):
        db.session.delete(cart_item)
        db.session.commit()
