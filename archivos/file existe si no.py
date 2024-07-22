import os.path
import os

archivo='archivo.json'
APP_PATH=os.getcwd()
FILE_PATH=APP_PATH+'\\'+archivo

resultado=os.path.exists(FILE_PATH)

#resultado=os.path.exists('c:\\Users\\PC\\Python\\Ejercicios\\archivos\\archivo.json')
print(resultado)
if resultado == True: 
    print('1')
else:
    print('2')

