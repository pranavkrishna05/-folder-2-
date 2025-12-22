from app.controllers.user_controller import user_blueprint

def register_routes(app):
    """
    Register all routes for the application.
    """
    app.register_blueprint(user_blueprint, url_prefix='/api')