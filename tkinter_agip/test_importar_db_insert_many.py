import os
import sqlite3
import csv
import linecache
import re

#deberia crear una lista con las lineas del TXT
LISTA=['lineas del txt']


def importar(LISTA):
    APP_PATH = os.getcwd()
    #corregir ard3
    filename = APP_PATH+'\\'+'ard3'+'.txt'
    with open(APP_PATH+'\\'+'ard3'+'.txt', 'rb') as f:
            x = len(f.readlines())
            print(f'Total lineas: {x}')
    linea=1
    while True:
        if linea<x:
            #corregir ard
            line=linecache.getline(APP_PATH+'\\'+'ard3'+'.txt', linea)
            cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
            text=re.search('(.*)', line).group(1)
            print(f'{text}')
            print(f'cuit: {cuit}')
            #corregir base
            con = sqlite3.connect(APP_PATH+'\\'+'base'+'.db')
            cursor=con.cursor()
            #si es texto el dato le pongo comillas por fuera de '{nombre}'
            instruccion=f"INSERT INTO base VALUES(?,?);"
            cursor.executemany(instruccion, LISTA)
            con.commit()
            linea+=1
            print(f'insertar {linea}')
        else:
            con.close()
            print('fin')
            break
        

if __name__=='__main__':
    importar(LISTA)

