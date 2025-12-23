"""
Controller layer for shopping cart management routes, specifically item removal.
"""

from flask import Blueprint, jsonify, request
from app.services.cart_service import CartService

cart_blueprint = Blueprint("cart", __name__, url_prefix="/cart")


@cart_blueprint.route("/remove", methods=["DELETE"])
def remove_from_cart():
    """Endpoint to remove an item from the shopping cart."""
    data = request.get_json()
    cart_id = data.get("cart_id")
    item_id = data.get("item_id")
    confirmation = data.get("confirm")

    if not cart_id or not item_id:
        return jsonify({"error": "Cart ID and Item ID are required"}), 400

    if confirmation != "true":
        return jsonify({"error": "Confirmation is required"}), 400

    try:
        updated_cart = CartService.remove_item(cart_id=cart_id, item_id=item_id)
        return jsonify(updated_cart), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404