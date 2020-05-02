import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32),
        favorite_color VARCHAR(32)
    );"""

)

connection.commit()
cursor.close()
connection.close()
