# cart_management.py
from flask import request, jsonify
from flask.views import MethodView
from backend.repositories.cart.cart_repository import CartRepository
from backend.repositories.products.product_repository import ProductRepository
from backend.services.cart.cart_service import CartService

class AddToCartAPI(MethodView):
    def post(self):
        data = request.get_json()
        cart_repository = CartRepository()
        product_repository = ProductRepository()
        cart_service = CartService(cart_repository, product_repository)
        cart_item = cart_service.add_to_cart(data)
        return jsonify(cart_item.to_dict()), 201

class ViewCartAPI(MethodView):
    def get(self):
        user_id = request.args.get('user_id')
        cart_repository = CartRepository()
        cart_service = CartService(cart_repository)
        cart_items = cart_service.view_cart(user_id)
        return jsonify([item.to_dict() for item in cart_items]), 200

class RemoveFromCartAPI(MethodView):
    def delete(self, item_id):
        cart_repository = CartRepository()
        cart_service = CartService(cart_repository)
        cart_service.remove_from_cart(item_id)
        return jsonify({'message': 'Item removed from cart successfully'}), 200
