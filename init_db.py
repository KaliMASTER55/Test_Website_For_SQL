import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create a table for users
c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert a sample user
c.execute('''
INSERT INTO users (username, password) VALUES (?, ?)
''', ('testuser', 'testpass'))

# Commit and close the connection
conn.commit()
conn.close()
