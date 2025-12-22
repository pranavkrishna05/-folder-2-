from app.controllers.auth_controller import auth_blueprint

def register_auth_routes(app):
    """
    Register authentication routes for the application.
    """
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')