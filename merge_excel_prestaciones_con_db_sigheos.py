import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import pandas as pd
import sqlite3

# Read the Excel file into a pandas DataFrame
name_excel='Prestaciones2024'
excel_file = f'{name_excel}'+'.xlsx'
worksheet_name = 'Exportar Hoja de Trabajo'
df_excel = pd.read_excel(excel_file, sheet_name=worksheet_name)

# Output
OUTPUT_DB=f'{name_excel}'+'_con_sigheos_os.db'
OUTPUT_TABLE_NAME='Galileo'

# Filter rows where 'CODIGO_VISITA' starts with 'G' or 'GLAB' and extract the number after
df_excel['CODIGO_VISITA'] = df_excel['CODIGO_VISITA'].astype(str)
df_excel['CODIGO_VISITA2'] = df_excel['CODIGO_VISITA'].apply(lambda x: x.lstrip('G').lstrip('LAB'))

# Create a new SQLite database connection
conn = sqlite3.connect('obrasocialxvisita_10052024.db')

# Read the SQLite table into a pandas DataFrame
table_name = 'obrasocialxvisita_10052024'
df_sqlite = pd.read_sql_query(f"SELECT *, codigo_visita AS codigo_visita3 FROM {table_name}", conn)

# Close the database connection
conn.close()

# Ensure 'codigo_visita2' column in df_sqlite is also string type
df_sqlite['codigo_visita3'] = df_sqlite['codigo_visita3'].astype(str)

# Merge the DataFrames on 'CODIGO_VISITA' column
df_merged = pd.merge(df_excel, df_sqlite, left_on='CODIGO_VISITA2', right_on='codigo_visita3', how='inner')

# Drop the 'codigo_visita2' column
df_merged.drop(columns=['codigo_visita'], inplace=True)

# Print the first 5 rows of the merged DataFrame
print(df_merged.head())
# Save the first few rows to a CSV file
df_merged.head().to_csv('first_few_rows.csv', index=False)

# Save the result to a SQLite database table named 'pepe'
conn = sqlite3.connect(f'{OUTPUT_DB}')
df_merged.to_sql(f'{OUTPUT_TABLE_NAME}', conn, if_exists='replace', index=False)

print('-----------------JOB DONE----------------------')

conn.close()
