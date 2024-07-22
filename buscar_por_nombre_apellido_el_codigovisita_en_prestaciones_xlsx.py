import pandas as pd
import logging
import os
# SCRIPT PARA USAR UN EXCEL DE ENTRADA CON NOMBRE Y APELLIDO, BUSCAR EN PRESTACIONES LOS CODIGOS DE VISITA Y GUARDAR LOS RESULTADOS EN UN EXCEL

EXCEL_INPUT = 'buscados.xlsx'
EXCEL_ARCHIVES = [
    'Prestaciones2019.xlsx',
    'Prestaciones2020.xlsx',
    'Prestaciones2021.xlsx',
    'Prestaciones2022.xlsx',
    'Prestaciones2023.xlsx',
    'Prestaciones2024.xlsx'
]
EXCEL_OUTPUT = 'set_codigo_visita_limpio_salida_b.xlsx'

# Suppress openpyxl warnings
logging.getLogger("openpyxl").setLevel(logging.ERROR)

# Define the function to process archives and obtain the unique 'CODIGO_VISITA' values
def process_archives(main_df, archive_files):
    archive_data = {}
    all_codigo_visita_values = set()  # Initialize an empty set to store all 'CODIGO_VISITA' values
    
    for archive_file in archive_files:
        archive_df = pd.read_excel(archive_file)
        archive_data[archive_file] = archive_df
    
    for index, row in main_df.iterrows():
        nombre = row['NOMBRE_PACIENTE']
        apellido = row['APELLIDO_PACIENTE']
        for archive_df in archive_data.values():
            matching_rows = archive_df[(archive_df['NOMBRE_PACIENTE'] == nombre) & (archive_df['APELLIDO_PACIENTE'] == apellido)]
            codigo_visita_values = set(matching_rows['CODIGO_VISITA'])
            all_codigo_visita_values.update(codigo_visita_values)  # Add unique 'CODIGO_VISITA' values to the set
            
    return tuple(all_codigo_visita_values)  # Return the tuple of unique 'CODIGO_VISITA' values

try:
    # Read the 'buscados' Excel file
    main_df = pd.read_excel(EXCEL_INPUT)
    
    # Get the unique 'CODIGO_VISITA' values from the archive files
    codigo_visita_values_tuple = process_archives(main_df, EXCEL_ARCHIVES)
    #print("Tuple of 'CODIGO_VISITA' values:", codigo_visita_values_tuple)
    
    # Read the 'codigo_visita' Excel file
    codigo_visita_df = pd.DataFrame({'CODIGO_VISITA': codigo_visita_values_tuple})

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
    
except FileNotFoundError:
    print("One or more input files not found.")
except Exception as e:
    print(f"An error occurred: {e}")