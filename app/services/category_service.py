"""
Category service: application layer for business logic.
"""

from app.repositories.category_repository import CategoryRepository


class CategoryService:
    """Service layer to handle category-related logic."""

    @staticmethod
    def add_category(name: str, parent_id: int = None) -> dict:
        """Create a new category."""
        if not name.strip():
            raise ValueError("Category name cannot be empty")

        category = CategoryRepository.add_category(name=name, parent_id=parent_id)
        return category.to_dict()

    @staticmethod
    def update_category(category_id: int, name: str = None, parent_id: int = None) -> dict:
        """Update an existing category."""
        category = CategoryRepository.get_category_by_id(category_id)
        if not category:
            raise ValueError("Category not found")

        CategoryRepository.update_category(category_id=category.id, name=name, parent_id=parent_id)
        return category.to_dict()

    @staticmethod
    def get_all_categories() -> list[dict]:
        """Retrieve all categories."""
        categories = CategoryRepository.get_all_categories()
        return [category.to_dict() for category in categories]