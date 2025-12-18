from app.database import db
from app.product_management.domain.entities.product import Product

class ProductRepository:
    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        return Product.query.get(product_id)

    @staticmethod
    def delete_product(product: Product) -> None:
        db.session.delete(product)
        db.session.commit()
