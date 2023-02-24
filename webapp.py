from flask import Flask, redirect, render_template, url_for
import petbehavior
import foodrecc
import pet_setup
import os
from consumable import Consumable
from user import User

app = Flask(__name__)

# TODO: implement users
users = {}
### TEST USER REMOVE LATER ###
test_user_id = 'bobjoe123'
test_user = User(test_user_id)
users['bobjoe123'] = test_user
test_user.pet = pet_setup.VirtualPet("Fluffy II", "cat", 5)
### TEST USER REMOVE LATER ###

pet = None
pet_file = "pet.json"
if os.path.isfile(pet_file):
    pet = pet_setup.readFromJson(pet_file)
else:
    pet = pet_setup.VirtualPet("Fluffy", "cat", 3)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/pet_status')
def pet_status():
    # TODO make these dynamic urls with user_id, don't hardcode pet
    return render_template('pet_status.html', pet=users['bobjoe123'].pet)

@app.route('/settings')
def settings():
    return render_template('settings.html')


# User actions

@app.route('/<user_id>/feed')
def feed(user_id):
    # TODO replace with consumable of user's choice
    user_pet = users[user_id].pet
    print(f"User {user_id} is feeding their pet named {user_pet.name}")
    return user_pet.feed(Consumable("dog food", 1, 1))

@app.route('/<user_id>/recomend')
def recommend(user_id):
    pass

@app.route('/<user_id>/purchase')
def purchase(user_id):
    pass

if __name__ == '__main__':
    app.run()
