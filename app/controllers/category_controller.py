"""
Controller layer for category management routes.
"""

from flask import Blueprint, jsonify, request
from app.services.category_service import CategoryService

category_blueprint = Blueprint("category", __name__, url_prefix="/category")


@category_blueprint.route("/add", methods=["POST"])
def add_category():
    """Endpoint to add a new category."""
    data = request.get_json()
    name = data.get("name")
    parent_id = data.get("parent_id")

    if not name:
        return jsonify({"error": "Category name is required"}), 400

    try:
        category_data = CategoryService.add_category(name=name, parent_id=parent_id)
        return jsonify(category_data), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@category_blueprint.route("/update/<int:category_id>", methods=["PUT"])
def update_category(category_id: int):
    """Endpoint to update an existing category."""
    data = request.get_json()
    name = data.get("name")
    parent_id = data.get("parent_id")

    try:
        category_data = CategoryService.update_category(category_id=category_id, name=name, parent_id=parent_id)
        return jsonify(category_data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@category_blueprint.route("/", methods=["GET"])
def get_all_categories():
    """Endpoint to retrieve all categories."""
    categories = CategoryService.get_all_categories()
    return jsonify(categories), 200