#! C:\Python311\python.exe
from connect import connect, disconnect
import argon2

def retrieve_profile(username): 
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT email FROM users WHERE name = %s;", (username,))
    fetched_email = cur.fetchone()
    if (fetched_email == None):
        return None
        
    return fetched_email[0]
    
    


