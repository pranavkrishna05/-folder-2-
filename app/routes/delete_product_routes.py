from app.controllers.delete_product_controller import delete_product_blueprint

def register_delete_product_routes(app):
    """
    Register product deletion routes for the application.
    """
    app.register_blueprint(delete_product_blueprint, url_prefix='/api/products')