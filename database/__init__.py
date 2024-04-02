from flask_mysqldb import MySQL

mysql = MySQL()

def init_app(app):
    # Initialize the database with the Flask app
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'derek'
    app.config['MYSQL_PASSWORD'] = '12345678'
    app.config['MYSQL_DB'] = 'npcmanager'
    mysql.init_app(app)