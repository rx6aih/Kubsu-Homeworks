#!/usr/bin/env python

import cgitb

from db import get_all_employees, get_all_currencies, get_all_rates

cgitb.enable()

print("Content-type: text/html")
print(f'''
        <!DOCTYPE html>
        <html lang="ru">
            <head>
                <title>БД</title>
                <meta charset="UTF-8">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
            </head>
            <body>
                <h1> Список сотрудников </h1>
                <ul class="list-group">
                        ''')
try:
    for row in get_all_employees():
        print(f'<li class="list-group-item">{row}св</li>')
    print('''
                    </ul>
                    <h1> Список Валют </h1>
                    <ul class="list-group">''')
except Exception:
    pass
try:
    for row in get_all_currencies():
        print(f'<li>{row}</li>')
    print('''
                    </ul>
                    <h1> Курсы </h1>
                    <ul>''')
except Exception:
    pass
try:
    for row in get_all_rates():
        print(f'<li>{row}</li>')
except Exception:
    pass
print('\n'
      '                <form action="../cgi-bin/xml_to_sql.py">\n'
      '                    <input type="submit" class="btn btn-warning" value="Создать БД из xml">\n'
      '                </form><br>\n'
      '                <a class="btn btn-success" href="../templates/index.html">На главную</a><br>\n'
      '                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>\n'
      '            </body>\n'
      '        </html>\n'
      '        ')
