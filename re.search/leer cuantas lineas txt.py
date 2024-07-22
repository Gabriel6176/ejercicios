import os
import re
import linecache

APP_PATH = os.getcwd()

#indico que lo lea en modo binario 'rb' sino puedo tener errores
#esto me cuenta cuantas lineas tiene
#si abro en binario no tengo que ponerle el encoding , encoding='latin-1'
with open(APP_PATH+'\\ARD3.txt', 'rb') as f:
    x = len(f.readlines())
    print(f'Total lineas: {x}')


#--------------------------------------
#informa un rango de lineas -no me funciono muy bien
with open(APP_PATH+'\\ARD3.txt', 'rb') as f:
    x = len(f.readlines())
    linea_leer = [3, 4]
    lineas=[]
    for i, line in enumerate(f):
        if i in linea_leer:
            lineas.append(line.strip())
        elif i > 5:
            break     
print(lineas)

#---------------------------------------------
#proceso lento itera de a una linea
cuit=30710468520
cuit2=20001148304
#intento leer una linea
with open(APP_PATH+'\\ARD3.txt', 'r') as f:
    count=0
    for line in f:
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit2)
        print(f'Resultado: {resultado} linea {count}')
        if resultado == 0:
            #print(f'encontrado linea: {count}')
            line=linecache.getline(APP_PATH+'\\ARD3.txt', count)
            print(line)
            break
        else:
            count+=1
            #print('no encontrado')

            
