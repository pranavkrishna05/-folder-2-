from app.controllers.category_controller import category_blueprint

def register_category_routes(app):
    """
    Register category routes for the application.
    """
    app.register_blueprint(category_blueprint, url_prefix='/api/categories')