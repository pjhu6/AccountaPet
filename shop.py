from flask import Flask, request, redirect, render_template, session
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
app.secret_key = 'shop_secret_key'
CORS(app, resources={r"/*": {"origins": ["http://localhost"]}})

@app.route('/shop', methods=['POST'])
def handle_shop_request():
    action = request.form['action']
    if action == 'buy':
        print(action)
        
        data = request.form
        response, status_code = buy(data)

        if status_code == 200:
            print(status_code)
            #bought item successfully
            return redirect('http://127.0.0.1:5000/shop')
        elif status_code == 400:
            print(status_code)
            #failed item purchase
            return render_template('shop.html', user_name=session['user_name'], message=response)


def buy(data):
    conn = sqlite3.connect('db/accountapet.db')
    c = conn.cursor()

    item_id = data['item_id']

    #Retrieve user_id from current_user table
    c.execute("SELECT user_id FROM current_user")
    user_id = c.fetchone()[0]

    #Get cost of item in pet shop table based on item_id
    c.execute("SELECT cost, item_name, effect FROM pet_shop WHERE item_id=?", (item_id,))
    result = c.fetchone()
    if not result:
        return 'Item not found', 400
    item_cost, item_name, item_effect = result

    #Get user wallet balance from users table
    c.execute("SELECT wallet FROM users WHERE user_id=?", (user_id,))
    result = c.fetchone()
    wallet = result[0] if result else 0
    
    #Check if user can afford the item based on their current balance
    if wallet < item_cost:
        return 'Not enough funds to buy item', 400

    #Deduct item cost from user wallet
    new_wallet = wallet - item_cost
    c.execute("UPDATE users SET wallet=? WHERE user_id=?", (new_wallet, user_id))
    conn.commit()

    #Check if item already exists in user inventory
    c.execute("SELECT item_amount FROM inventory WHERE user_id=? AND item_id=?", (user_id, item_id))
    result = c.fetchone()
    if result:
        #If item exists, increment item amount by 1
        item_amount = result[0] + 1
        c.execute("UPDATE inventory SET item_amount=? WHERE user_id=? AND item_id=?", (item_amount, user_id, item_id))
    else:
        #If item does not exist, create new record with item amount starting at 1
        c.execute("INSERT INTO inventory (user_id, item_id, item_name, item_amount, effect) VALUES (?, ?, ?, ?, ?)", (user_id, item_id, item_name, 1, item_effect))

    conn.commit()
    conn.close()

    return 'Item purchased successfully', 200

if __name__ == '__main__':
    app.run(port=5002)