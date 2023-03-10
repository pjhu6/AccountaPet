import sqlite3

conn = sqlite3.connect('db/accountapet.db')
c = conn.cursor()

# list all tables in the database
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

# clear all rows from each table
for table_name in tables:
    c.execute(f"DELETE FROM {table_name[0]}")
    print(f"All rows deleted from {table_name[0]}")

conn.commit()
c.close()
conn.close()
