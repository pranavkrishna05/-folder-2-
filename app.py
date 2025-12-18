from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.user_account.interfaces.routes.user_routes import user_bp
import logging

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object('config.Config')

# Set up structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the database
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
