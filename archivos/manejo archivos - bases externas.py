# manejo archivos externos
# crear archivo externo
# abrir archivo externo
# manipularlo
# cerrar archivo externo

#docs.python.org/3/library//io.html
##(r) lectura - (w)=escritura - (a) append

#from io import open

#PARA LECTURA Y ESCRITURA
##archivo_texto=open("archivo.txt","r+")

#texto=archivo_texto.readlines()
#archivo_texto.close()
#print(texto)

#lineas_texto=archivo_texto.readlines()
#archivo_texto.close()
#print(lineas_texto[1])

#archivo_texto.write("\n Hola")

#archivo_texto=open("archivo.txt","r")
#lineas=archivo_texto.readlines()    #lee por linea
##convierte a lista manipulable
#archivo_texto.close()
#print(lineas[0])
#accedo solo a la linea de texto numero 0

#agrega y lee
#archivo_texto=open("archivo.txt","a")
#archivo_texto.write("siempre es lindo")
#archivo_texto=open("archivo.txt","r")
#print(archivo_texto.read())
#archivo_texto.close()

#como situar un puntero en un lugar - seek
#from io import open
#archivo_texto=open("archivo.txt","r")
#print(archivo_texto.read())
#archivo_texto.seek(25)           #vuelve a cero e imprime desde el punto 25
#print(archivo_texto.read(30))   #que lea desde el 25 hasta carter 25+30

# lee el total de longitud y solo leo la mitad
#from io import open
#archivo_texto=open("archivo.txt","r")
#archivo_texto.seek(len(archivo_texto.read())/2)
#print(archivo_texto.read())

from io import open
archivo_texto=open("archivo.txt","r+")
lista_texto=archivo_texto.readlines()
lista_texto[1]=" Esta linea ha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
print(archivo_texto.readlines())


















