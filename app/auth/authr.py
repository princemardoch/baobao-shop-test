from flask import Blueprint, redirect, url_for, session

auth = Blueprint('auth', __name__)

@auth.before_request
def islogin():
    if 'id' in session:
        pass

@auth.route('/')
def redirect_():
    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return 'Ok'