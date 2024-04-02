from flask import Blueprint
from models import mysql

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login')
def login():
    return "Login Page"

@auth.route('/logout')
def logout():
    return "Logout Page"

@auth.route('/register')
def register():
    return "Register Page"