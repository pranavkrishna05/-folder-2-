from flask import Blueprint, request, jsonify
from app.services.shopping_cart_service import ShoppingCartService
from app.repositories.shopping_cart_repository import ShoppingCartRepository
from app.repositories.product_repository import ProductRepository

shopping_cart_blueprint = Blueprint('shopping_cart', __name__)
shopping_cart_service = ShoppingCartService(ShoppingCartRepository(), ProductRepository())

@shopping_cart_blueprint.route('/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    
    if not product_id or quantity is None:
        return jsonify({"message": "Product ID and quantity are required"}), 400
    
    try:
        shopping_cart = shopping_cart_service.add_product(user_id, product_id, quantity)
        return jsonify({"cart_id": shopping_cart.id, "product_id": product_id, "quantity": quantity}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@shopping_cart_blueprint.route('/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    
    if not product_id:
        return jsonify({"message": "Product ID is required"}), 400
    
    try:
        shopping_cart = shopping_cart_service.remove_product(user_id, product_id)
        return jsonify({"message": "Product successfully removed from cart"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@shopping_cart_blueprint.route('/modify', methods=['POST'])
def modify_quantity_in_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    
    if not product_id or quantity is None:
        return jsonify({"message": "Product ID and quantity are required"}), 400
    
    try:
        shopping_cart = shopping_cart_service.modify_quantity(user_id, product_id, quantity)
        return jsonify({"message": "Product quantity successfully updated"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400