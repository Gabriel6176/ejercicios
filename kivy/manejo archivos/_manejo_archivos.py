


try:
    #---tengo que poner dos diagonales siempre para indicar la ruta. en MAC o LINUx se utiliza diagonal hacia adelante 
    archivo=open('C:\\Users\\usuario\\Downloads\\Python\\gaby.txt', 'r+')
    #---leer los primeros 5 caracteres
    #print(archivo.read(5))
    #---leer los siguientes 3 caracteres
    #print(archivo.read(3))
    #----para leer la primera linea completa
    #print(archivo.readline())
    #-----si quiero leer la segun linea le agrego una line mas de codigo
    #print(archivo.readline())
    #----leer todas las lineas
    #for linea in archivo:
    #    print(linea)
    #----------leer solo lineas en formato de lista    
    #print(archivo.readlines())
    #----------leer solo una linea    
    #print(archivo.readlines()[0])
    #----crear copia del archivo original----"a" es append informacion--
    # si uso 'a' varias veces agrega lo mismo muchas veces sino usar solo "w" y de ultima sobre escribe--------
    archivo2 = open('copia.txt', 'a')
    archivo2.write(archivo.read())
    archivo2.close()


except Exception as e:
    print(e)
finally:
    archivo.close()


## ------- si uso 'w+' es para escribir y leer al igual que 'r+'-----

####----------------crear archivo--------------------------------
'''
try:
    #---aca con ecoding le indico que puedo poner acentos-----
    archivo = open('gaby.txt', 'w', encoding='utf8')
    archivo.write('Sos el más capito\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
'''
###---------------------------------------------------------------

