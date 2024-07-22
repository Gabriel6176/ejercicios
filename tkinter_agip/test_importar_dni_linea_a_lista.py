import os
import sqlite3
import csv
import linecache
import re

#importo a la base sql de a una linea del txt
#solo importo el dni y el numero de linea

def importar():
    APP_PATH = os.getcwd()
    #corregir ard3
    filename = APP_PATH+'\\'+'ard'+'.txt'
    with open(APP_PATH+'\\'+'ard'+'.txt', 'rb') as f:
            x = len(f.readlines())
            print(f'Total lineas: {x}')
    linea=1
    #gabriel={"cuit":[],}
    while True:
        if linea<=50001:
            #corregir ard
            line=linecache.getline(APP_PATH+'\\'+'ard'+'.txt', linea)
            cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
            text=linea
            con = sqlite3.connect(APP_PATH+'\\'+'base'+'.db')
            cursor=con.cursor()
            #si es texto el dato le pongo comillas por fuera de '{nombre}'
            if linea==10000:
                print('diez mil')
            elif linea==50000:
                print('cincuenta mil')
            else:
                pass
            try:
                #gabriel.append({cuit},{linea})
                linea+=1
                #print(f'insertar {linea}')
            except Exception as e:
                print(f'Excepcion al insertar datos: {e}')
        else:
            con.close()
            print('fin')
            print(gabriel)
            break
        

if __name__=='__main__':
    importar()

