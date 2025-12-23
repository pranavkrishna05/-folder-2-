"""
Controller layer for product-related API endpoints.
"""

from flask import Blueprint, jsonify, request
from app.services.product_service import ProductService

product_blueprint = Blueprint("product", __name__, url_prefix="/product")


@product_blueprint.route("/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id: int):
    """Endpoint for admins to delete products."""
    confirmation = request.args.get("confirm")
    if confirmation != "true":
        return jsonify({"error": "Deletion requires confirmation"}), 400

    try:
        ProductService.delete_product(product_id=product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404