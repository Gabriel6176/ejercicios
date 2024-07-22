
try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    #print(archivo.read())
    
    #como leer algunos caracteres para leerlos primeros 5
    'print(archivo.read(5))'
    #como leer los primeros 3 caracteres y luegos los 5
    'print(archivo.read(3))'
    'print(archivo.read(5))'
    #como leer una linea
    'print(archivo.readline())'
    'print(archivo.readline())'
    #para leer todas las lineas de a una
    'for linea in archivo:'
    '   print(linea)'
    #leer lineas(esta es la linea 2 ya que comienza desde cero)
    'print(archivo.readlines()[1])'
    #o readline()[2] - leer linea item 2
    'print(archivo.readline()[2])'
    #copiar archivo en nuevo archivo - a append no borra ni sobreescribe
    "archivo2 = open('copia.txt', 'a')"
    'archivo2.write(archivo.read())'
    'archivo2.close()'


except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Se cerro el archivo')
