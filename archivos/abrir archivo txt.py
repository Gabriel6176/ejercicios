#como abrir archivo este tiene que estar en el mismo directorio 
#importante cuando copias la ruta de acceso puede usar la bara alt+92 por las dudas cambialas por alt+47

#f = open("texto.txt") 
#for linea  in f:
#    print(linea,end="")
#f.close()

#opcion 2 poner la ruta completa
#f = open("/Users/usuario/Downloads/Python/texto.txt") 
#for linea  in f:
#    print(linea,end="")
#f.close()


#opcion 3 sirve para que busque el archivo txt en la misma carpeta donde tengo el archivo python.
#http://www.delftstack.com/es/howto/python/how-to-get-the-current-script-file-directory/

import os

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)

#print(f"Script file path is {path}, filename is {filename}")

print(path+"texto.txt")

f = open(path+"/texto.txt") 
for linea  in f:
    print(linea,end="")
f.close()

