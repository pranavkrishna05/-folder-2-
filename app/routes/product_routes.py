from app.controllers.product_controller import product_blueprint

def register_product_routes(app):
    """
    Register product routes for the application.
    """
    app.register_blueprint(product_blueprint, url_prefix='/api/products')