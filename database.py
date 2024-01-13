# database.py
import sqlite3
import os

def create_database_file():
     if not os.path.exists('database.db'):
        # If not, create the database file
        open('database.db', 'w').close()


def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    # Create other tables as needed (add your menu-related tables here)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database_file()
    create_tables()
    print('Tables created successfully.')
