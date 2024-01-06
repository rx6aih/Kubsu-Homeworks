#!/usr/bin/env python
import cgi
import cgitb
import codecs
import html
import sys

from db import add_Currency

cgitb.enable()

form = cgi.FieldStorage()

name = html.escape(form.getvalue('field-currency_name'))
code = html.escape(form.getvalue('field-code'))

add_Currency(
    name=name,
    code=code,
)

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
                <h1> Валюта {name} успешно добавлена </h1><br>
                <a class="btn btn-success" href="../templates/index.html">На главную</a><br>
            </body>
        </html>
''')
