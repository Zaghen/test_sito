def select_user(db):
    return db.execute("SELECT * FROM UTENTI").fetchall()