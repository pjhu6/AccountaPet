import sqlite3

conn = sqlite3.connect('db/accountapet.db')

c = conn.cursor()

pet_statuses = [
    ('Happy', 0),
    ('Hungry', -5),
    ('Sick', -10)
]

pets = [
    ('cat1', 'Fluffy', 'cat1.png'),
    ('dog1', 'Bob', 'dog1.png')
]

c.executemany('INSERT INTO pet_status (pet_status_name, effect) VALUES (?, ?)', pet_statuses)
c.executemany('INSERT INTO pets (pet_id, pet_name, img_name) VALUES (?, ?, ?)', pets)

print("Filled out tables.")

conn.commit()

c.close()
conn.close()