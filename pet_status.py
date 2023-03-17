from flask import Flask, request, redirect, render_template, session
from flask_cors import CORS
import sqlite3
from dto.user_status import PetStatus, UserStatus, Item
import search
import datetime

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

    # Get user's pet status info from db
    c.execute('''SELECT pets.pet_name, pets.img_name, pet_status.pet_status_name, pet_status.effect, users.pet_health, users.pet_id, users.wallet, users.last_updated
                FROM users
                JOIN pet_status ON users.pet_status_id = pet_status.pet_status_id
                JOIN pets ON users.pet_id = pets.pet_id
                WHERE users.user_id = ?;''', 
                (user_id,))
    status_info = c.fetchone()
    if not status_info:
        return {}
    print(f'{user_id}\'s pet status: {status_info}')

    # Change status if a day has passed since last update
    last_updated = datetime.datetime.strptime(status_info[7], '%Y-%m-%d')
    today = datetime.datetime.today()
    if today - last_updated >= datetime.timedelta(days=1):
        c.execute('SELECT pet_status_id FROM pet_status ORDER BY RANDOM() LIMIT 1')
        new_status_id = c.fetchone()[0]
        c('UPDATE users SET pet_status_id = ? WHERE user_id = ?', (new_status_id, user_id))
    # Set last updated to now
    c.execute("UPDATE users SET last_updated = ? WHERE user_id = ?", (today, user_id))

    # Get user's inventory
    c.execute('''SELECT item_id, item_name, item_amount
                FROM inventory
                WHERE user_id = ?;''',
                (user_id,))
    inventory = c.fetchall()

    c.close()
    conn.close()
    
    # build DTOs
    pet_status = PetStatus(pet_name=status_info[0], img_name=status_info[1], status_name=status_info[2], 
                    effect_value=status_info[3], pet_health=status_info[4])
    items = [Item(entry[0], entry[1], entry[2]) for entry in inventory] if inventory else []
    recommendations = get_recommendations(status_info[6], 10) 
    return UserStatus(pet_status=pet_status, items=items, recommendations=recommendations).to_dict()


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
    
    # Find item in inventory from item_id and decrement item amount
    c.execute('''SELECT item_amount
              FROM inventory WHERE user_id=? AND item_id=?''',
              (user_id, item_id))
    result = c.fetchone()
    if not result:
        return {}
    item_amount = result[0] 
    print(f'item amount: {item_amount}')
    if item_amount > 1:
        c.execute("UPDATE inventory SET item_amount=? WHERE user_id=? AND item_id=?", (item_amount - 1, user_id, item_id))
    else:
        c.execute("DELETE FROM inventory WHERE user_id=? AND item_id=?", (user_id, item_id))

    # Calculate item effect 
    c.execute("SELECT * FROM pet_shop WHERE item_id = ?", (item_id,))
    item_row = c.fetchone()
    weather_id, time = search.get_weather_id_time()
    adjusted_effect = search.calculate_adjusted_effect(item_row, weather_id=weather_id, timestamp=time)

    # Apply item effect
    pet_health = c.execute("SELECT pet_health FROM users WHERE user_id = ?", (user_id,)).fetchone()[0]
    new_health = min(pet_health + adjusted_effect, 100)
    c.execute("UPDATE users SET pet_health = ? WHERE user_id = ?", (new_health, user_id))

    conn.commit()
    return {}

def get_recommendations(wallet, num_items):
    # Return list of Items
    weather_id, time = search.get_weather_id_time()
    sorted_shop_list = search.perform_search(wallet, weather_id=weather_id, timestamp=time)
    return [Item(item[0], item[1], item[2]) for item in sorted_shop_list][:num_items]

if __name__ == '__main__':
    app.run(port=5004)