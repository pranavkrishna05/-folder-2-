"""
Repository layer for category data interactions.
"""

from app.models.category import Category, db


class CategoryRepository:
    """Provides Category model-related database functionality."""

    @staticmethod
    def add_category(name: str, parent_id: int = None) -> Category:
        """Add a new category."""
        category = Category(name=name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_category_by_id(category_id: int) -> Category | None:
        """Retrieve a category by its ID."""
        return Category.query.get(category_id)

    @staticmethod
    def get_all_categories() -> list[Category]:
        """Retrieve all categories."""
        return Category.query.all()

    @staticmethod
    def update_category(category_id: int, name: str = None, parent_id: int = None) -> None:
        """Update an existing category."""
        category = CategoryRepository.get_category_by_id(category_id)
        if category:
            if name:
                category.name = name
            if parent_id is not None:
                category.parent_id = parent_id
            db.session.commit()