# database.py
import sqlite3
import os

def create_database_file():
        open('database.db', 'w').close()

def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            UserID INTEGER PRIMARY KEY,
            email VARCHAR,
            password VARCHAR,
            username VARCHAR,
            role VARCHAR,
            createdAt DATETIME,
            lastLogin DATETIME
        )
    ''')

    # Create Admin table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Admin (
            AdminID INTEGER PRIMARY KEY,
            UserID INTEGER,
            FOREIGN KEY (UserID) REFERENCES Users (UserID)
        )
    ''')

    # Create Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INTEGER PRIMARY KEY,
            UserID INTEGER,
            FOREIGN KEY (UserID) REFERENCES Users (UserID)
        )
    ''')

    # Create Restaurants table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Restaurants (
            RestaurantID INTEGER PRIMARY KEY,
            name VARCHAR,
            addressID INTEGER,
            averageRating FLOAT,
            totalRating INTEGER,
            status VARCHAR,
            FOREIGN KEY (addressID) REFERENCES Address (AddressID)
        )
    ''')

    # Create Dish table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Dish (
            DishID INTEGER PRIMARY KEY,
            restaurantID INTEGER,
            dishName VARCHAR,
            description VARCHAR,
            cost DECIMAL,
            createdAt DATETIME,
            FOREIGN KEY (restaurantID) REFERENCES Restaurants (RestaurantID)
        )
    ''')

    # Create Address table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Address (
            AddressID INTEGER PRIMARY KEY,
            UserID INTEGER,
            addressLine VARCHAR,
            city VARCHAR,
            state VARCHAR,
            country VARCHAR,
            pinCode INTEGER,
            FOREIGN KEY (UserID) REFERENCES Users (UserID)
        )
    ''')

    # Create Orders table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            OrderID INTEGER PRIMARY KEY,
            CustomerID INTEGER,
            DishID INTEGER,
            AddressID INTEGER,
            RestaurantID INTEGER,
            quantity INTEGER,
            status VARCHAR,
            timestamp DATETIME,
            FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID),
            FOREIGN KEY (DishID) REFERENCES Dish (DishID),
            FOREIGN KEY (AddressID) REFERENCES Address (AddressID),
            FOREIGN KEY (RestaurantID) REFERENCES Restaurants (RestaurantID)
        )
    ''')

    # Create Reviews table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Reviews (
            ReviewID INTEGER PRIMARY KEY,
            RestaurantID INTEGER,
            CustomerID INTEGER,
            rating INTEGER,
            role VARCHAR,
            title VARCHAR,
            content VARCHAR,
            createdAt DATETIME,
            FOREIGN KEY (RestaurantID) REFERENCES Restaurants (RestaurantID),
            FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
        )
    ''')

    # Create Category table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Category (
            CategoryID INTEGER PRIMARY KEY,
            categoryName VARCHAR
        )
    ''')

    # Create CategoryDish table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CategoryDish (
            CategoryID INTEGER,
            DishID INTEGER,
            PRIMARY KEY (CategoryID, DishID),
            FOREIGN KEY (CategoryID) REFERENCES Category (CategoryID),
            FOREIGN KEY (DishID) REFERENCES Dish (DishID)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database_file()
    create_tables()
    print('Tables created successfully.')
