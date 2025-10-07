def select_users(db):
    return db.execute("SELECT * FROM UTENTI").fetchall()