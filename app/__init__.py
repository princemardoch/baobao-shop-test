import secrets

from flask import Flask, session

from logging_setup import logging_

def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.before_request
    def make_session_permanent():
        session.permanent = True
        logging_.setup()

    app.config['SECRET_KEY'] = secrets.token_urlsafe(30)
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    from .user.userr import user
    from .admin.adminr import admin
    from .auth.authr import auth

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(user, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/admin')

    return app