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

def save_db(ip_adress, naviguateur, date_modif):
    uid = create_uid()
    conn1 = connect("db/tab_codes.db")
    cur1 = conn1.cursor()
    code = '# Write your code here...'
    langage = ''
    cur1.execute('INSERT INTO codes(id, code,langage) VALUES(?,?,?)', (uid, code, langage))
    conn1.commit()
    cur1.close()
    conn1.close()
    conn2 = connect("db/tab_users.db")
    cur2 = conn2.cursor()
    cur2.execute('INSERT INTO users(uid_code,ip_adress,naviguateur, date_modif) VALUES(?,?,?,?)', (uid, ip_adress, naviguateur, date_modif))
    conn2.commit()
    cur2.close()
    conn2.close()
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

def get_all_users():
    conn = connect("db/tab_users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    d = cur.fetchall()
    cur.close()
    conn.close()
    return d

def get_ip_users():
    conn = connect("db/tab_users.db")
    cur = conn.cursor()
    cur.execute("SELECT ip_adress FROM users")
    d = cur.fetchall()
    cur.close()
    conn.close()
    return d[0]

def get_ip_from_uid(uid):
    conn = connect("db/tab_users.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE uid_code = ?',(uid,))
    d = cur.fetchall()
    cur.close()
    conn.close()
    print(d)
    return d

#print(get_last_code_db())

