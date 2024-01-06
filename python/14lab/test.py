import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con =sqlite3.connect('C:\Program Files\DB Browser for SQLite\exchange.db')
        print('good!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    except Error:
        print(Error+'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    finally:
        con.close()
    