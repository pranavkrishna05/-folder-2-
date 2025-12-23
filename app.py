"""
Application entry point for the Flask application.
"""

from flask import Flask
from app.config.app_config import DevelopmentConfig
from app.routes.api_routes import api_blueprint
from app.models.user import db


def create_app() -> Flask:
    """Create and initialize the Flask application."""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register API routes
    app.register_blueprint(api_blueprint)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)
```