import sqlite3
from sqlite3 import Error
conn = sqlite3.connect('exchange.db')
# Заполнение таблицы "Сотрудники"
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

currencies_data= [
    ('100','Dollar'),
    ('101','Euro'),
    ('102','Rub'),
    ('103','Danish Krone'),
    ('104','Austrailan Dollar'),
    ('105','Rupee'),
    ('106','Yen'),
    ('107','Won'),
    ('108','Rupiah'),
    ('109','Lev')
]

exchangeRates_data=[
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (2,3),
    (1,4),
    (5,6),
    (2,7)
]

exchangeOperations_data=[
    (1,1,300),
    (1,2,4),
    (1,3,12051),
    (2,1,3004),
    (4,5,20),
    (1,2,104),
    (3,2,299),
    (5,7,300),
    (7,3,4000),
    (8,4,1000000)
]

clients_data=[
    ('Travis','+8000232133','assap@gmail.com'),
    ('Timmy','+8000232133','LiKeAbO$$@gmail.com'),
    ('Tomas','+8000232133','goofy@gmail.com'),
    ('Evgeniy','+8000232133','ponosenko@gmail.com'),
    ('Reji','+8000232133','hima@gmail.com'),
    ('Vladimir','+8000232133','rx6aih@gmail.com'),
    ('Kostya','+8000232133','gangster_v_kedah@gmail.com'),
    ('Harry','+8000232133','volshebnaya_palochka@gmail.com'),
    ('Antony','+8000232133','bobby2007@gmail.com'),
    ('Vasya','+8000232133','vasya_pupkinovichenov@gmail.com'),
]
def sql_insert1(con,employees_data1):
    cursorObj=con.cursor()
    cursorObj.executemany('INSERT INTO Employees (name, position, salary) VALUES (?, ?, ?)', employees_data1)
    con.commit()
sql_insert1(conn,employees_data1)

def sql_insert2(con,currencies_data):
    cursorObj=con.cursor()
    cursorObj.executemany('INSERT INTO Currencies (code, name) VALUES (?, ?)', currencies_data)
    con.commit()
sql_insert2(conn,currencies_data)

def sql_insert3(con,exchangeRates_data):
    cursorObj=con.cursor()
    cursorObj.executemany('INSERT INTO ExchangeRates (currency_id, rate) VALUES (?, ?)', exchangeRates_data)
    con.commit()
sql_insert3(conn,exchangeRates_data)

def sql_insert4(con, exchangeOperations_data):
    cursorObj=con.cursor()
    cursorObj.executemany('INSERT INTO ExchangeOperations (employee_id, currency_id, amount) VALUES (?, ?, ?)', exchangeOperations_data)
    con.commit()
sql_insert4(conn,exchangeOperations_data)

def sql_insert5(con,clients_data):
    cursorObj=con.cursor()
    cursorObj.executemany('INSERT INTO Clients (name, phone, email) VALUES (?,?,?)', clients_data)
    con.commit()
sql_insert5(conn,clients_data)

# Сохранение изменений и закрытие соединения с базой данных
