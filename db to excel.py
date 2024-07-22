#db to excel

import pandas as pd
import sqlite3

DATA_BASE= 'Prestaciones2024_puco.db'
YOUR_TABLE= 'Galileo'
OUTPUT_FILE= 'Prestaciones2024_puco.xlsx'

# Connect to the SQLite database
conn = sqlite3.connect(DATA_BASE)

# Read data from the database table into a pandas DataFrame
query = f"SELECT * FROM {YOUR_TABLE};"
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Write the DataFrame to an Excel file
df.to_excel(OUTPUT_FILE, index=False)

print("Conversion from .db to Excel is complete.")