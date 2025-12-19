# app.py
import os
from flask import Flask
from backend.config import configure_app
from backend.controllers.auth import auth_blueprint
from backend.controllers.profile import profile_blueprint
from backend.models import db
from backend.repositories import init_repositories
from backend.services import init_services

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    configure_app(app, config_name)
    db.init_app(app)
    init_repositories(app)
    init_services(app)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(profile_blueprint, url_prefix='/profile')
    return app


if __name__ == '__main__':
    config_name = os.getenv('FLASK_ENV', 'development')
    app = create_app(config_name)
    app.run(host='0.0.0.0', port=5000)
