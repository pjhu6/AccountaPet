import sqlite3

conn = sqlite3.connect('db/accountapet.db')

c = conn.cursor()

pet_statuses = [
    (0, 'Happy', 0),
    (1, 'Hungry', -5)
]

pets = [
    ('cat1', 'Fluffy', 'cat1.png'),
    ('dog1', 'Bob', 'dog1.png')
]

c.executemany('INSERT INTO pet_status (pet_status_id, pet_status_name, effect) VALUES (?, ?, ?)', pet_statuses)
c.executemany('INSERT INTO pets (pet_id, pet_name, img_name) VALUES (?, ?, ?)', pets)

print("Filled out tables.")

conn.commit()

c.close()
conn.close()