import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import sqlite3
import pandas as pd
import os
from os import remove
from tkinter import messagebox
import re
import csv

root=Tk()
root.title("Lector de TXT AGIP v1.2")

#miFrame=Frame(root, width=500, height=500)

#Size of the window - min and max
root.maxsize(600, 350)
root.minsize(400, 210)

#Setting a fixed size of window on opening
root.geometry("500x250")

#Setting the background colour
root.configure(background="white")

APP_PATH = os.getcwd()

def crear_base(con, cursor):
    APP_PATH = os.getcwd()
    DB_PATH = APP_PATH+'\\base.db'
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS BASE
        (Creacion INT, 
        Desde INT, 
        Hasta INT, 
        Cuit INT, 
        _1 VARCHAR(5), 
        _2 VARCHAR(5), 
        _3 VARCHAR(5), 
        _4 VARCHAR(5), 
        _5 VARCHAR(5), 
        _6 VARCHAR(5), 
        _7 VARCHAR(5), 
        Nombre VARCHAR(100)
        )''')
    con.commit()

    cursor.execute('''CREATE UNIQUE INDEX IF NOT EXISTS cuit_index on base (Cuit)''')

def importar(con, cursor, filename):
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        next(csv.reader(f), None)

        for entry in reader:
            try:
                print(reader.line_num)
                record = (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10], entry[11])
                #crear un sql insert statement witn placeholders
                stmt = "INSERT INTO base(Creacion, Desde, Hasta, Cuit, _1, _2, _3, _4, _5, _6, _7, Nombre) values(?,?,?,?,?,?,?,?,?,?,?,?);" 
                #stmt += " values(?,?,?,?,?,?,?,?,?,?,?,?);"
                
                APP_PATH = os.getcwd()
                DB_PATH = APP_PATH+'\\base.db'
                con = sqlite3.connect(DB_PATH)
                cursor = con.cursor()
                #ejecutar statement with tuple data
                cursor.execute(stmt,record)
                print('paso por aca')
                if cursor.lastrowid % 100 == 0:
                    con.commit()

            except csv.Error as e:
                print(f'Line:{reader.line_num}, Record:{record}')

def buscar():
    d1 = miTXT.get()
    #d1='dni'
    d2 = miCUIT.get()
    #d2='20000691810'
    resultado=[]
    no_encontrado=[]
    cuit_error=[]
    if d2>35000000000 or d2<20000000001:
        cuit_error.append('Cuit incorrecto') 
        print('Error')
    else:
        cuit_error.append('OK')
        print('OK')
        try:
            APP_PATH = os.getcwd()
            DB_PATH = APP_PATH+'\\base.db'
            con = sqlite3.connect(DB_PATH)
            cursor = con.cursor()
            cursor.execute("SELECT Creacion, Desde, Hasta, Cuit, _1, _2, _3, _4, _5, _6, _7, Nombre FROM Base WHERE Cuit=20000691810") 
        except Exception as e:
            print(e)

    label_cuit_error.config(text=str(cuit_error[0]))    
    #label_resultado.config(text=str(resultado[0]))
    #label_no_encontrado.config(text=str(no_encontrado[0]))
   
def salir():
    root.destroy()


if __name__ == "__main__":
    con = sqlite3.connect('base.db')
    cursor=con.cursor()
    crear_base(con, cursor)
    importar(con, cursor, (APP_PATH+'\\ard2.csv'))
    con.commit()
    con.close()
    print('job completed')


#TK-INTER--------------------------------------------------------------

#label de texto nombre archivo entrada
labelTXT=Label(root, text="Nombre archivo donde buscar: ")
labelTXT.grid(row=2, column=1, sticky="w", padx="10", pady="10")

#caja donde escribo el nombre del archivo para importar
miTXT=StringVar()
cuadroNombreTXT=Entry(root, bg="light blue", textvariable=miTXT)
cuadroNombreTXT.grid(row=2, column=2, sticky="w", padx="1", pady="10")
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
cuadroCUIT.grid(row=3, column=2, sticky="w", padx="1", pady="10")
cuadroCUIT.config(fg="blue", justify="left")

#label cuit incorrecto
cuit_error=[]
label_cuit_error=Label(root, bg="plum", text=cuit_error)
label_cuit_error.grid(row=3, column=3, sticky="w", padx="1", pady="1")

#-----------------------------------------------------------------

#label de texto resultado
labelResultado=Label(root, text="Resultado: ")
labelResultado.grid(row=4, column=1, sticky="w", padx="10", pady="10")


#label resultado
resultado=[]
label_resultado=Label(root, bg="plum", text=resultado)
label_resultado.grid(row=4, column=2, sticky="w", padx="1", pady="1")

#-----------------------------------------------------------------
#label de texto resultado
labelInformacion=Label(root, text="Informacion: ")
labelInformacion.grid(row=5, column=1, sticky="w", padx="10", pady="10")

#label no encontrado
no_encontrado=[]
label_no_encontrado=Label(root, bg="plum", text=no_encontrado)
label_no_encontrado.grid(row=5, column=2, sticky="w", padx="1", pady="1")

#----------------------------------------------------------------

#boton buscar
Boton2=Button(root, text="Buscar", command=buscar)
Boton2.grid(row=6, column=2, sticky="nswe", padx="10", pady="10")

#boton salir
Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=6, column=3, sticky="nswe", padx="1", pady="10")


root.mainloop()




