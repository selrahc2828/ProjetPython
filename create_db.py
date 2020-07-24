from sqlite3 import *

# create bdd codes 

conn = connect("db/tab_codes.db")
cur = conn.cursor()
cur.execute("CREATE TABLE codes (id VARCHAR(20) PRIMARY KEY NOT NULL, code TEXT NOT NULL, langage TEXT)")
conn.commit()
cur.close()
conn.close()
