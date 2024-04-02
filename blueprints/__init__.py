from flask import Blueprint
from models import mysql

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')