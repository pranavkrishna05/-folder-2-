from typing import Optional
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository

class ProductService:
    """
    Service class for managing product operations.
    """
    
    def __init__(self, product_repository: ProductRepository, category_repository: CategoryRepository) -> None:
        self.product_repository = product_repository
        self.category_repository = category_repository
    
    def add_product(self, name: str, description: str, price: float, category_name: str) -> Product:
        if self.product_repository.find_by_name(name):
            raise ValueError("Product name must be unique")
        if price <= 0:
            raise ValueError("Product price must be a positive number")
        if not description:
            raise ValueError("Product description cannot be empty")
        
        category = self.category_repository.find_by_name(category_name)
        if not category:
            raise ValueError("Specified category does not exist")
        
        new_product = Product(name=name, description=description, price=price, category_id=category.id)
        self.product_repository.save(new_product)
        return new_product