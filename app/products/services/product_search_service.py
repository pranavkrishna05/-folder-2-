"""
Service for managing product search functionality.
"""

from products.models.product_model import Product
from db.database import Database


class ProductSearchService:
    """
    Handles search logic for the product catalog.
    """

    def __init__(self):
        self.db = Database()

    def search_products(self, query: str, page: int, per_page: int) -> list[Product]:
        """
        Searches products in the database matching the query.
        Returns paginated results.
        """
        product_records = self.db.search_products(query, page, per_page)
        return [Product(**record) for record in product_records]