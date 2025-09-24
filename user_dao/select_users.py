from UTILS.CONN import connect
def select_user():
    db=connect()
    print(db.execute("SELECT * UTENTI;").fetchall())