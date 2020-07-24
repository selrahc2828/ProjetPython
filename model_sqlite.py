#!/usr/bin/env python3

from model import create_uid

from sqlite3 import *

def get_last_code_db():
    conn = connect("db/tab_codes.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM codes")
    d = cur.fetchall()
    cur.close()
    conn.close()
    return d

def save_db():
    uid = create_uid()
    conn = connect("db/tab_codes.db")
    cur = conn.cursor()
    code = '# Write your code here...'
    langage = ''
    cur.execute('INSERT INTO codes(id, code,langage) VALUES(?,?,?)', (uid, code, langage))
    conn.commit()
    cur.close()
    conn.close()
    return uid

def get_code(uid):
    conn = connect("db/tab_codes.db")
    cur = conn.cursor()
    cur.execute("SELECT code FROM codes where id = '"+uid+"'")
    d = cur.fetchone()
    cur.close()
    conn.close()
    return d[0]

def get_langage(uid):
    conn = connect("db/tab_codes.db")
    cur = conn.cursor()
    cur.execute("SELECT langage FROM codes where id = '"+uid+"'")
    d = cur.fetchone()
    cur.close()
    conn.close()
    return d[0]

def update_code(uid=None,code=None,langage=None):
    if uid is None:
        uid = create_uid()
        code = '# Write your langage here...'
        langage = ''
    conn = connect("db/tab_codes.db")
    cur = conn.cursor()
    print(code)
    cur.execute("UPDATE codes SET code = '"+code+"', langage = '"+langage+"' where id = '"+uid+"'")
    conn.commit()
    cur.close()
    conn.close()
    return uid


print(get_last_code_db())