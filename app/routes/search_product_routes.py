from app.controllers.search_product_controller import search_product_blueprint

def register_search_product_routes(app):
    """
    Register product search routes for the application.
    """
    app.register_blueprint(search_product_blueprint, url_prefix='/api/products')