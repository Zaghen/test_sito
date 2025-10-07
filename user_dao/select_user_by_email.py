def select_user_by_email(email,db):
    return db.execute("SELECT * FROM UTENTI WHERE EMAIL=?",(email))