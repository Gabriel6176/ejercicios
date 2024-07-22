
##----lo bueno de usar with es que no lo tengo que cerrar--- y le indico que es la variable archivo
#with open('C:\\Users\\usuario\\Downloads\\Python\\gaby.txt', 'r', encoding='utf8') as archivo:

####-----es el "nombre del archivo" donde tengo la clase y el "nombre de la clase"
from ManejoArchivo import ManejoArchivo

        
with ManejoArchivo('C:\\Users\\usuario\\Downloads\\Python\\gaby.txt') as archivo:
    print(archivo.read())
