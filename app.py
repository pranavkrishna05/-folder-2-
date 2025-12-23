"""
Application entry point for the Flask application.
"""

from flask import Flask
from app.config.app_config import DevelopmentConfig
from app.routes.product_routes import product_routes
from app.models.product import db


def create_app() -> Flask:
    """Create and initialize the Flask application."""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register product-related routes
    app.register_blueprint(product_routes)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)
```