from flask import Flask, request, redirect, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost"]}})

@app.route('/home', methods=['POST'])
def handle_home_request():
    action = request.form['action']
    if action == 'check_login':
        print(action)
        print(request.form['user_id'])

        data = request.form
        response, status_code = check_login(data)

        if status_code == 200:
            print(status_code)
            #successful login
            return redirect('http://127.0.0.1:5000/home')
        elif status_code == 404:
            print(status_code)
            #invalid user ID
            return render_template('login.html', message_login=response)
    elif action == 'create_user':
        print(action)
        print(request.form['user_name'])


        data = request.form
        response, status_code = create_user(data)

        if status_code == 201:
            print(status_code)
            #successful registration
            return redirect('http://127.0.0.1:5000/home')
        elif status_code == 400:
            print(status_code)
            #user ID already in use
            return render_template('login.html', message_register=response)
    else:
        return 'Invalid action'


def check_login(data):
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()

    user_id = data['user_id']
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()

    c.close()
    conn.close()

    if user:
        return 'User found', 200
    else:
        return 'Invalid User ID', 404

def create_user(data):
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()

    user_id = data['user_id']
    user_name = data['user_name']

    #check if user_id already exists in the database
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    if user:
        #user_id already exists, return validation error
        c.close()
        conn.close()
        return 'User ID already exists', 400

    #otherwise proceed with creating the user along with other user fields
    wallet = 0
    pet_health = 100
    pet_status_id = 0
    c.execute('INSERT INTO users (user_id, user_name, wallet, pet_health, pet_status_id) VALUES (?, ?, ?, ?, ?)', 
              (user_id, user_name, wallet, pet_health, pet_status_id))
    conn.commit()

    c.close()
    conn.close()

    return 'User created', 201






if __name__ == '__main__':
    app.run(port=5001)
