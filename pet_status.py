from flask import Flask, request, redirect, render_template, session
from flask_cors import CORS
import sqlite3
from dto.user_status import PetStatus, UserStatus, Item

app = Flask(__name__)
app.secret_key = 'home_secret_key'
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5000"]}})

@app.route('/status', methods=['GET'])
def get_current_status():
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()
    c.execute("SELECT user_id FROM current_user")
    results = c.fetchone()
    if not results:
        return {}
    user_id = results[0]

    # TODO: Update user's pet status in db according to context filtering, i.e. location, weather, time

    # Get user's pet status info from db
    c.execute('''SELECT pets.pet_name, pets.img_name, pet_status.pet_status_name, pet_status.effect, users.pet_health, users.pet_id
                FROM users
                JOIN pet_status ON users.pet_status_id = pet_status.pet_status_id
                JOIN pets ON users.pet_id = pets.pet_id
                WHERE users.user_id = ?;''', 
                (user_id,))
    status_info = c.fetchone()
    print(f'{user_id}\'s pet status: {status_info}')

    # Get user's inventory
    c.execute('''SELECT item_id, item_name
                FROM inventory
                WHERE user_id = ?;''',
                (user_id,))
    inventory = c.fetchall()
    c.close()
    conn.close()

    if not status_info:
        return {}
    
    # build DTOs
    pet_status = PetStatus(pet_name=status_info[0], img_name=status_info[1], status_name=status_info[2], 
                    effect_value=status_info[3], pet_health=status_info[4])
    items = [Item(entry[0], entry[1]) for entry in inventory] if inventory else []
    # TODO: do items for real
    items = [Item(0, "medicine"), Item(1, "food")]
    return UserStatus(pet_status=pet_status, items=items).to_dict()


@app.route('/status', methods=['POST'])
def use_item():
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()
    c.execute("SELECT user_id FROM current_user")
    results = c.fetchone()
    if not results:
        return {}
    user_id = results[0]

    item_id = request.form['item_id']
    print(f"{user_id} used item with id: {item_id}")
    return {}

if __name__ == '__main__':
    app.run(port=5004)