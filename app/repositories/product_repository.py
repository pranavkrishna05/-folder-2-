from typing import List
from app.models.product import Product
from app import db

class ProductRepository:
    """
    Repository class for interacting with the Product model.
    """
    
    def find_by_name(self, name: str) -> Optional[Product]:
        return Product.query.filter_by(name=name).first()
    
    def find_by_id(self, id: int) -> Optional[Product]:
        return Product.query.get(id)
    
    def save(self, product: Product) -> None:
        db.session.add(product)
        db.session.commit()
    
    def delete(self, product: Product) -> None:
        db.session.delete(product)
        db.session.commit()
    
    def search_by_query(self, query: str, page: int, per_page: int) -> List[Product]:
        return Product.query.filter(Product.name.ilike(f'%{query}%')).paginate(page, per_page, False).items
    
    def count_by_query(self, query: str) -> int:
        return Product.query.filter(Product.name.ilike(f'%{query}%')).count()