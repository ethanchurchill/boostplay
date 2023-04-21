import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        conn.set_session(autocommit=True)

        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        return None

def disconnect(conn, cur):
    try:
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        return False
    finally:
        if conn is not None:
            conn.close()
    return True


if __name__ == '__main__':
    conn = connect()
    cur = conn.cursor()
    disconnect(conn, cur)