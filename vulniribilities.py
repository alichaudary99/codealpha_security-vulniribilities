from flask import Flask, request, render_template_string
import sqlite3
import sys
print(sys.path)


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Vulnerable query
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials"

    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <button type="submit">Login</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

