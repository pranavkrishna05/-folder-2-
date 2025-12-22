from typing import List, Dict, Any
from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class SearchProductService:
    """
    Service class for managing product search operations.
    """
    
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository
    
    def search_products(self, query: str, page: int = 1, per_page: int = 10) -> Dict[str, Any]:
        products = self.product_repository.search_by_query(query, page, per_page)
        total_products = self.product_repository.count_by_query(query)
        
        return {
            "products": products,
            "total": total_products,
            "page": page,
            "per_page": per_page
        }