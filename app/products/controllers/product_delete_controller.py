"""
Product Controller for handling deletion of products from the catalog.
"""

from flask import request, jsonify, Blueprint
from products.services.product_delete_service import ProductDeleteService

product_delete_controller = Blueprint("product_delete_controller", __name__)
product_delete_service = ProductDeleteService()

@product_delete_controller.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """
    Endpoint to delete a product from the catalog.
    Requires admin authentication.
    """
    admin_token = request.headers.get("Admin-Token")
    
    if not admin_token or not product_delete_service.validate_admin(admin_token):
        return jsonify({"error": "Unauthorized access"}), 403

    confirmation = request.json.get("confirmation")
    if confirmation != "YES":
        return jsonify({"error": "Deletion requires explicit confirmation"}), 400

    deleted = product_delete_service.delete_product(product_id)
    if deleted:
        return jsonify({"message": "Product successfully deleted"}), 200

    return jsonify({"error": "Product not found or deletion failed"}), 404