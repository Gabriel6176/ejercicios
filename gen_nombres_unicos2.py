import pandas as pd
import numpy as np

def procesar_nombres(input_file, output_file):
    df = pd.read_csv(input_file, header=0, names=['Nombre', 'Numero1', 'Numero2'])
    
    nombres_set = set()
    for nombre_completo in df['Nombre']:
        if isinstance(nombre_completo, str):
            nombres = nombre_completo.split(',')
            for nombre in nombres:
                nombre = nombre.strip()
                if ' ' not in nombre:  # Verificar que no haya espacios en el nombre
                    if '(' in nombre and ')' in nombre:
                        pos1 = nombre.find('(')
                        pos2 = nombre.find(')')
                        nombre = nombre[:pos1] + nombre[pos2+1:]
                    nombre = nombre.strip()
                    nombres_set.add(nombre)
        elif isinstance(nombre_completo, float) and np.isnan(nombre_completo):
            continue
    
    # Convertir el conjunto de nombres a una lista y ordenarla alfabéticamente
    nombres_ordenados = sorted(nombres_set)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for nombre in nombres_ordenados:
            f.write(nombre + '\n')

# Llamar a la función para procesar el archivo nombres.csv
procesar_nombres('nombres.csv', 'nombres_separados.txt')

print("Proceso completado. Verifica el archivo nombres_separados.txt para los nombres separados, ordenados alfabéticamente y excluyendo nombres de dos palabras.")





