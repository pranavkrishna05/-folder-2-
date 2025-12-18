from flask import Flask, g, session
from flask_sqlalchemy import SQLAlchemy
from app.product_management.interfaces.routes.product_routes import product_bp
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
app.register_blueprint(product_bp)

@app.before_request
def load_user():
    user_id = session.get('user_id')
    if user_id:
        g.user = User.query.get(user_id)
    else:
        g.user = None

if __name__ == '__main__':
    app.run(debug=True)
