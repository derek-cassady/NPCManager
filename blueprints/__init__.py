from flask import Blueprint
from database import mysql

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')