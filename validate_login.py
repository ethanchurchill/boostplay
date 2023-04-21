#! C:\Python311\python.exe
from connect import connect, disconnect
import argon2

# Function: 
#   login(username, password)
# Parameters: 
#   username: Name submitted by user attempting to login
#   password: Password subbmitted user attempting to login
# Description:
#   Takes in a username and password submitted by user, connects to
#   users table in database and validates that the password submitted
#   matches the password for that username.
# Returns:
#   0: Successful authentication
#   1: Submitted password does not match held password for username
#   2: Other verification error
#   3: User does not exist in table

def validate_login(username, password):
    ph = argon2.PasswordHasher()
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT hash FROM users WHERE name = %s;", (username,))
    hash_val = cur.fetchone()
    if hash_val == None:
        return 3
    hash_val = hash_val[0]

    # Verify password, raises exception if wrong.
    try:
        ph.verify(hash_val, password)
    except(Exception, argon2.exceptions.VerifyMismatchError):
        return 1
    except(Exception, argon2.exceptions.VerificationError):
        return 2
    
    # Now that we have the cleartext password,
    # check the hash's parameters and if outdated,
    # rehash the user's password in the database.
    if ph.check_needs_rehash(hash_val):
        cur.execute("UPDATE users SET hash = %s WHERE name = %s;",(ph.hash(password),username,))
    cur.execute("SELECT userid FROM users WHERE name = %s;", (username,))
    userid = cur.fetchone()
    userid = userid[0]
    disconnect(conn,cur)
    return userid
