from user_dao.select_users import select_user 
from user_dao.insert_user import insert_user
from models.user import User
from user_dao.create_table_user import create_table_user
def app():
    create_table_user()
    email=input("iserisci la tua email")
    password=input("insersici la password")
    insert_user(email,password)
    a=select_user()
    print(a)
