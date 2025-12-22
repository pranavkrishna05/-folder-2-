from typing import Optional
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository

class UpdateProductService:
    """
    Service class for managing product update operations.
    """
    
    def __init__(self, product_repository: ProductRepository, category_repository: CategoryRepository) -> None:
        self.product_repository = product_repository
        self.category_repository = category_repository
    
    def update_product(self, product_id: int, name: Optional[str] = None, description: Optional[str] = None, price: Optional[float] = None, category_name: Optional[str] = None) -> Product:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        
        if name and self.product_repository.find_by_name(name):
            raise ValueError("Product name must be unique")
        if price is not None and price <= 0:
            raise ValueError("Product price must be a positive number")
        if description and not description.strip():
            raise ValueError("Product description cannot be empty")
        
        if name:
            product.name = name
        if description:
            product.description = description
        if price is not None:
            product.price = price
        
        if category_name:
            category = self.category_repository.find_by_name(category_name)
            if not category:
                raise ValueError("Specified category does not exist")
            product.category_id = category.id
        
        self.product_repository.save(product)
        return product