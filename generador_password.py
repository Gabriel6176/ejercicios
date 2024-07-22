import pandas as pd

# Leer el archivo nombres_separados.txt
df = pd.read_csv('nombres_separados.txt', header=None, names=['Nombre'])

# Abrir (o crear) el archivo passwords.txt en modo escritura
with open('passwords.txt', 'w') as f:
    for nombre in df['Nombre']:
        nombre_c = nombre.capitalize()  # Capitaliza la primera letra del nombre
        
        # Escribir el nombre seguido de un salto de línea
        f.write(f"{nombre_c}\n")
        
        # Generar contraseñas con números del 1 al 1000
        for num in range(1, 1001):
            f.write(f"{nombre_c}{num}\n")
        
        # Generar contraseñas con años del 1950 al 2025
        for año in range(1950, 2026):
            f.write(f"{nombre_c}{año}\n")

