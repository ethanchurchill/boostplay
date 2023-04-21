#! C:\Python311\python.exe

from connect import connect, disconnect
import argon2

def validate_registration(name, password, email):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT userid FROM users WHERE name = %s;",(name,))
    result = cur.fetchone()
    if result != None:
        return 1 # User already exists in table
    ph = argon2.PasswordHasher()
    hash = ph.hash(password)
    cur.execute("INSERT INTO users (name, email, hash) VALUES (%s, %s, %s);",(name, email, hash,))
    disconnect(conn, cur)
    return 0
    