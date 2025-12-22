from typing import Optional
from app.models.product import Product
from app import db

class ProductRepository:
    """
    Repository class for interacting with the Product model.
    """
    
    def find_by_name(self, name: str) -> Optional[Product]:
        return Product.query.filter_by(name=name).first()
    
    def save(self, product: Product) -> None:
        db.session.add(product)
        db.session.commit()