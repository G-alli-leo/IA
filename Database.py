import pyodbc
"""
ODBC Driver 18.6 was used alongside SQL Server 2025 Express.
For viewing purposes I used SSMS.
Each item in the database is a product with an id, name, price, and quantity.
ID is an INT; Name is a VARCHAR; Price is a Decimal with 10 total digits and 2 decimal places; and Quantity is an INT.
"""

#Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;
# Specifying the ODBC driver, server name, database, etc. directly
    #TODO: Make the commands for query, insert, update, delete, and select. Make sure to commit or activate ;autocommit=True
    #Order: Insert, Delete, Query, Select, Update
    #TODO: Add and substract from quantity, and update price.
    #TODO: Make the ID auto-increment in the database, so that the user doesn't have to input it
conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=InventoryDB;Trusted_Connection=yes;TrustServerCertificate=yes;"  # Crucial bypass for SSL errors on local setups
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Successfully connected to SQL Server Express!")

    def validate_data(data: list[str]):
        """
        Data subjected to the DB's rules. ID and Quantity must be integers, Price must be a decimal with 2 decimal places, and Name must be a string. The list must contain exactly 4 elements.
        """
        length=True if (len(data) == 4) else False
        ints=True if (data[0].isdecimal() and data[3].isdecimal()) else False
        decimal=True if (data[2].split('.')[1]).isdecimal() else False #Split into whole and decimal parts, check if decimal part is a number
        if length and ints and decimal == True:
            return True 

    def strict_insert(cursor: pyodbc.Connection, data: list[str]):
        """
        Inserts a new product into the Products table. Full data must be provided: [id, name, price, quantity].
        """
        if validate_data(data):
            cursor.execute("INSERT INTO Products (ProductID, ProductName, Quantity, Price) VALUES (?, ?, ?, ?)", (data[0], data[1], data[2], data[3]))
            conn.commit()
        else:
            print("Data validation failed. Ensure ID and Quantity are integers, Price is a decimal with 2 decimal places, and Name is a string.")
        
    def ID_delete(cursor: pyodbc.Connection, ID: int):
        """
        Deletes a given product based on their ProductID 
        """
        cursor.execute("DELETE FROM Products WHERE ProductID=?", (ID))

    #def strict_query(cursor: pyodbc.Connection, *data: list[str]):
    #    cursor.execute("SELECT * FROM Products WHERE b=? AND c=?", (data[0], data[1]))
except Exception as e:
    print(f"Connection failed: {e}")

