from flask import Blueprint, request, jsonify
from app.services.update_product_service import UpdateProductService
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository

update_product_blueprint = Blueprint('update_product', __name__)
update_product_service = UpdateProductService(ProductRepository(), CategoryRepository())

@update_product_blueprint.route('/update', methods=['POST'])
def update_product():
    data = request.get_json()
    product_id = data.get('product_id')
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    category_name = data.get('category_name')
    
    if not product_id:
        return jsonify({"message": "Product ID is required"}), 400
    
    try:
        product = update_product_service.update_product(product_id, name, description, price, category_name)
        return jsonify({"name": product.name, "description": product.description, "price": product.price, "category_id": product.category_id}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400