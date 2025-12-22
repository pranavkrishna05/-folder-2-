"""
Application Routes: Registers all route blueprints with the application instance.
"""

from flask import Flask
from app.controllers.user_controller import user_bp

def register_routes(app: Flask):
    """Attach route blueprints to the Flask application instance."""
    app.register_blueprint(user_bp, url_prefix='/api/users')