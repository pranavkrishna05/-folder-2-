"""
Controller layer for shopping cart management routes.
"""

from flask import Blueprint, jsonify, request
from app.services.cart_service import CartService

cart_blueprint = Blueprint("cart", __name__, url_prefix="/cart")


@cart_blueprint.route("/get", methods=["GET"])
def get_cart():
    """Endpoint to retrieve or create a shopping cart."""
    user_id = request.args.get("user_id", type=int)  # Can be None for guests

    try:
        cart = CartService.get_or_create_cart(user_id=user_id)
        return jsonify(cart), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@cart_blueprint.route("/add", methods=["POST"])
def add_to_cart():
    """Endpoint to add a product to the shopping cart."""
    data = request.get_json()
    cart_id = data.get("cart_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    if not cart_id or not product_id:
        return jsonify({"error": "Cart ID and Product ID are required"}), 400

    try:
        item = CartService.add_to_cart(cart_id=cart_id, product_id=product_id, quantity=quantity)
        return jsonify(item), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@cart_blueprint.route("/remove", methods=["DELETE"])
def remove_from_cart():
    """Endpoint to remove an item from the shopping cart."""
    data = request.get_json()
    cart_id = data.get("cart_id")
    item_id = data.get("item_id")

    if not cart_id or not item_id:
        return jsonify({"error": "Cart ID and Item ID are required"}), 400

    try:
        CartService.remove_item(cart_id=cart_id, item_id=item_id)
        return jsonify({"message": "Item removed successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404