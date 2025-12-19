# __init__.py
from flask import Blueprint
from backend.controllers.auth.registration import RegisterAPI
from backend.controllers.auth.login import LoginAPI
from backend.controllers.auth.password_reset import PasswordResetRequestAPI, PasswordResetAPI

auth_blueprint = Blueprint('auth', __name__)

# Register routes
auth_blueprint.add_url_rule('/register', view_func=RegisterAPI.as_view('register'))
auth_blueprint.add_url_rule('/login', view_func=LoginAPI.as_view('login'))
auth_blueprint.add_url_rule('/password-reset-request', view_func=PasswordResetRequestAPI.as_view('password_reset_request'))
auth_blueprint.add_url_rule('/password-reset/<token>', view_func=PasswordResetAPI.as_view('password_reset'))
