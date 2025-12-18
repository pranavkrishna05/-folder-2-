from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.user_account.interfaces.routes.user_routes import user_bp
import logging
from datetime import timedelta

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object('config.Config')
app.secret_key = app.config['SECRET_KEY']
app.permanent_session_lifetime = timedelta(minutes=30)

# Set up structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the database
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
