import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect("test.db",isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users \
    (uid text PRIMARY KEY, upw text)")

# c.execute("INSERT INTO users(id,pw) \
#     VALUES('banana', 'banana')")
c.execute("SELECT * FROM users")
print(c.fetchall())
# c.execute("DROP table users")