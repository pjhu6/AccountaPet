import sqlite3

conn = sqlite3.connect('db/accountapet.db')

c = conn.cursor()

# insert some data into the pet_shop table
data = [
    ('Item 1', 5, 5),
    ('Item 2', 5, 5),
    ('Item 3', 10, 5),
    ('Item 4', 15, 10),
    ('Item 5', 20, 20),
]

c.executemany('INSERT INTO pet_shop (item_name, cost, effect) VALUES (?, ?, ?)', data)

conn.commit()

c.close()
conn.close()
