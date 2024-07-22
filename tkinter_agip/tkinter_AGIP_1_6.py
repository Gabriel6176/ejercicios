import os
from tkinter import *
import tkinter as tk
import pandas as pd
import os
import re
from os import remove
from tkinter import messagebox
import csv
import linecache
import cchardet as chardet
from tkinter import ttk 
import time
import sqlite3

root=Tk()
root.title("Lector de TXT AGIP v1.6")
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
encode='latin-1'

def detectar_si_utf():
    #esto es para que borre el exto de la caja de resultados
    txt_row.delete(0.0, 'end')
    df = miTXT.get()
    file_name=df+'.txt'
    with open(file_name, 'rb') as f:
        msg=f.read()
        detection=chardet.detect(msg)
        f.close()
        with open('procesado.txt', 'w') as r:
            r.write(str(detection))
            r.close()
        with open('procesado.txt', 'rb') as r:    
            line=linecache.getline(APP_PATH+'\\procesado.txt', 1)
            texto=re.search("ng': '(.+?)', 'con", line).group(1)
            r.close()
            if texto != 'UTF-8':
                #deberia convertir txt a UTF-8
                convierte_a_utf(file_name)
                os.remove(APP_PATH+'\\procesado.txt')
                print('1')
            else:
                #deberia ir a la consulta sin convertir la base
                os.remove(APP_PATH+'\\procesado.txt')
                test_cuit()
                print('0')

#-----------------------------------------------------------------------

def convierte_a_utf(file_name):
    try:
        print('try')
        dummy_file = file_name + '.bak'
        # open original file in read mode and dummy file in write mode
        with open(APP_PATH+'\\'+file_name, 'r', encoding=encode) as read_origin_file, open(dummy_file, 'w', encoding='utf-8') as write_obj:
            for line in read_origin_file:
                write_obj.write(line)
        # remove original file
        os.remove(file_name)
        # Rename dummy file as the original file
        os.rename(dummy_file, file_name)
        #antes guardaba en un txt un 1 si era utf
        #with open(APP_PATH+'\\procesado.txt', 'a') as f:
        #    f.write(str(1)+'\n')
        test_cuit()
    except:
        print('except')
        df = miTXT.get()
        file_name=df+'.txt'
        dummy_file = file_name + '.bak'
        # open original file in read mode and dummy file in write mode
        with open(APP_PATH+'\\'+file_name, 'r', encoding=encode) as read_origin_file, open(dummy_file, 'w', encoding='utf-8') as write_obj:
            for line in read_origin_file:
                write_obj.write(line)
        # remove original file
        os.remove(file_name)
        # Rename dummy file as the original file
        os.rename(dummy_file, file_name)
        #antes escribia un archivo si era utf
        #with open(APP_PATH+'\\procesado.txt', 'a') as f:
        #    f.write(str(1)+'\n')
        test_cuit()


#--------------------------------------------------------------------

linea=1

def test_cuit():
    #label_resultado.config(text=str('Procesando'))
    d1 = miTXT.get()
    cuit = miCUIT.get()
    #label_cuit_error.config(text=str(''))
    txt_row.delete(0.0, 'end')
    #label_resultado.config(text=str(''))
    try:
        with open(APP_PATH+'\\'+d1+'.txt', 'rb') as f:
            x = len(f.readlines())
            print(f'Total lineas: {x}')
    except FileNotFoundError as e:
        messagebox.showwarning(title='Error', message=f'Archivo no Encontrado: {e}')
    if cuit>34999999999 or cuit<20000000001:
        messagebox.showerror(title='Error', message=f'Cuit Incorrecto!')
    else:
        #buscar(cuit)
        pass

def confirm_db_exist():
    d1 = miTXT.get()
    archivo=d1+'.db'
    APP_PATH=os.getcwd()
    FILE_PATH=APP_PATH+'\\'+archivo

    resultado=os.path.exists(FILE_PATH)
    print(resultado)
    if resultado == True: 
        cuit=miCUIT.get()
        buscar(cuit)
    else:
        crear_base()
        print('2')

def crear_base():
    APP_PATH = os.getcwd()
    #le pone el mismo nombre a la base que al txt
    DB_PATH = APP_PATH+'\\'+miTXT.get()+'.db'
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS BASE
        (CUIT INT, 
        LINEA NVARCHAR(200)
        )''')
    con.commit()
    cursor.execute('''CREATE UNIQUE INDEX IF NOT EXISTS cuit_index on base (CUIT)''')
    importar(con, cursor)

def importar(con, cursor):
    APP_PATH = os.getcwd()
    d1=miTXT.get()
    filename = APP_PATH+'\\'+d1+'.txt'
    with open(APP_PATH+'\\'+d1+'.txt', 'rb') as f:
            x = len(f.readlines())
            print(f'Total lineas: {x}')
    linea=1
    while True:
        if linea<=x:
            line=linecache.getline(APP_PATH+'\\'+d1+'.txt', linea)
            cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
            #text=re.search('(.*)', line).group(1)
            char_to_replace = {'!' : '!!',	
                   "'" : "''",
                   "#" : " "	
                   }
            # Iterate over all key-value pairs in dictionary
            for key, value in char_to_replace.items():
            # Replace key character with value character in string
                text=text.replace(key, value)
            print(f'texto: {text}')
            print(f'cuit: {cuit}')
            con = sqlite3.connect(APP_PATH+'\\'+d1+'.db')
            cursor=con.cursor()
            #si es texto el dato le pongo comillas por fuera de '{nombre}'
            instruccion=f"INSERT INTO base VALUES({cuit},'{str(text)}');"
            cursor.execute(instruccion)
            con.commit()
            linea+=1
            print(f'insertar {linea}')
        else:
            print('fin')
            cuit=miCUIT.get()
            buscar(cuit)    

def buscar(cuit):
    d1=miTXT.get()
    d2=d1+'.db'
    con = sqlite3.connect(APP_PATH+'\\'+d2)
    cursor=con.cursor()
    instruccion=f"SELECT LINEA FROM '{d2}' WHERE (CUIT = {cuit});"
    cursor.execute(instruccion)
    respuesta=cursor.fetchall()
    con.commit()
    con.close()
    print(respuesta)
    print_resultado(linea, cuit)

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
Boton2=Button(root, text="Buscar", command=detectar_si_utf)
Boton2.grid(row=6, column=3, sticky="nswe", padx="1", pady="10")

#boton salir
Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=7, column=3, sticky="nswe", padx="1", pady="10")


root.mainloop()




