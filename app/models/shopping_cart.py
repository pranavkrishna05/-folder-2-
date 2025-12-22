from app import db

class ShoppingCart(db.Model):
    """
    ShoppingCart model for storing shopping cart details.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    items = db.relationship('ShoppingCartItem', backref='shopping_cart', lazy=True)

    def __repr__(self):
        return f"ShoppingCart('{self.user_id}', '{self.created_at}')"

class ShoppingCartItem(db.Model):
    """
    ShoppingCartItem model for storing items in the shopping cart.
    """
    id = db.Column(db.Integer, primary_key=True)
    shopping_cart_id = db.Column(db.Integer, db.ForeignKey('shopping_cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"ShoppingCartItem('{self.product_id}', '{self.quantity}')"