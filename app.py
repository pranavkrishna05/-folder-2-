"""
Application entry point for the Flask application.
"""

from flask import Flask
from app.config.app_config import DevelopmentConfig
from app.routes.auth_routes import auth_blueprint
from app.models.session import db
from app.models.user import User


def create_app() -> Flask:
    """Create and initialize the Flask application."""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register authentication routes
    app.register_blueprint(auth_blueprint)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)
```