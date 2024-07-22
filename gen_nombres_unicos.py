# Inicializamos una lista vacía para almacenar los nombres únicos
nombres_unicos = []

# Abrimos el archivo nombres.csv y leemos cada línea
with open('nombres.csv', 'r') as archivo:
    for linea in archivo:
        # Dividimos la línea por las comas
        partes = linea.strip().split(',')
        
        # Obtenemos el nombre
        nombre = partes[0]
        
        # Dividimos el nombre en caso de que tenga más de una palabra
        nombres = nombre.split()
        
        # Iteramos sobre las palabras del nombre
        for n in nombres:
            # Verificamos si el nombre no está en la lista de nombres únicos
            if n not in nombres_unicos:
                nombres_unicos.append(n)

# Escribimos los nombres únicos en el archivo nombres.txt
with open('nombres.txt', 'w') as archivo_salida:
    for nombre_unico in nombres_unicos:
        archivo_salida.write(nombre_unico + '\n')

print("Proceso completado. Los nombres únicos se han guardado en nombres.txt.")
