#!/usr/bin/env python
import cgi
import sqlite3

print("Content-type: text/html\n")  # Заголовок HTTP-ответа

form = cgi.FieldStorage()

# Установка соединения с базой данных
conn = sqlite3.connect('db.db')
cursor = conn.cursor()
deleted = False

# Обработка данных из формы и удаление записей из базы данных
if form.getvalue('id'):
        course_id = form.getvalue('id')
        # Удаление записи по CourseID из таблицы Emlployees
        cursor.execute("DELETE FROM Employees WHERE id = ?", id,)
        conn.commit()
        deleted = True

if deleted:
    print("<p>Сотрудник уволен!</p>")
# HTML форма для ввода данных
print(f'''
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>БД</title>
    <meta charset="UTF-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
</head>
<body>
    <h1>Удалить сотрудника из базы данных</h1>
    <form method="post" action="">
        <label for="course_id">Введите id сотрудника, который нужно удалить:</label><br>
        <input type="text" id="id" name="id"><br><br>

        <input class="btn btn-danger" type="submit" value="Удалить">
    </form>
    
                <a class="btn btn-success" href="../templates/index.html">На главную</a><br> 
</body>
</html>
''')

conn.close()