"""
Entry point for the Flask application.
"""

from flask import Flask
from app.controllers.users.user_controller import user_bp

def create_app() -> Flask:
    """
    Create and configure a Flask instance.

    Returns:
        Flask: A configured Flask application.
    """
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(user_bp, url_prefix='/api/users')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
```