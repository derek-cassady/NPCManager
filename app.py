from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import your models
from models import db
# Import your Blueprints
from blueprints.auth import auth_blueprint
from blueprints.dashboard import dashboard_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://derek:12345678@localhost/npcmanager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the current application
db.init_app(app)

# Initialize Flask-Migrate with the application and the SQLAlchemy db instance
migrate = Migrate(app, db)

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(dashboard_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
