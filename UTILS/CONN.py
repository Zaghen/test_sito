import sqlite3
def connect():
    conn=sqlite3.connect("db/user.db")
    cursor=conn.cursor()
    conn.row_factory=sqlite3.Row
    return cursor