from app.controllers.profile_controller import profile_blueprint

def register_profile_routes(app):
    """
    Register profile routes for the application.
    """
    app.register_blueprint(profile_blueprint, url_prefix='/api/profile')