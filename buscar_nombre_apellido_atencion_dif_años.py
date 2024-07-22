import pandas as pd
import os

EXCEL_BUSQUEDA = 'buscados.xlsx'
EXCEL_ARCHIVES = [
    'Prestaciones2019.xlsx',
    'Prestaciones2020.xlsx',
    'Prestaciones2021.xlsx',
    'Prestaciones2022.xlsx',
    'Prestaciones2023.xlsx',
    'Prestaciones2024.xlsx'
]
EXCEL_SALIDA='resultados_busqueda.xlsx'

def process_archives(main_df, archive_files):
    archive_data = {}
    for archive_file in archive_files:
        archive_df = pd.read_excel(archive_file)
        archive_data[archive_file] = archive_df
    
    for index, row in main_df.iterrows():
        nombre = row['NOMBRE_PACIENTE']
        apellido = row['APELLIDO_PACIENTE']
        codigo_visita_sets = []
        for archive_file, archive_df in archive_data.items():
            matching_rows = archive_df[(archive_df['NOMBRE_PACIENTE'] == nombre) & (archive_df['APELLIDO_PACIENTE'] == apellido)]
            codigo_visita_set = set(matching_rows['CODIGO_VISITA'])
            codigo_visita_sets.append(codigo_visita_set)
        main_df.at[index, 'SET_CODIGO_VISITA'] = str(codigo_visita_sets)

try:
    main_df = pd.read_excel(EXCEL_BUSQUEDA)
    process_archives(main_df, EXCEL_ARCHIVES)
    main_df.to_excel(f'{EXCEL_SALIDA}', index=False)
    print(f"Results written to '{EXCEL_SALIDA}'")
except FileNotFoundError:
    print("One or more input files not found.")
except Exception as e:
    print(f"An error occurred: {e}")