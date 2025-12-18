from flask import Flask
from controllers.auth.auth_controller import auth_bp


def register_controllers(app: Flask):
    app.register_blueprint(auth_bp)
    # Register other blueprints similarly