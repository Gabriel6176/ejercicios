import os
import pandas as pd

def csv_to_xls(csv_file, xlsx_file):
    # Leer el archivo CSV
    df = pd.read_csv(csv_file)
    
    # Escribir el DataFrame en un archivo Excel
    df.to_excel(xlsx_file, index=False)

# Verificar el directorio actual
print("Directorio actual:", os.getcwd())

# Listar archivos en el directorio actual
#print("Archivos en el directorio actual:", os.listdir(os.getcwd()))

# Ruta del archivo CSV de entrada
csv_file = 'C:\\Users\\PC\\Desktop\\B2021\\facturas_venta_samic_20_21.csv'

# Ruta del archivo Excel de salida
xlsx_file = 'C:\\Users\\PC\\Desktop\\B2021\\facturas_venta_samic_20_21.xlsx'

# Llamada a la función para convertir
csv_to_xls(csv_file, xlsx_file)

print("¡Conversión completada!")


'''import pandas as pd

def csv_to_xls(csv_file, xlsx_file):
    # Leer el archivo CSV
    df = pd.read_csv(csv_file)
    
    # Escribir el DataFrame en un archivo Excel
    df.to_excel(xlsx_file, index=False)

# Ruta del archivo CSV de entrada
csv_file = 'ordenpago2021.csv'

# Ruta del archivo Excel de salida
xlsx_file = 'ordenpago2021.xlsx'

# Llamada a la función para convertir
csv_to_xls(csv_file, xlsx_file)

print("¡Conversión completada!")
'''