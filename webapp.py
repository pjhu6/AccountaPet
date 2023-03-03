from flask import Flask, abort, render_template
from virtual_pet import VirtualPet
import os
from consumable import Consumable
from user import User
import db

app = Flask(__name__)

# TODO: implement users
users = {}

### TEST USER REMOVE LATER ###
test_user_id = 'bobjoe123'
db.execute("DROP TABLE IF EXISTS users") # remove these later
db.execute("DROP TABLE IF EXISTS consumables")
db.execute("DROP TABLE IF EXISTS pets")
db.build()


user_file = f'{test_user_id}.json'
if os.path.isfile(user_file):
    users[test_user_id] = User.from_json(user_file)
else:
    users[test_user_id] = User(test_user_id, VirtualPet("Fluffy II", "cat", 5))

db.execute("INSERT INTO users (user_id) VALUES (?)", test_user_id)
db.commit()
test_pet_data = db.record("SELECT pet_name, species FROM pets WHERE user_id = ?", test_user_id)
print(f"[{test_user_id}] has a [{test_pet_data[1]}] named [{test_pet_data[0]}]")

### TEST USER REMOVE LATER ###

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html', user=users['bobjoe123'])

@app.route('/shop')
def shop():
    return render_template('shop.html', user=users['bobjoe123'])

@app.route('/pet_status')
def pet_status():
    # TODO make these dynamic urls with user_id, don't hardcode pet
    return render_template('pet_status.html', user=users['bobjoe123'])

@app.route('/settings')
def settings():
    return render_template('settings.html', user=users['bobjoe123'])


# User actions

@app.route('/<user_id>/feed')
def feed(user_id):
    # TODO replace with consumable of user's choice
    if user_id not in users:
        print(f'User {user_id} does not exist.')
        abort(404)
    print(f"User {user_id} is feeding their pet named {users[user_id].pet.name}")
    return users[user_id].feed(Consumable("dog food", 1, 1))

@app.route('/<user_id>/recomend')
def recommend(user_id):
    if user_id not in users:
        print(f'User {user_id} does not exist.')
        abort(404)
    return users[user_id].recommend()

@app.route('/<user_id>/purchase/<cost>')
def purchase(user_id,cost):
     if user_id not in users:
        print(f'User {user_id} does not exist.')
        abort(404)
     print("Purchase!")
     print(cost)
     return users[user_id].purchase(Consumable("dog food",0,0,10))

if __name__ == '__main__':
    app.run()
