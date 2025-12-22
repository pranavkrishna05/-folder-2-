from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class DeleteProductService:
    """
    Service class for managing product deletion operations.
    """
    
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository
    
    def delete_product(self, product_id: int) -> None:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        self.product_repository.delete(product)