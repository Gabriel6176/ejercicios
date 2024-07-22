#from aPelicula import Pelicula
import os

class Catalogo:
    
    ruta_archivo = 'peliculas.txt'
    
    #si hubiese usado @staticmethod no podria haber accedido a ruta_archivo que es un atributo de clase
    @classmethod
    def agregar_pelicula(cls, pelicula):
        #al usar with abre el archivo y lo cierra solo
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
            
    @classmethod        
    def listar_pelicula(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catalogo de Peliculas'.center(50,'-'))
            print(archivo.read())

    @classmethod            
    def eliminar_pelicula(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')

