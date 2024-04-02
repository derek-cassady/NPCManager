from flask import Blueprint

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/dashboard')
def show_dashboard():
    return "Dashboard Page"