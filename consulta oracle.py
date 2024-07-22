import cx_Oracle

# Oracle connection details
username = 'Calipso'
password = 'Calafate'
host = '127.21.14.21'
port = '1521'  # Usually 1521 for Oracle
SID = 'WMBD'  # or SID if you're using SID instead of service name

# Construct connection string
dsn = cx_Oracle.makedsn(host, port, SID)

# Establish a connection to the Oracle database
connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)

# Create a cursor
cursor = connection.cursor()

# Execute a sample query
cursor.execute("SELECT * FROM v$version;")

# Fetch the results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.close()