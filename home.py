from flask import Flask, request, redirect, render_template, session
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
app.secret_key = 'home_secret_key'
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

    elif action == 'add_goal':
        print(action)
        print(request.form['goal_description'])
        print(request.form['time_remaining'])

        data = request.form
        response, status_code = add_goal(data)

        if status_code == 200:
            print(status_code)
            #successful goal add
            return redirect('http://127.0.0.1:5000/home')
        elif status_code == 400:
            print(status_code)
            #failed goal add
            return render_template('home.html', user_name=session['user_name'], message=response)
    elif action == 'remove_goal':
        print(action)
        print(request.form['goal_id'])

        data = request.form
        response, status_code = remove_goal(data)

        if status_code == 200:
            print(status_code)
            #removed goal successfully
            return redirect('http://127.0.0.1:5000/home')
        elif status_code == 400:
            print(status_code)
            #failed goal removal
            return render_template('home.html', user_name=session['user_name'], message=response)


    else:
        return 'Invalid action'

def remove_goal(data):
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()

    #Get the user_id of the current user
    c.execute("SELECT user_id FROM current_user")
    user_id = c.fetchone()[0]

    #Get the goal_id from the POST request
    goal_id = data['goal_id']

    #Delete the goal from the goal table with the given goal_id and user_id
    c.execute("DELETE FROM goal WHERE goal_id=? AND user_id=?", (goal_id, user_id))

    # Increase user's wallet by 5
    c.execute("UPDATE users SET wallet = wallet + 5 WHERE user_id = ?", (user_id,))
    conn.commit()

    c.close()
    conn.close()

    return 'Goal successfully removed', 200



def check_login(data):
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()

    user_id = data['user_id']
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()

    c.close()
    conn.close()

    if user:
        #save user_id and associated user_name from user table into current user table
        conn = sqlite3.connect('db/accountapet.db')
        c = conn.cursor()
        c.execute("INSERT INTO current_user (user_id, user_name) VALUES (?, ?)", (user_id, user[1]))
        conn.commit()
        c.close()
        conn.close()
    
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

    #save user_id and user_name into current user table
    c.execute("INSERT INTO current_user (user_id, user_name) VALUES (?, ?)", (user_id, user_name))
    conn.commit()

    c.close()
    conn.close()

    return 'User created', 201

def add_goal(data):
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()

    #Retrieve user_id from current_user table
    c.execute("SELECT user_id FROM current_user")
    user_id = c.fetchone()[0]

    #Get the maximum goal_id value from the goal table and add 1 to get the next goal_id
    c.execute("SELECT MAX(goal_id) FROM goal")
    goal_id = c.fetchone()[0]
    if goal_id is None:
        goal_id = 0
    else:
        goal_id += 1

    #Insert new goal record into goal table
    goal_description = data['goal_description']
    try:
        time_remaining = int(data['time_remaining'])
    except ValueError:
        return 'Invalid time remaining', 400


    c.execute("INSERT INTO goal (goal_id, user_id, goal_description, time_remaining) VALUES (?, ?, ?, ?)",
              (goal_id, user_id, goal_description, time_remaining))
    conn.commit()

    c.close()
    conn.close()

    return 'Goal successfully added', 200




if __name__ == '__main__':
    app.run(port=5001)
