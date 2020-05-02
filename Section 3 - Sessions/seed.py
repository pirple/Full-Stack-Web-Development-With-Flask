import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
        )VALUES(
            'Gordon',
            'Ramsay',
            'Red'
        );"""

)

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
        )VALUES(
            'Ironman',
            'Tony',
            'Gold'
        );"""

)

connection.commit()
cursor.close()
connection.close()
