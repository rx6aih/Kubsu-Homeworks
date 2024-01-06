#!/usr/bin/env python3
print("Content-type: text/html\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Artist</title>
</head>
<body>
    <h1>Add Artist</h1>
    <form action="/cgi-bin/add_artist.py" method="post">
        <label for="artist_name">Artist Name:</label>
        <input type="text" name="artist_name" required><br>

        <label for="category_id">Category ID:</label>
        <input type="number" name="category_id" required><br>

        <input type="submit" value="Add Artist">
    </form>
    <p><a href="D:\Study\Code\python_code\kubsuPython\Other\Server\cgi-bin\Result.py">View Result</a></p>
</body>
</html>
""")

