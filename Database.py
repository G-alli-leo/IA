import pyodbc
"""
ODBC Driver 18.6 was used alongside SQL Server 2025 Express.
For viewing purposes I used SSMS.
Each item in the database is a product with an id, name, price, and quantity.
ID is an INT; Name is a VARCHAR; Price is a Decimal with 10 total digits and 2 decimal places; and Quantity is an INT.
"""

#Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;
# Specifying the ODBC driver, server name, database, etc. directly
    #TODO: Make the commands for query, insert, update, delete, and select
    #Order: Insert, Delete, Query, Select, Update

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=InventoryDB;Trusted_Connection=yes;TrustServerCertificate=yes;"  # Crucial bypass for SSL errors on local setups
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Successfully connected to SQL Server Express!")
    
    # Test query
    cursor.execute("SELECT * FROM Products")
    for row in cursor.fetchall():
        print(row)
        
except Exception as e:
    print(f"Connection failed: {e}")
#def strict_insert(cursor, data: list[str]):
