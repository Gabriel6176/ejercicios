import os
import os.path
import linecache
import cchardet as chardet
import re
import sqlite3

#lo que quiero hacer es generar un txt solo con CUIT y numero de linea
#despues cargarlo a una base de datos 
#luego consultar el DNI y obtengo el numero de linea
#luego consulto al txt en la linea justa

APP_PATH=os.getcwd()

encode='latin-1'
#df='ard'
#file_name=df+'.txt'
#testeo si existe la base.db con el numero de cuit y linea


def db_exists(df, cuit):
    db_file=df+'.db'
    db_exists= os.path.exists(db_file)
    if db_exists:
        print('paso db_exist _va_ buscar cuit')
        buscar_cuit(df, cuit)
    else:
        print('paso db_exist _va_ convierte_a_utf_narrow')
        convierte_a_utf_narrow(df, cuit)

def convierte_a_utf_narrow(df, cuit):
    try:
        print('try')
        narrow_file = df + '_2.txt'
        file_name=df+'.txt'
        # open original file in read mode and dummy file in write mode
        with open(APP_PATH+'\\'+file_name, 'r', encoding=encode) as f, open(narrow_file, 'w', encoding='utf-8') as nf:
            linea=1
            for line in f:
                cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
                nf.write(f'{cuit};{linea}\n')
                linea+=1
        print('paso convierte_utf_narrow _va_ crear_base')
        crear_base(df, cuit)
    except:
        print('except')
        with open(APP_PATH+'\\'+file_name, 'r', encoding=encode) as f, open(narrow_file, 'w', encoding='utf-8') as nf:
            for line in f:
                cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
                nf.write(f'{cuit};{linea}\n')
                linea+=1
        print('paso convierte_utf_narrow x except _va_ crear_base')
        crear_base(df, cuit)

def crear_base(df, cuit):
    APP_PATH = os.getcwd()
    #le pone el mismo nombre a la base que al txt
    DB_PATH = APP_PATH+'\\'+df+'.db'
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS BASE (CUIT INT, LINEA INT)''')
    #con.commit()
    cursor.execute('''CREATE UNIQUE INDEX IF NOT EXISTS cuit_index on base (CUIT)''')
    print(' paso por crear_base _va_ importar')
    importar(df, cuit, con, cursor)

def importar(df, cuit, con, cursor):
    APP_PATH = os.getcwd()
    filename = APP_PATH+'\\'+df+'_2.txt'
    with open(filename, 'rb') as f:
            x = len(f.readlines())
            print(f'Total lineas: {x}')
    linea=1
    while True:
        if linea<=x:
            line=linecache.getline(filename, linea)
            cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
            num_linea=re.search(';(.*)', line).group(1)
            con = sqlite3.connect(APP_PATH+'\\'+df+'.db')
            cursor=con.cursor()
            #si es texto el dato le pongo comillas por fuera de '{nombre}'
            instruccion=f"INSERT INTO base VALUES({cuit},'{num_linea}');"
            cursor.execute(instruccion)
            con.commit()
            linea+=1
        else:
            print(' paso importar _va_ buscar cuit')
            return buscar_cuit(df, cuit)    

def buscar_cuit(df, cuit):
    con = sqlite3.connect(APP_PATH+'\\'+df+'.db')
    cursor=con.cursor()
    instruccion=f"SELECT * FROM BASE WHERE (CUIT = {cuit});"
    cursor.execute(instruccion)
    linea=cursor.fetchall()
    con.commit()
    con.close()
    print(*linea)
    

    #print_resultado(linea, cuit)
'''
def print_resultado(linea, cuit):
    #esto es para detener la barra de progreso
    #my_progress.stop()
    txt_row.delete(0.0, 'end')
    label_resultado.delete(0.0, 'end')
    print(f'La linea es: {linea} el cuit es: {cuit}') 
    if linea>0:
        texto0='Encontrado'
        label_resultado.insert(0.0, texto0)
        #label_resultado.config(text=str('Encontrado'))
    else:
        texto0='No encontrado'
        label_resultado.insert(0.0, texto0)
        #label_resultado.config(text=str('No Encontrado'))
    txt_row.insert(0.0, linea)
'''
if __name__=='__main__':
    db_exists('ard1', 20000182274)
    