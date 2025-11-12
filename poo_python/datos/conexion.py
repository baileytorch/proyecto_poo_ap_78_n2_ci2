import mysql.connector

# Connect to server
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="aerolinea")

# Get a cursor
cur = conexion.cursor()

# Execute a query
cur.execute("SELECT CURDATE()")

# Fetch one result
row = cur.fetchone()
print(f"Fecha Actual: {row}")

# Close connection
conexion.close()