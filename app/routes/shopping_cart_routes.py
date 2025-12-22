from app.controllers.shopping_cart_controller import shopping_cart_blueprint

def register_shopping_cart_routes(app):
    """
    Register shopping cart routes for the application.
    """
    app.register_blueprint(shopping_cart_blueprint, url_prefix='/api/cart')