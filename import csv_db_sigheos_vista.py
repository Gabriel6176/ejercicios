import pandas as pd
import sqlite3

# Load the CSV file into a DataFrame
df = pd.read_csv('obrasocialxvisita_10052024.csv')

# Create a SQLite database connection
conn = sqlite3.connect('padron7.db')

# Replace 'your_table_name' with the name you want for your table
table_name = 'obrasocialxvisita_10052024'

# Define column data types
column_types = {
    'tipo_turno': 'TEXT',
    'codigo_turno': 'INTEGER',
    'codigo_visita': 'INTEGER',
    'cmensaje': 'TEXT',
    'nobrasocial': 'INTEGER',
    'dobrasocial': 'VARCHAR(172)',
    'tnroafiliado': 'VARCHAR(25)'
}

# Write the DataFrame to the SQLite database with specified data types
df.to_sql(table_name, conn, index=False, if_exists='replace', dtype=column_types)
print('--------------JOB DONE------------------')
# Commit the changes and close the connection
conn.commit()
conn.close()