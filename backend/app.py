import os
import logging
from flask import Flask


log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger(__name__)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))

    from controllers.auth import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.analytics import analytics_bp
    app.register_blueprint(analytics_bp)

    # Register other blueprints here

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

