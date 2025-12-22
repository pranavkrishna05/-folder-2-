from app.controllers.update_product_controller import update_product_blueprint

def register_update_product_routes(app):
    """
    Register product update routes for the application.
    """
    app.register_blueprint(update_product_blueprint, url_prefix='/api/products')