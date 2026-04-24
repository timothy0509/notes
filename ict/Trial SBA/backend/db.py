import pymysql
from contextlib import contextmanager

DB_CONFIG = {
    'host': 'localhost',
    'port': 3307,
    'user': 'root',
    'password': 'usbw',
    'database': 'todo_db',
    'cursorclass': pymysql.cursors.DictCursor
}

@contextmanager
def get_db():
    conn = pymysql.connect(**DB_CONFIG)
    try:
        yield conn
    finally:
        conn.close()

def query_one(sql, args=()):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, args)
            return cur.fetchone()

def query_all(sql, args=()):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, args)
            return cur.fetchall()

def execute(sql, args=()):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, args)
            conn.commit()
            return cur.lastrowid
