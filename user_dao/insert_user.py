from UTILS.CONN import connect
def insert_user(email,password):
    db=connect()
    db.execute("INSERT INTO UTENTI (EMAIL,PASSWORD) VALUES (?,?)",(email,password))
