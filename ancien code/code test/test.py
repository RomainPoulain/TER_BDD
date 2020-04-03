import sqlite3,distance

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")
conn.commit()
cur.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("olivier", 30))
conn.commit()
req = "select * from users"
result = cur.execute(req)
print(type(result))
for row in result:
	print(row[1])
