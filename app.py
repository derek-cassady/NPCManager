from flask import Flask
from flask_mysqldb import MySQL
# Import your Blueprints here
from blueprints.auth import auth_blueprint
from blueprints.dashboard import dashboard_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize the database
init_database_app(app)

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(dashboard_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)