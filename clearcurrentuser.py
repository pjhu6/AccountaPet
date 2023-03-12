import sqlite3

conn = sqlite3.connect('db/accountapet.db')
c = conn.cursor()
c.execute("DELETE FROM current_user")
rows_deleted = c.rowcount
print(f"{rows_deleted} rows deleted from current_user table.")
conn.commit()
c.close()
conn.close()

