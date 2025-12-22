from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService
from app.repositories.category_repository import CategoryRepository

category_blueprint = Blueprint('category', __name__)
category_service = CategoryService(CategoryRepository())

@category_blueprint.route('/create', methods=['POST'])
def create_category():
    data = request.get_json()
    name = data.get('name')
    parent_category_id = data.get('parent_category_id')
    
    if not name:
        return jsonify({"message": "Category name is required"}), 400
    
    try:
        category = category_service.create_category(name, parent_category_id)
        return jsonify({"name": category.name, "parent_category_id": category.parent_category_id}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@category_blueprint.route('/update', methods=['POST'])
def update_category():
    data = request.get_json()
    category_id = data.get('category_id')
    name = data.get('name')
    parent_category_id = data.get('parent_category_id')
    
    if not category_id:
        return jsonify({"message": "Category ID is required"}), 400
    
    try:
        category = category_service.update_category(category_id, name, parent_category_id)
        return jsonify({"name": category.name, "parent_category_id": category.parent_category_id}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@category_blueprint.route('/delete', methods=['POST'])
def delete_category():
    data = request.get_json()
    category_id = data.get('category_id')
    
    if not category_id:
        return jsonify({"message": "Category ID is required"}), 400
    
    try:
        category_service.delete_category(category_id)
        return jsonify({"message": "Category successfully deleted"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400