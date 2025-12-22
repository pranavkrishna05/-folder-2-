from flask import Flask, jsonify
from app.routes.user_routes import user_routes

def create_app():
    """
    Application factory to create and configure the Flask app instance.
    """
    app = Flask(__name__)

    # Load configurations
    app.config.from_object("app.config.config")

    # Register blueprints
    app.register_blueprint(user_routes, url_prefix="/api/v1/users")

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "An internal error occurred"}), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
