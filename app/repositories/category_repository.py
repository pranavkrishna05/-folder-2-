"""
Repository layer for category data interactions.
"""

from app.models.category import Category, db


class CategoryRepository:
    """Provides Category model-related database functionality."""

    @staticmethod
    def add_category(name: str) -> Category:
        """Add a new category to the database."""
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_category_by_id(category_id: int) -> Category | None:
        """Retrieve category by its ID."""
        return Category.query.get(category_id)

    @staticmethod
    def get_all_categories() -> list[Category]:
        """Retrieve all categories."""
        return Category.query.all()