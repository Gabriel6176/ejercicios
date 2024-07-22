import os
import re
import pandas as pd

APP_PATH = os.getcwd()

#d1 = miTXT.get()
d1='dni'
#d2 = miCUIT.get()
d2='30000004'

try:
    archivo=open(APP_PATH+'\\'+d1+'.txt', 'r+', encoding='utf8')
    archivo2=archivo.readlines()
    for i in archivo2:
        linea=1
        valor = re.search('(\d\d\d\d\d\d\d\d)', i).group(1)
        if valor == d2:
            print(i)
            linea+=1
        else:
            print('buscando')
            linea+=1    
    else:
        print('else')
except Exception as e:
    print(e)