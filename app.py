from flask import Flask, g, session
from flask_sqlalchemy import SQLAlchemy
from app.product_management.interfaces.routes.category_routes import category_bp
import logging
from datetime import timedelta

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object('app.config.Config')
app.secret_key = app.config['SECRET_KEY']
app.permanent_session_lifetime = timedelta(hours=24)

# Set up structured logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the database
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(category_bp)

@app.before_request
def load_user():
    # Placeholder for actual user loading logic
    g.user = None  # Make sure to set this to the actual user object based on session or token

if __name__ == '__main__':
    app.run(debug=True)
