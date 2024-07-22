import os
import sqlite3
import csv
import linecache
import re

#importo a la base sql de a una linea del txt

def importar():
    APP_PATH = os.getcwd()
    #corregir ard3
    filename = APP_PATH+'\\'+'ard'+'.txt'
    with open(APP_PATH+'\\'+'ard'+'.txt', 'rb') as f:
            x = len(f.readlines())
            print(f'Total lineas: {x}')
    linea=1
    while True:
        if linea<=x:
            #corregir ard
            line=linecache.getline(APP_PATH+'\\'+'ard'+'.txt', linea)
            cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
            text=re.search('(.*)', line).group(1)
            char_to_replace = {'!' : '!!',	
                   "'" : "''",
                   "#" : " "	
                   }
            # Iterate over all key-value pairs in dictionary
            for key, value in char_to_replace.items():
            # Replace key character with value character in string
                text=text.replace(key, value)
            #print(str(text))
            ##print(f'{text}')
            ##print(f'cuit: {cuit}')
            #corregir base
            con = sqlite3.connect(APP_PATH+'\\'+'base'+'.db')
            cursor=con.cursor()
            #si es texto el dato le pongo comillas por fuera de '{nombre}'
            try:
                #inserta o ignora si el valor es repetido
                #instruccion=f"INSERT or IGNORE INTO base VALUES(%d, '%s')" % (int(cuit), text)
                instruccion=f"INSERT or IGNORE INTO base VALUES({cuit}, '{text}');"
                cursor.execute(instruccion)
                con.commit()
                linea+=1
                #print(f'insertar {linea}')
            except Exception as e:
                print(f'Excepcion al insertar datos: {e}')
        else:
            con.close()
            print('fin')
            break
        

if __name__=='__main__':
    importar()

