# product_service.py
from backend.repositories.products.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def add_product(self, data):
        if self.product_repository.get_by_name(data['name']):
            raise ValueError('Product name must be unique')
        if data['price'] <= 0:
            raise ValueError('Product price must be a positive number')
        if not data['description']:
            raise ValueError('Product description cannot be empty')
        product = Product(
            name=data['name'],
            description=data['description'],
            price=data['price']
        )
        self.product_repository.save(product)
        return product

    def update_product(self, product_id, data):
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise ValueError('Product not found')
        if 'name' in data and product.name != data['name']:
            if self.product_repository.get_by_name(data['name']):
                raise ValueError('Product name must be unique')
            product.name = data['name']
        if 'price' in data:
            if data['price'] <= 0:
                raise ValueError('Product price must be a positive number')
            product.price = data['price']
        if 'description' in data:
            if not data['description']:
                raise ValueError('Product description cannot be empty')
            product.description = data['description']
        self.product_repository.save(product)
        return product
