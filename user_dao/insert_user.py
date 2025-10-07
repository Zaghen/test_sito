def insert_user(email,password,db,con):
    "permette di registrare gli utenti"
    db.execute("INSERT INTO UTENTI (EMAIL,PASSWORD) VALUES (?,?)",(email,password))
    con.commit()
