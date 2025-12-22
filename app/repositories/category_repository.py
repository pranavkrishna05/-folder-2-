from typing import Optional
from app.models.category import Category
from app import db

class CategoryRepository:
    """
    Repository class for interacting with the Category model.
    """
    
    def find_by_name(self, name: str) -> Optional<Category]:
        return Category.query.filter_by(name=name).first()
    
    def save(self, category: Category) -> None:
        db.session.add(category)
        db.session.commit()