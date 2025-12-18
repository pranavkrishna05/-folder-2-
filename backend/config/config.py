import os
from flask import Flask


def setup_config(app: Flask):
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    app.config['DEBUG'] = os.getenv('DEBUG', True)