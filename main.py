from user_dao.select_users import select_user 
from user_dao.insert_user import insert_user
from models.user import User
from user_dao.create_table_user import create_table_user
from UTILS.CONN import get_db
def app():
    cursor,conn=get_db()
    create_table_user(cursor,conn)
    email=input("iserisci la tua email ")
    password=input("insersici la password ")
    insert_user(email,password,cursor,conn)
    print(select_user(cursor))
app()