from user_dao.select_user_by_email import select_user_by_email
from user_dao.insert_user import insert_user
from models.user import User
from user_dao.create_table_user import create_table_user
from UTILS.CONN import get_db
def app():
    cursor,conn=get_db()
    create_table_user(cursor,conn)
    scelta=input("scegli fra sign-up account o log-in ")
    scelte=["sign-up","log-in"]
    if scelta in scelte:
        if scelta=="sign-up":
            email=input("inserisci email")
            password=input("inserisci password")
            insert_user(email,password,cursor,conn)
        else:
            email=input("inserisci email")
            if select_user_by_email(email,cursor)==list():
                print("email non esistente registrati o riprova")
            else:
                print("accesso effettuato")
app()