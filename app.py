from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)

# Secret key for session management. Replace with a random, secure value.
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'derek'  # MySQL username
app.config['MYSQL_PASSWORD'] = '12345678'  # MySQL password
app.config['MYSQL_DB'] = 'npcmanager'  # Name of the database

# Initialize MySQL connection
mysql = MySQL(app)

@app.route('/')
def home():
    # Redirects to the login page
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Handles registration logic
    if request.method == 'POST':
        # Collect form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash the password for secure storage
        hashed_password = generate_password_hash(password)

        # Insert new user into the database
        # Prepare the cursor
        cursor = mysql.connection.cursor()
        try:
            # Insert the user with is_active set to 0 (False)
            cursor.execute('''INSERT INTO users (username, email, password, is_active) VALUES (%s, %s, %s, %s)''', 
                           (username, email, hashed_password, 0))
            mysql.connection.commit()
            flash('You were successfully registered! Your account is pending approval.')
            return redirect(url_for('login'))
        except Exception as e:
            mysql.connection.rollback()
            flash('Registration failed. There might be a problem with your registration details.')
            return redirect(url_for('register'))
        finally:
            cursor.close()
    return render_template('register.html')

    # Render the registration form template
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handles login logic
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check user credentials
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT password FROM users WHERE username = %s ''', (username,))
        user_pass = cursor.fetchone()
        cursor.close()
        
        if user_pass and check_password_hash(user_pass[0], password):
            # Set user session if login is successful
            session['username'] = username
            return "Login successful!"
        else:
            # Login failure
            return "Invalid credentials!"
    # Render the login form template
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Logout logic to remove the user from session
    session.pop('username', None)
    # Return the logout.html template
    return render_template('logout.html')

@app.route('/dashboard')
def dashboard():
    # Dashboard page that requires user to be logged in
    if 'username' not in session:
        # Redirect to login if not logged in
        return redirect(url_for('login'))
    # Render the dashboard template with the username passed to it
    return render_template('dashboard.html', username=session['username'])

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)