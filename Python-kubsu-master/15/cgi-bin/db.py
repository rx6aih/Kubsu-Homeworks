import sqlite3
from typing import Dict, List

"""Тема таблиц курсы"""


def sqlite_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect('db.db') as con:
            kwargs['con'] = con
            res = func(*args, **kwargs)
            con.commit()
        return res

    return wrapper


employees_data1 = [
    ('Иванов', 'Менеджер', 1000),
    ('Петров', 'Кассир', 800),
    ('Сидоров', 'Кассир', 800),
    ('Бабуинов', 'Запасной вышибала', 1000),
    ('Джунгарик', 'Крутильщик', 800),
    ('Топотун', 'Барабанщик', 800),
    ('Вакуленко', 'Менеджер', 1000),
    ('Телепатов', 'Грузчик', 800),
    ('Макакин', 'Вышибала', 800),
    ('Петухов', 'Курьер', 1000),
    ('Шнырёв', 'Куратор', 800),
    ('Напасенко', 'Тестировщик', 800)
]

currencies_data = [
    ('100', 'Dollar'),
    ('101', 'Euro'),
    ('102', 'Rub'),
    ('103', 'Danish Krone'),
    ('104', 'Austrailan Dollar'),
    ('105', 'Rupee'),
    ('106', 'Yen'),
    ('107', 'Won'),
    ('108', 'Rupiah'),
    ('109', 'Lev')
]

exchangeRates_data = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (2, 3),
    (1, 4),
    (5, 6),
    (2, 7)
]


@sqlite_connection
def init_db(con: sqlite3.Connection):
    'Создаём таблицу с id, цвет,  выдержкой, сортом, страной, описанием вина'
    cur = con.cursor()
    # Создание таблицы "Сотрудники"
    cur.execute("\n"
                "                CREATE TABLE IF NOT EXISTS Employees\n"
                "                (id INTEGER PRIMARY KEY AUTOINCREMENT,  \n"
                "                name TEXT NOT NULL,\n"
                "                position TEXT NOT NULL,\n"
                "                salary REAL NOT NULL\n"
                "                );\n"
                "                ")

    # Создание таблицы "Валюты"
    cur.execute("\n"
                "                    CREATE TABLE IF NOT EXISTS Currencies\n"
                "                    (id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
                "                    code TEXT NOT NULL,\n"
                "                    name TEXT NOT NULL);\n"
                "                ")

    # Создание таблицы "Курсы валют"
    cur.execute('\n'
                '                    CREATE TABLE IF NOT EXISTS ExchangeRates\n'
                '                    (id INTEGER PRIMARY KEY AUTOINCREMENT,\n'
                '                    currency_id INTEGER NOT NULL,\n'
                '                    rate REAL NOT NULL,\n'
                '                    FOREIGN KEY (currency_id) REFERENCES Currencies(id));\n'
                '                ')

    cur.executemany("INSERT INTO Employees (name, position, salary) VALUES (?, ?, ?)", employees_data1)
    cur.executemany('INSERT INTO Currencies (code, name) VALUES (?, ?)', currencies_data)
    cur.executemany("INSERT INTO ExchangeRates (currency_id, rate) VALUES (?, ?)", exchangeRates_data)


@sqlite_connection
def get_all_employees(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('\n'
                '        SELECT name,position \n'
                '        FROM Employees\n'
                '    ')
    return cur.fetchall()


@sqlite_connection
def get_all_currencies(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('\n'
                '        SELECT code, name\n'
                '        FROM Currencies;\n'
                '    ')
    return cur.fetchall()


@sqlite_connection
def get_all_rates(con: sqlite3.Connection) -> List:
    cur = con.cursor()
    cur.execute('\n'
                '        SELECT currency_id, rate\n'
                '        FROM ExchangeRates;\n'
                '    ')
    return cur.fetchall()


@sqlite_connection
def add_employee(con: sqlite3.Connection, SubjectName: str, Position: str, salary: int):
    cur = con.cursor()
    cur.execute('\n'
                '        INSERT INTO Employees (name, position, salary) VALUES (?, ?,?);\n'
                '    ', (SubjectName, Position, salary))


@sqlite_connection
def add_Currency(con: sqlite3.Connection, code, name, ):
    cur = con.cursor()
    cur.execute('\n'
                '        INSERT INTO Currencies (code, name) VALUES (?,?);\n'
                '    ', (code, name))


def update_Employees(con: sqlite3.Connection, position, id: int):
    cur = con.cursor()
    cur.execute('\n'
                '        UPDATE Employees\n'
                '        SET position = (?)\n'
                '        WHERE id = (?)\n'
                '    ', (position, id))


def delete_courses(con: sqlite3.Connection, id: int):
    cur = con.cursor()
    cur.execute("DELETE FROM Employees WHERE id = (?)", (id,))


@sqlite_connection
def add_Currency(con: sqlite3.Connection, code: str, name: str):
    cur = con.cursor()
    cur.execute("INSERT INTO Currencies (code, name) VALUES (?, ?);", (code, name))


@sqlite_connection
def update_Currency_name(course_id: int, new_name: str, con: sqlite3.Connection):
    """
    Обновляет название курса по его идентификатору.
    """
    cur = con.cursor()
    cur.execute('UPDATE Currency SET name = ? WHERE id = ?;', (new_name, course_id))


if __name__ == '__main__':
    init_db()
