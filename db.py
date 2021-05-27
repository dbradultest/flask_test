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

def get_customers_by_name(first_name, last_name):
    query = f"select * from customers"

    where_filter = {}
    if first_name:
        where_filter['FirstName'] = first_name
    if last_name:
        where_filter['LastName'] = last_name

    if where_filter:
        query += ' WHERE ' + ' OR '.join(f'{k}=\'{v}\'' for k, v in where_filter.items())

    records = execute_query(query)

    return records