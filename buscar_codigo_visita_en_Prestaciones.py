import pandas as pd
import logging

EXCEL_INPUT = 'set_codigo_visita_limpio.xlsx'
EXCEL_ARCHIVES = [
    'Prestaciones2019.xlsx',
    'Prestaciones2020.xlsx',
    'Prestaciones2021.xlsx',
    'Prestaciones2022.xlsx',
    'Prestaciones2023.xlsx',
    'Prestaciones2024.xlsx'
]
EXCEL_OUTPUT = 'set_codigo_visita_limpio_salida.xlsx'

# Suppress openpyxl warnings
logging.getLogger("openpyxl").setLevel(logging.ERROR)

# Read the 'codigo_visita' Excel file
codigo_visita_df = pd.read_excel(EXCEL_INPUT, header=None, names=['CODIGO_VISITA'])

# Create an empty DataFrame to store the concatenated filtered data
concatenated_df = pd.DataFrame()

# Iterate over each archive file
for archive_file in EXCEL_ARCHIVES:
    # Read the archive file
    archive_df = pd.read_excel(archive_file)
    
    # Filter rows where 'CODIGO_VISITA' matches values from the 'codigo_visita' file
    filtered_df = archive_df[archive_df['CODIGO_VISITA'].isin(codigo_visita_df['CODIGO_VISITA'])]
    
    # Concatenate the filtered DataFrame with the existing data
    concatenated_df = pd.concat([concatenated_df, filtered_df])

# Write the concatenated DataFrame to the output file
concatenated_df.to_excel(EXCEL_OUTPUT, index=False)

print(f"Filtered data written to {EXCEL_OUTPUT}")