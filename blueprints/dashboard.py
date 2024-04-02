from flask import Blueprint
from models import mysql

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/dashboard')
def show_dashboard():
    return "Dashboard Page"