from flask import Flask
from app.config.config import config_by_name
from app.routes.user_routes import register_routes
from app.routes.auth_routes import register_auth_routes
from app.routes.password_reset_routes import register_password_reset_routes
from app.routes.profile_routes import register_profile_routes
from app import db

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    register_routes(app)
    register_auth_routes(app)
    register_password_reset_routes(app)
    register_profile_routes(app)
    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run()
```