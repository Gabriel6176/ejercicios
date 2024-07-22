#generador de ciudades

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento


ciudadesdevueltas=devuelve_ciudades("Madrid", "Berlin", "Viena")

print(next(ciudadesdevueltas))
print(next(ciudadesdevueltas))







    










