"""
Application entry point for the Flask application.
"""

from flask import Flask
from app.config.app_config import DevelopmentConfig
from app.routes.password_routes import password_routes
from app.models.password_reset import db
from app.models.user import User


def create_app() -> Flask:
    """Create and initialize the Flask application."""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register password-related routes
    app.register_blueprint(password_routes)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)
```