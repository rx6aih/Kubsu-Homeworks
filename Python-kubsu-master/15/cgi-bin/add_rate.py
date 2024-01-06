#!/usr/bin/env python
import cgi
import sqlite3

print("Content-type: text/html\n")  # Заголовок HTTP-ответа

form = cgi.FieldStorage()

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Обработка данных из формы и добавление их в базу данных
if form.getvalue('name') and form.getvalue('id'):
    currency_id = form.getvalue('course_name')
    rate = form.getvalue('instructor_id')

    # Вставка данных в таблицу Courses
    cursor.execute("INSERT INTO ExchangeRates (currency_id, rate) VALUES (?, ?)", (currency_id, rate))
    conn.commit()

# HTML форма для ввода данных
print('''
<!DOCTYPE html>

<html lang="ru">
            <head>
                <title>БД</title>
                <meta charset="UTF-8">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
            </head>
    <h1>Добавить курс в базу данных</h1>
    <form method="post" action="">
        <label for="course_name">код валюты:</label><br>
        <input type="text" id="course_name" name="course_name"><br><br>

        <label for="instructor_id">курс валюты:</label><br>
        <input type="text" id="instructor_id" name="instructor_id"><br><br>

        <input type="submit" value="Добавить курс">
    </form>
</body>
</html>
''')

conn.close()