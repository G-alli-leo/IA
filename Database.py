"""
#Window
import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
# Using a DSN, but providing a password as well
cnxn = pyodbc.connect('DSN=test;PWD=password')

# Create a cursor from the connection
cursor = cnxn.cursor()
"""
import sqlite3

#Creating the inventory database and connecting to it
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    Quantity INTEGER DEFAULT 0,
    Price REAL NOT NULL
);
""")

# Insert initial test item
cursor.execute("""
INSERT INTO Products (ProductName, Quantity, Price) 
VALUES (?, ?, ?)
""", ('The Product', 1, 99.99))

conn.commit()

# Fetch and verify data
cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())

conn.close()