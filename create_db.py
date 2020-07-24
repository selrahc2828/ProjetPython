from sqlite3 import *

# create bdd codes 

conn = connect("db/tab_codes.db")
cur = conn.cursor()
cur.execute("CREATE TABLE codes (id VARCHAR(20) PRIMARY KEY NOT NULL, code TEXT NOT NULL, langage TEXT)")
conn.commit()
cur.close()
conn.close()


# create bdd users

conn = connect("db/tab_users.db")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, ip_adress VARCHAR NOT NULL, naviguateur text, date TIMESTAMP)")
conn.commit()
cur.close()
conn.close()
