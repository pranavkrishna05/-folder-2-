from flask import Blueprint, request, jsonify
from app.services.delete_product_service import DeleteProductService
from app.repositories.product_repository import ProductRepository

delete_product_blueprint = Blueprint('delete_product', __name__)
delete_product_service = DeleteProductService(ProductRepository())

@delete_product_blueprint.route('/delete', methods=['POST'])
def delete_product():
    data = request.get_json()
    product_id = data.get('product_id')
    
    if not product_id:
        return jsonify({"message": "Product ID is required"}), 400
    
    try:
        delete_product_service.delete_product(product_id)
        return jsonify({"message": "Product successfully deleted"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400