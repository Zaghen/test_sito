from UTILS.CONN import connect
def create_table_user():
    db=connect()
    db.execute("CREATE TABLE UTENTI(EMAIL TEXT NOT NULL UNIQUE,PASSWORD TEXT NOT NULL,PRIMARY KEY(EMAIL));")
    