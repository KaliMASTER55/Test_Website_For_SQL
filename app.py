from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                            (username, password)).fetchone()
        conn.close()
        
        if user:
            flash('Login successful!')
            return redirect(url_for('welcome'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return 'Welcome to the website!'

if __name__ == '__main__':
    app.run(debug=True)
