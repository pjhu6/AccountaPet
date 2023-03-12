import sqlite3

conn = sqlite3.connect('db/accountapet.db')
c = conn.cursor()
c.execute("DELETE FROM goal")
rows_deleted = c.rowcount
print(f"{rows_deleted} rows deleted from goal table.")
conn.commit()
c.close()
conn.close()

