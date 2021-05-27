import os
import sqlite3


def execute_query(query, args=()):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    # db_path = 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    records = cur.fetchall()
    return records
