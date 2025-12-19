
from flask import Flask
from config import Config

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Register Blueprints
from controllers.authentication import auth_bp
from controllers.categories import categories_bp
# Register other blueprints as required

app.register_blueprint(auth_bp)
app.register_blueprint(categories_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
