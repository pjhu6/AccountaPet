import sqlite3

# create connection to database
conn = sqlite3.connect('./db/accountapet.db')

# create user table
conn.execute('''CREATE TABLE user
                 (user_id INTEGER PRIMARY KEY,
                  user_name TEXT NOT NULL,
                  wallet INTEGER,
                  pet_health INTEGER,
                  pet_status_id INTEGER,
                  FOREIGN KEY (pet_status_id) REFERENCES pet_status(pet_status_id));''')

# create goal table
conn.execute('''CREATE TABLE goal
                 (goal_id INTEGER PRIMARY KEY,
                  user_id INTEGER,
                  goal_description TEXT,
                  time_remaining INTEGER,
                  FOREIGN KEY (user_id) REFERENCES user(user_id));''')

# create pet shop table
conn.execute('''CREATE TABLE pet_shop
                 (item_id INTEGER PRIMARY KEY,
                  item_name TEXT,
                  cost INTEGER,
                  effect INTEGER);''')

# create inventory table
conn.execute('''CREATE TABLE inventory
                 (user_id INTEGER,
                  item_id INTEGER,
                  item_name TEXT,
                  effect INTEGER,
                  FOREIGN KEY (user_id) REFERENCES user(user_id),
                  FOREIGN KEY (item_id) REFERENCES pet_shop(item_id));''')

# create pet status table
conn.execute('''CREATE TABLE pet_status
                 (pet_status_id INTEGER PRIMARY KEY,
                  pet_status_name TEXT,
                  effect INTEGER);''')

# close connection to database
conn.close()
