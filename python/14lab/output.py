import sqlite3
con = sqlite3.connect('exchange.db')
def sql_fetch1(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM Employees')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch1(con)

def sql_fetch2(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name,position FROM Employees where Employees.salary=800')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch2(con)

print('----------------------------------------------')

def sql_fetch3(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT currency_id FROM ExchangeRates where ExchangeRates.rate=4')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch3(con)

print('----------------------------------------------')

def sql_fetch4(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT currency_id,amount FROM ExchangeOperations where ExchangeOperations.employee_id=1')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch4(con)

print('----------------------------------------------')

def sql_fetch5(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT email FROM Clients where Clients.name="Kostya"')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch5(con)



def sql_fetch6(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE FROM ExchangeOperations where ExchangeOperations.employee_id=1')
sql_fetch6(con)



def sql_fetch7(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE FROM Clients where Clients.name="Kostya"')
sql_fetch7(con)



def sql_fetch8(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE FROM ExchangeRates where ExchangeRates.rate=4')
sql_fetch8(con)



def sql_fetch9(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE FROM Employees where Employees.salary=800')
sql_fetch9(con)


def sql_fetch10(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE FROM Employees where Employees.salary=1000 and Employees.name="Петухов"')
sql_fetch10(con)

