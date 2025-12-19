from flask import Flask, session
from user_account.interfaces.routes.auth import bp as auth_bp

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_COOKIE_NAME'] = 'my_session'
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)