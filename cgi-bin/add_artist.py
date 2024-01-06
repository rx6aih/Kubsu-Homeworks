#!/usr/bin/env python3
import cgi
import sqlite3

print("Content-type: text/html\n")

form = cgi.FieldStorage()
artist_name = form.getvalue('artist_name')
category_id = form.getvalue('category_id')

if artist_name and category_id:
    conn = sqlite3.connect('D:\Study\Code\python_code\kubsuPython\Other\Server\cgi-bin\database\circus_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Artist (ArtistName, CategoryID) VALUES (?, ?)", (artist_name, category_id))
    conn.commit()
    conn.close()
    print(f"Location: D:\Study\Code\python_code\kubsuPython\Other\Server\cgi-bin\Result.py\n")
else:
    print("Error: Artist Name and Category ID are required.")
