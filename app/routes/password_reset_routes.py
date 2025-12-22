from app.controllers.password_reset_controller import password_reset_blueprint

def register_password_reset_routes(app):
    """
    Register password reset routes for the application.
    """
    app.register_blueprint(password_reset_blueprint, url_prefix='/api/password_reset')