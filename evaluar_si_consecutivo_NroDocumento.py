import sqlite3
import pandas as pd
import csv

# Connect to your SQLite database and read the column into a DataFrame
conn = sqlite3.connect('base.db')
df = pd.read_sql_query("SELECT NroDocumento FROM DNI", conn)

# Close the connection
conn.close()

# Convert column values to integers
df['NroDocumento'] = df['NroDocumento'].astype(int)

# Check for consecutive numbers
if df['NroDocumento'].diff().eq(1).all():
    print("The column contains all consecutive numbers.")
else:
    print("The column contains some non-consecutive numbers.")
    # Find missing numbers
    min_val = df['NroDocumento'].min()
    max_val = df['NroDocumento'].max()
    missing_numbers = list(set(range(min_val, max_val + 1)).difference(df['NroDocumento']))
    print("Missing numbers:", missing_numbers)
    num_missing = len(missing_numbers)
    print("Cantidad de Numeros faltantes", num_missing)
    #write missing numbers to csv files
    csv_file_path = 'data_xxx.csv'
    # Write the list to a CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows([list(missing_numbers)])
    print("Listado guardado en archivo CSV llamado:", csv_file_path)

    

'''import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Replace 'your_table' and 'NroDocumento' with the actual table and column names
cursor.execute("SELECT NroDocumento FROM DNI")  

# Fetch all rows from the query result
rows = cursor.fetchall()

# Extract the values from the fetched rows into a list and convert them to integers
column_values = [int(row[0]) for row in rows]

# Close the cursor and the connection
cursor.close()
conn.close()

# Function to check if a list contains consecutive numbers
def has_consecutive(lst):
    return sorted(lst) == list(range(min(lst), max(lst)+1))

# Function to find missing numbers
def find_missing_numbers(lst):
    min_val = min(lst)
    max_val = max(lst)
    return [num for num in range(min_val, max_val + 1) if num not in lst]

# Check if the column has all consecutive numbers
if has_consecutive(column_values):
    print("The column contains all consecutive numbers.")
else:
    print("The column contains some non-consecutive numbers.")
    # Find the missing numbers
    missing_numbers = find_missing_numbers(column_values)
    print("Missing numbers:", missing_numbers)'''