#!/usr/bin/env python
import cgi
import sqlite3

print("Content-type: text/html\n")  # Заголовок HTTP-ответа

form = cgi.FieldStorage()

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Обработка данных из формы и обновление информации в базе данных
if form.getvalue('id') and (form.getvalue('name') or form.getvalue('salary')):
    id = form.getvalue('id')
    name = form.getvalue('name')
    salary = form.getvalue('salary')

    # Обновление данных в таблице Employees
    if id:
        cursor.execute("UPDATE Employees SET name = ? WHERE id = ?", (name, id))
    if salary:
        cursor.execute("UPDATE Employees SET salary = ? WHERE id = ?", (instructor_id, course_id))

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
<body>
    <h1>Обновление информации о сотрудниках</h1>
    <form method="post" action="">
        <label for="course_id">ID Сотрудника:</label><br>
        <input type="text" id="id" name="id"><br><br>

        <label for="course_name">Новое имя сотрудника:</label><br>
        <input type="text" id="name" name="name"><br><br>

        <label for="instructor_id">Новая зарплата:</label><br>
        <input type="text" id="id" name="id"><br><br>

        <input class="btn btn-danger" type="submit" value="Обновить информацию">
    </form>
</body>
</html>
''')

conn.close()