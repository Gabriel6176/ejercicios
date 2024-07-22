import sqlite3

# Connect to the database
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Function to check if a record with a given NroDocumento exists
def check_existence(nro_documento):
    cursor.execute("SELECT 1 FROM DNI WHERE NroDocumento = ?", (nro_documento,))
    return cursor.fetchone() is not None

# Function to insert a record with default values
def insert_record(nro_documento):
    cursor.execute("INSERT INTO DNI (NroDocumento, Nombre, ObraSocial, Siglas) VALUES (?, '--', '--', '--')", (nro_documento,))
    conn.commit()
    print(f"Inserted record for NroDocumento: {nro_documento}")

# Get the maximum value of NroDocumento from the database
cursor.execute("SELECT MAX(CAST(NroDocumento AS INTEGER)) FROM DNI")
max_nro_documento = cursor.fetchone()[0]

# Loop to check and insert missing consecutive numbers
for i in range(25675000, max_nro_documento + 1):
    if not check_existence(str(i)):
        insert_record(str(i))

# Close the connection
conn.close()