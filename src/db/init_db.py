import sqlite3

def init_db():
    conn = sqlite3.connect("db/database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        name TEXT,
        email TEXT,
        phone TEXT,
        resume TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS custom_answers (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        ats TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()