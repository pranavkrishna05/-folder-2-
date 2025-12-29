"""
Category Controller handling category management.
"""

from flask import request, jsonify, Blueprint
from products.services.category_service import CategoryService

category_controller = Blueprint("category_controller", __name__)
category_service = CategoryService()

@category_controller.route("/categories", methods=["POST"])
def add_category():
    """
    Endpoint to create a new category.
    Accessible only to admins.
    """
    admin_token = request.headers.get("Admin-Token")
    if not category_service.validate_admin(admin_token):
        return jsonify({"error": "Unauthorized access"}), 403

    data = request.json
    name = data.get("name")
    parent_id = data.get("parent_id")

    if not name:
        return jsonify({"error": "Category name is required"}), 400

    category = category_service.create_category(name, parent_id)
    if category:
        return jsonify(category.dict()), 201

    return jsonify({"error": "Category with the same name already exists"}), 400

@category_controller.route("/categories", methods=["GET"])
def list_categories():
    """
    Endpoint to retrieve all categories.
    """
    categories = category_service.get_all_categories()
    return jsonify([category.dict() for category in categories]), 200