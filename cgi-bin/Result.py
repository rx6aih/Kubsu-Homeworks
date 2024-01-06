#!/usr/bin/env python3
import sqlite3

print("Content-type: text/html\n")

conn = sqlite3.connect('D:\Study\Code\python_code\kubsuPython\Other\Server\cgi-bin\database\circus_database.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Artist")
artists = cursor.fetchall()
conn.close()

print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
</head>
<body>
    <h1>Result</h1>
    <ul>
""")
for artist in artists:
    print(f"        <li>{artist[1]}, Category ID: {artist[2]}</li>")
print("""
    </ul>
    <p><a href="/cgi-bin/index.html">Back to Add Artist</a></p>
</body>
</html>
""")
