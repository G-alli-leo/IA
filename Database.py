#Window
import pyodbc
#ODBC Driver 18.6 was used alongside SQL Server 2025 Express.
#For viewing purposes I used SSMS

#Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;
# Specifying the ODBC driver, server name, database, etc. directly
try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=InventoryDB;Trusted_Connection=yes;TrustServerCertificate=yes;')
    print("Connection established successfully.")
except:
    print("Error: Could not connect to the database.")
#cnxn = pyodbc.connect('DSN=test;PWD=password')
# Create a cursor from the connection
#cursor = cnxn.cursor()