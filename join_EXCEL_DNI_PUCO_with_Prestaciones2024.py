import pandas as pd
import sqlite3

# Read the Excel file
excel_file = 'DNI_prestaciones_2024.xlsx'
df_excel = pd.read_excel(excel_file)

# Read data from SQLite database
db_file = 'Prestaciones2024.db'
conn = sqlite3.connect(db_file)
query = "SELECT * FROM Galileo;"
df_sqlite = pd.read_sql_query(query, conn)
conn.close()

# Convert the 'NUM_DOCUMENTO_PACIENTE' column to match the data type of 'DNI'
df_sqlite['NUM_DOCUMENTO_PACIENTE'] = df_sqlite['NUM_DOCUMENTO_PACIENTE'].astype(str)

# Convert the 'DNI' column in the Excel DataFrame to strings
df_excel['DNI'] = df_excel['DNI'].astype(str)

# Merge the dataframes based on the common column "NUM_DOCUMENTO_PACIENTE"
merged_df = pd.merge(df_sqlite, df_excel, how='left', left_on='NUM_DOCUMENTO_PACIENTE', right_on='DNI')

# Add "puco_" prefix only to column titles from the Excel file
excel_columns = df_excel.columns
merged_df.rename(columns={col: 'puco_' + col if col in excel_columns else col for col in merged_df.columns}, inplace=True)

# Write the merged dataframe to a new SQLite database
output_db_file = 'Prestaciones2024_puco.db'
conn = sqlite3.connect(output_db_file)
merged_df.to_sql('Galileo', conn, if_exists='replace', index=False)
conn.close()

print("Merged data saved to Prestaciones2024_puco.db")