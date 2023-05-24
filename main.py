import sqlite3

from app import App


def init_db(conn):
    cursor = conn.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    date TEXT
    )'''
    cursor.execute(sql)
    conn.commit()


if __name__ == '__main__':
    with sqlite3.connect('budget.db') as connection:
        init_db(connection)
        App(connection)
