import sqlite3

with sqlite3.connect('database.db') as connection : 
    cursor = connection.cursor()

    createTablequery = '''
    create table if not exists Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    '''
    cursor.execute(createTablequery)
    connection.commit()
    print('Query Executed')