from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import the init_app function from the database module
from database import init_app as init_database_app
# Import your Blueprints here
from blueprints.auth import auth_blueprint
from blueprints.dashboard import dashboard_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize the database
init_database_app(app)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://derek:12345678@localhost/npcmanager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(dashboard_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)