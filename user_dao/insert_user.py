def insert_user(email,password,db,con):
    db.execute("INSERT INTO UTENTI (EMAIL,PASSWORD) VALUES (?,?)",(email,password))
    con.commit()
