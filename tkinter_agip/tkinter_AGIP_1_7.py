from ast import Break
import os
import os.path
from os import remove
from tkinter import *
import tkinter as tk
import pandas as pd
import re
from tkinter import messagebox
import csv
import linecache
import cchardet as chardet
from tkinter import ttk 
import sqlite3

root=Tk()
root.title("Lector de TXT AGIP v1.7")
#esta version lee el txt verifica si es UTF-8 sino convierte el txt dejandolo de igual nombre al original 
#crea una base de datos para optimizar la busqueda

#miFrame=Frame(root, width=500, height=500)

#Size of the window - min and max
root.maxsize(600, 450)
root.minsize(400, 250)

#Setting a fixed size of window on opening
root.geometry("500x300")

#Setting the background colour
root.configure(background="white")

APP_PATH = os.getcwd()

#------------------------------------------------------------------------

#lo que quiero hacer es generar un txt solo con CUIT y numero de linea
#despues cargarlo a una base de datos 
#luego consultar el CUIT y obtengo el numero de linea
#luego consulto al txt en la linea justa

APP_PATH=os.getcwd()

encode='latin-1'

def db_exists():
    cuit=miCUIT.get()
    df=miTXT.get()
    db_file=df+'.db'
    db_exists= os.path.exists(db_file)
    if db_exists:
        print('paso db_exist _va_ buscar cuit')
        buscar_cuit(df)
    else:
        print('paso db_exist _va_ convierte_a_utf_narrow')
        convierte_a_utf_narrow(df, cuit)

def convierte_a_utf_narrow(df, cuit):
    narrow_file=df+'_2.txt'
    nf_exists= os.path.exists(narrow_file)
    if nf_exists:
        os.remove(APP_PATH+'\\'+df+'_2.txt')
    else:
        try:
            file_name=df+'.txt'
            # open original file in read mode and dummy file in write mode
            with open(APP_PATH+'\\'+file_name, 'r', encoding=encode) as f, open(narrow_file, 'a', encoding='utf-8') as nf:
                lineas=1
                nf.write('CUIT;LINEA\n')
                print('inserto el cuit y linea')
                for line in f:
                    cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
                    nf.write(f'{cuit};{lineas}\n')
                    lineas+=1
            print('paso convierte_utf_narrow _va_ crear_base')
            #crear_base(df, cuit)
            importar_db(df, cuit)
        except:
            print('exception')
            with open(APP_PATH+'\\'+file_name, 'r', encoding=encode) as f, open(narrow_file, 'w', encoding='utf-8') as nf:
                for line in f:
                    cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
                    nf.write(f'{cuit};{lineas}\n')
                    lineas+=1
            print('excep-convierte_utf_narrow _va_ importar_base')
            #crear_base(df, cuit)
            importar_db(df,cuit)

def importar_db(df, cuit):
    #podes importar csv o txt
    table='base'
    APP_PATH = os.getcwd()
    con = sqlite3.connect(APP_PATH+'\\'+df+'.db')
    cursor=con.cursor()
    #si quiero leer desde registo 1M hasta 1,999M
    #read_csv(..., skiprows=1000000, nrows=999999)
    # load the data into a Pandas DataFrame
    #users = pd.read_csv(f"{df}_2.txt", sep=';', usecols=['CUIT', 'LINEA']) [['CUIT', 'LINEA']]
    users = pd.read_csv(f"{df}_2.txt", sep=';', usecols=['CUIT', 'LINEA']) [['CUIT', 'LINEA']]
    # write the data to a sqlite table
    #print(users)
    #users.to_sql(csv_name, con, if_exists='append', index = False)
    users.to_sql(table, con, if_exists='append', index=False)
    con.commit()
    cursor.close()
    os.remove((APP_PATH+'\\'+df+'_2.txt'))
    buscar_cuit(df)    

def buscar_cuit(df):
    try:
        cuit=miCUIT.get()
        con = sqlite3.connect(APP_PATH+'\\'+df+'.db')
        cursor=con.cursor()
        instruccion=f"SELECT LINEA FROM BASE WHERE (CUIT = {cuit});"
        cursor.execute(instruccion)
        linea=cursor.fetchall()
        con.commit()
        con.close()
        resultado=list(zip(*linea))
        res2=resultado[0]
        linea=res2[0]
        print(f"la linea es: {linea}")
        print_resultado(df,linea)
    except Exception as e:
        txt_row.delete(0.0, 'end')
        label_resultado.delete(0.0, 'end')    
        texto0='No encontrado'
        label_resultado.insert(0.0, texto0)
        #label_resultado.config(text=str('No Encontrado'))

def print_resultado(df,linea):
    #esto es para detener la barra de progreso
    #my_progress.stop()
    with open(APP_PATH+'\\'+df+'.txt',encoding='iso-8859-1') as f:
        l1 = f.readlines()
        linea=re.search('(.*)', l1[linea-1]).group()
    print(linea)
    txt_row.delete(0.0, 'end')
    label_resultado.delete(0.0, 'end')
    texto0='Encontrado'
    label_resultado.insert(0.0, texto0)
    #label_resultado.config(text=str('Encontrado'))
    txt_row.insert(0.0, linea)

def salir():
    root.destroy()


#TK-INTER--------------------------------------------------------------
#barra de progreso
#my_progress=ttk.Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
#my_progress.grid(row=6, column=2, sticky="we", padx="10", pady="10")

#label de texto nombre archivo entrada
labelTXT=Label(root, text="Nombre archivo donde buscar: ")
labelTXT.grid(row=2, column=1, sticky="w", padx="10", pady="10")

#caja donde escribo el nombre del archivo para importar
miTXT=StringVar()
cuadroNombreTXT=Entry(root, bg="light blue", textvariable=miTXT)
cuadroNombreTXT.grid(row=2, column=2, sticky="ew", padx="1", pady="10")
cuadroNombreTXT.config(fg="blue", justify="left")
#si uso .place(x=100, y=100) es ancho por alto

#label .txt
labelTXT=Label(root, text=".txt           ")
labelTXT.grid(row=2, column=3, sticky="w", padx="10", pady="10")

#-----------------------------------------------------------------

#cuadro de texto CUIT a ingresar
labelCUIT=Label(root, text="CUIT a consultar (sin guiones): ")
labelCUIT.grid(row=3, column=1, sticky="w", padx="10", pady="10")

#caja donde escribo el CUIT
miCUIT=IntVar()
cuadroCUIT=Entry(root, bg="light blue", textvariable=miCUIT)
cuadroCUIT.grid(row=3, column=2, sticky="ew", padx="1", pady="1")
cuadroCUIT.config(fg="blue", justify="left")

#label cuit incorrecto
#cuit_error=[]
#label_cuit_error=Label(root, bg="plum", text=cuit_error)
#label_cuit_error.grid(row=3, column=3, sticky="ew", padx="1", pady="1")

#-----------------------------------------------------------------

#label de texto resultado
labelResultado=Label(root, text="Resultado: ")
labelResultado.grid(row=4, column=1, sticky="w", padx="10", pady="10")


#label resultado
#resultado=[]
#label_resultado=Label(root, bg="plum", text=resultado)
#label_resultado.grid(row=4, column=2, sticky="w", padx="1", pady="1")

label_resultado=Text(root, bg="plum", width=25, height=1, wrap=WORD)
label_resultado.grid(row=4, column=2, sticky="w", padx="1", pady="1")
#-----------------------------------------------------------------
#label de texto resultado
labelInformacion=Label(root, text="Informacion: ")
labelInformacion.grid(row=5, column=1, sticky="w", padx="10", pady="10")

#label resultado
txt_row=Text(root, bg="plum", width=25, height=5, wrap=WORD)
txt_row.grid(row=5, column=2, sticky="w", padx="1", pady="1")
#row=[]
#label_row=Label(root, bg="plum", text=row)
#label_row.grid(row=5, column=2, sticky="w", padx="1", pady="1")

#----------------------------------------------------------------

#boton buscar
Boton2=Button(root, text="Buscar", command=db_exists)
Boton2.grid(row=6, column=3, sticky="nswe", padx="1", pady="10")

#boton salir
Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=7, column=3, sticky="nswe", padx="1", pady="10")


root.mainloop()




