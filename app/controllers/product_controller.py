from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository

product_blueprint = Blueprint('product', __name__)
product_service = ProductService(ProductRepository(), CategoryRepository())

@product_blueprint.route('/add', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_name = data.get('category_name')
    
    if not name or not description or price is None or not category_name:
        return jsonify({"message": "All fields are required"}), 400
    
    try:
        product = product_service.add_product(name, description, price, category_name)
        return jsonify({"name": product.name, "description": product.description, "price": product.price}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400