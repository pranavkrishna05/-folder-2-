import os
from flask import Flask
from config import setup_config
from controllers import register_controllers


def create_app() -> Flask:
    app = Flask(__name__)
    setup_config(app)
    register_controllers(app)

    @app.route('/health')
    def health_check():
        return 'OK', 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))