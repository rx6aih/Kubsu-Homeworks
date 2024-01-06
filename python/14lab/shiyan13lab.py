import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con=sqlite3.connect('exchange.db')
        return con
    except Error:
        print(Error)


def sql_tables(con):
    
    conn=con.cursor()
    
    # Создание таблицы "Сотрудники"
    conn.execute('''CREATE TABLE IF NOT EXISTS Employees
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary REAL NOT NULL)''')

    # Создание таблицы "Валюты"
    conn.execute('''CREATE TABLE IF NOT EXISTS Currencies
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT NOT NULL,
                    name TEXT NOT NULL)''')

    # Создание таблицы "Курсы валют"
    conn.execute('''CREATE TABLE IF NOT EXISTS ExchangeRates
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    currency_id INTEGER NOT NULL,
                    rate REAL NOT NULL,
                    FOREIGN KEY (currency_id) REFERENCES Currencies(id))''')

    # Создание таблицы "Операции обмена"
    conn.execute('''CREATE TABLE IF NOT EXISTS ExchangeOperations
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER NOT NULL,
                    currency_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES Employees(id),
                    FOREIGN KEY (currency_id) REFERENCES Currencies(id))''')
    conn.execute('''CREATE TABLE IF NOT EXISTS Clients
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT)''')
    con.commit()
    
con=sql_connection()
sql_tables(con)





