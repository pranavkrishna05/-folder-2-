# product_management.py
from flask import request, jsonify
from flask.views import MethodView
from backend.repositories.products.product_repository import ProductRepository
from backend.services.products.product_service import ProductService

class AddProductAPI(MethodView):
    def post(self):
        data = request.get_json()
        product_repository = ProductRepository()
        product_service = ProductService(product_repository)
        product = product_service.add_product(data)
        return jsonify(product.to_dict()), 201

class UpdateProductAPI(MethodView):
    def put(self, product_id):
        data = request.get_json()
        product_repository = ProductRepository()
        product_service = ProductService(product_repository)
        product = product_service.update_product(product_id, data)
        return jsonify(product.to_dict()), 200

class DeleteProductAPI(MethodView):
    def delete(self, product_id):
        product_repository = ProductRepository()
        product_service = ProductService(product_repository)
        product_service.delete_product(product_id)
        return jsonify({'message': 'Product deleted successfully'}), 200
