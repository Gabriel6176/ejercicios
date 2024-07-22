import linecache
import re
import pandas as pd
import os
import sqlite3

APP_PATH=os.getcwd()
encode='latin-1'


def buscar_cuit(df, cuit):
    try:
        con = sqlite3.connect(APP_PATH+'\\'+df+'.db')
        cursor=con.cursor()
        instruccion=f"SELECT LINEA FROM BASE WHERE (CUIT = {cuit});"
        cursor.execute(instruccion)
        linea=cursor.fetchall()
        con.commit()
        con.close()
        resultado=list(zip(*linea))
        res=resultado[0]
        linea=res[0]
        print(linea)
        texto=linecache.getline(APP_PATH+'\\'+df+'.txt', linea)
        print(texto)
        #print_resultado(linea, cuit)
    except Exception as e:
        print('no encontrado')

if __name__=='__main__':
    buscar_cuit('ard', 20256755034)