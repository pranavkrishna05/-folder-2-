"""
Search service: application layer for search logic.
"""

from app.repositories.product_repository import ProductRepository


class SearchService:
    """Service layer to handle search-related logic."""

    @staticmethod
    def search(keyword: str, category: str = None, page: int = 1, per_page: int = 10) -> dict:
        """Search for products in the inventory."""
        if not keyword.strip():
            raise ValueError("Search keyword cannot be empty")
        return ProductRepository.search_products(
            keyword=keyword, category=category, page=page, per_page=per_page
        )