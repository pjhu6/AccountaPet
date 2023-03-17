import sqlite3

# create connection to database
conn = sqlite3.connect('./db/accountapet.db')

#conn.execute('''DROP TABLE IF EXISTS users''')
# create user table
conn.execute('''CREATE TABLE IF NOT EXISTS users
                (user_id TEXT PRIMARY KEY,
                user_name TEXT NOT NULL,
                wallet INTEGER DEFAULT 0,
                pet_health INTEGER DEFAULT 100,
                pet_status_id INTEGER DEFAULT 1,
                pet_id TEXT DEFAULT 'cat1',
                last_updated DATE DEFAULT (date('now')),
                FOREIGN KEY (pet_status_id) REFERENCES pet_status(pet_status_id),
                FOREIGN KEY (pet_id) REFERENCES pets(pet_id));''')

# create goal table
conn.execute('''CREATE TABLE IF NOT EXISTS goal
                (goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                goal_description TEXT,
                time_remaining INTEGER,
                FOREIGN KEY (user_id) REFERENCES user(user_id));''')

# create pet shop table
conn.execute('''CREATE TABLE IF NOT EXISTS pet_shop
                (item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                cost INTEGER,
                effect INTEGER,
                weather_2xx REAL,
                weather_3xx REAL,
                weather_5xx REAL,
                weather_6xx REAL,
                weather_7xx REAL,
                weather_8xx REAL,
                ideal_time INTEGER);''')

# create inventory table
conn.execute('''CREATE TABLE IF NOT EXISTS inventory
                (user_id TEXT,
                item_id INTEGER,
                item_name TEXT,
                item_amount INTEGER,
                effect INTEGER,
                FOREIGN KEY (user_id) REFERENCES user(user_id),
                FOREIGN KEY (item_id) REFERENCES pet_shop(item_id));''')

# create pet status table
conn.execute('''CREATE TABLE IF NOT EXISTS pet_status
                (pet_status_id INTEGER PRIMARY KEY AUTOINCREMENT,
                pet_status_name TEXT,
                effect INTEGER);''')

# create current user table
conn.execute('''CREATE TABLE IF NOT EXISTS current_user
                (user_id TEXT PRIMARY KEY,
                user_name TEXT NOT NULL);''')

# create pets table
conn.execute('''CREATE TABLE IF NOT EXISTS pets
                (pet_id TEXT PRIMARY KEY,
                pet_name TEXT NOT NULL,
                img_name TEXT NOT NULL);''')

# close connection to database
conn.close()
