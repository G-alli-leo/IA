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
def add_product(product_name, quantity, price):
    cursor.execute("""
    INSERT INTO Products (ProductName, Quantity, Price) 
    VALUES (?, ?, ?)
    """, (product_name, quantity, price))
    conn.commit()
"""
#High risk, no reward. (SQL injection possible)
def query_product(where_clause: str, *args):
    sql = f"SELECT * FROM Products WHERE {where_clause}"
    cursor.execute(sql, args)  # 'args' is automatically a tuple
    return cursor.fetchall()
"""
def query_id(product_id: int):
    cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
    return cursor.fetchall()

def query_name(name: str):
    cursor.execute("SELECT * FROM Products WHERE ProductName = ?", (name,))
    return cursor.fetchall()

def query_price_range(min_price: float, max_price: float):
    cursor.execute("SELECT * FROM Products WHERE Price BETWEEN ? AND ?", (min_price, max_price))
    return cursor.fetchall()

def query_all():
    cursor.execute("SELECT * FROM Products")


def delete_ID(product_id: int):
    cursor.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
    conn.commit()

def delete_name(name: str):
    cursor.execute("DELETE FROM Products WHERE ProductName = ?", (name,))
    conn.commit()

# Insert initial test item
cursor.execute("""
INSERT INTO Products (ProductName, Quantity, Price) 
VALUES (?, ?, ?)
""", ('The Product', 1, 99.99))

conn.commit()

# Fetch and verify data. Only The Product should appear for now
cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())

conn.close()