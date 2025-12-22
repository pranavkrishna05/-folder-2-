"""
Application Entry Point: Initializes and runs the Flask application.
"""

from flask import Flask
from app.config.config import config
from app.models.user import db
from app.routes.routes import register_routes

def create_app() -> Flask:
    """Application factory: Creates and configures a Flask app instance."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SECRET_KEY'] = config.SECRET_KEY

    # Initialize Plugins
    db.init_app(app)
    register_routes(app)

    return app

if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(debug=config.DEBUG)