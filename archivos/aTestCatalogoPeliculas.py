from aPelicula import Pelicula
from aCatalogoPeliculas import Catalogo as cp

opcion = None

while opcion != 4:
    try:
        print("Opciones: ")
        print("1. Agregar película: ")
        print("2. Listar películas: ")
        print("3. Eliminar catálogo de películas: ")
        print("4. Salir: ")
        opcion=int((input("Excribe tu opción (1-4): ")))

        if opcion == 1:
            nombre_pelicula = input('Proporciona un nombre de pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_pelicula()
        elif opcion == 3:
            cp.eliminar_pelicula()

    except Exception as e:
        print(f'Ocurrio un error del tipo: {e}') 
        #como el usuario ingreso un numero invalido es que da error y por eso 'opcion' tomo valor incorrecto y debo volver a ponerle none
        opcion=None

else: 
    print('Salimos del Programa')

