
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos algo al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Se cerro el archivo')
