from typing import Optional
from app.models.category import Category
from app.repositories.category_repository import CategoryRepository

class CategoryService:
    """
    Service class for managing category operations.
    """
    
    def __init__(self, category_repository: CategoryRepository) -> None:
        self.category_repository = category_repository
    
    def create_category(self, name: str, parent_category_id: Optional[int] = None) -> Category:
        if self.category_repository.find_by_name(name):
            raise ValueError("Category name must be unique")
        
        parent_category = None
        if parent_category_id:
            parent_category = self.category_repository.find_by_id(parent_category_id)
            if not parent_category:
                raise ValueError("Parent category not found")
        
        new_category = Category(name=name, parent_category_id=parent_category_id)
        self.category_repository.save(new_category)
        return new_category

    def update_category(self, category_id: int, name: Optional[str] = None, parent_category_id: Optional[int] = None) -> Category:
        category = self.category_repository.find_by_id(category_id)
        if not category:
            raise ValueError("Category not found")
        
        if name and self.category_repository.find_by_name(name):
            raise ValueError("Category name must be unique")
        
        parent_category = None
        if parent_category_id:
            parent_category = self.category_repository.find_by_id(parent_category_id)
            if not parent_category:
                raise ValueError("Parent category not found")
        
        if name:
            category.name = name
        if parent_category_id is not None:
            category.parent_category_id = parent_category_id
        
        self.category_repository.save(category)
        return category

    def delete_category(self, category_id: int) -> None:
        category = self.category_repository.find_by_id(category_id)
        if not category:
            raise ValueError("Category not found")
        self.category_repository.delete(category)