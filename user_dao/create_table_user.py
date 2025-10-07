def create_table_user(db,con):
    db.execute("CREATE TABLE IF NOT EXISTS UTENTI(EMAIL TEXT NOT NULL UNIQUE,PASSWORD TEXT NOT NULL,PRIMARY KEY(EMAIL))")
    con.commit()
    