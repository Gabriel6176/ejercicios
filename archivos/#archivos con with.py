#archivos con with

#manejo de contexto with - no necesito cerrar el archivo usando with
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
#    print(archivo.read())

#manejo archivo con clase Manejoarchivo
from clase_manejo_archivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
