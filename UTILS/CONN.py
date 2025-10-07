import sqlite3
def get_db():
    conn=sqlite3.connect("db/user.db")
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()
    return cursor,conn