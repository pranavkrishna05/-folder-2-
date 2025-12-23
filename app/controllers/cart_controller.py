"""
Controller layer for shopping cart management routes, focusing on persistence.
"""

from flask import Blueprint, jsonify, request
from app.services.cart_service import CartService

cart_blueprint = Blueprint("cart", __name__, url_prefix="/cart")


@cart_blueprint.route("/get", methods=["GET"])
def get_user_cart():
    """Endpoint to retrieve or create a persistent shopping cart for a user."""
    user_id = request.args.get("user_id", type=int)

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        cart = CartService.get_or_create_user_cart(user_id=user_id)
        return jsonify(cart), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@cart_blueprint.route("/add", methods=["POST"])
def add_to_cart():
    """Endpoint to add items to a persistent shopping cart."""
    data = request.get_json()
    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    if not user_id or not product_id:
        return jsonify({"error": "User ID and Product ID are required"}), 400

    try:
        cart = CartService.get_or_create_user_cart(user_id=user_id)
        item = CartService.add_to_cart(cart_id=cart["id"], product_id=product_id, quantity=quantity)
        return jsonify(item), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 404