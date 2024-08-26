import secrets

from flask import Flask, session

def create_app():
    app = Flask(__name__)

    @app.before_request
    def make_session_permanent():
        session.permanent = True

    app.config['SECRET_KEY'] = secrets.token_urlsafe(30)


    from .user.userr import user
    from .admin.adminr import admin
    from .auth.authr import auth

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(user, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/admin')

    return app