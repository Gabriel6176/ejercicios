import pandas as pd
import sqlite3

# Read data from base.db into a DataFrame
conn = sqlite3.connect('base.db')
query = "SELECT NroDocumento, Nombre, ObraSocial, Siglas FROM dni"
df = pd.read_sql_query(query, conn)

# Sort the DataFrame by NroDocumento column
df_sorted = df.sort_values(by='NroDocumento')

# Write the sorted data to base_1.db
conn_new = sqlite3.connect('base_1.db')
df_sorted.to_sql(name='dni_sorted', con=conn_new, index=False)

# Close the connections
conn.close()
conn_new.close()