from tkinter import *
import sqlite3
import pandas as pd
import os
from os import remove
from tkinter import messagebox
import csv
import re

root=Tk()
root.title("Importar archivos a db v1.1")
#Setting a fixed size of window on opening
root.geometry("500x400")
#max min windows
root.maxsize(600, 550)
root.minsize(400, 380)
#Setting the background colour
root.configure(background="white")


def test_cuit():
    d1 = miTXT.get()
    cuit = miCUIT.get()
    txt_row.delete(0.0, 'end')
    label_resultado.config(text=str(''))
    APP_PATH=os.getcwd()
    try:
        with open(APP_PATH+'\\'+d1+'.txt', 'rb') as f:
            x = len(f.readlines())
    except FileNotFoundError as e:
        messagebox.showwarning(title='Error', message=f'Archivo no Encontrado: {e}')
    if cuit>34999999999 or cuit<20000000001:
        messagebox.showerror(title='Error', message=f'Cuit Incorrecto!')
    else:
        buscar(cuit)

def procesar():
    d1=miTXT.get()
    #d2=miCSV.get()
    #d3='nombre'    
    d3=miDB.get()
    #d4=miExcel.get()
    #d5=miCUIT.get()
    APP_PATH=os.getcwd()
    con=sqlite3.connect(APP_PATH+'\\'+d3+'.db')
    cursor=con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS '''+d3+''' (
        FECHA1 INTEGER(8),
        FECHA2 INTEGER(8),
        FECHA3 INTEGER(8),
        CUIT INTEGER(11),
        D1 VARCHAR(2),
        D2 VARCHAR(2),
        D3 VARCHAR(2),
        D4 FLOAT,
        D5 FLOAT,
        D6 INTEGER,
        D7 INTEGER,
        NOMBRE VARCHAR(100)   
        )
        ''')
    con.commit()
    with open(APP_PATH+'\\'+d1+'.txt', 'r', encoding='ANSI', newline='\n') as f:
        txt_line=csv.reader(f, delimiter='\n')
        for row in txt_line:
            dt1=re.search('(\d\d\d\d\d\d\d\d)', row).group(1)
            cursor.execute('INSERT INTO '+d3+' (CUIT, LINEA) VALUES ('+str(dt1)+','+str(row)+')', row)
    con.commit()
    con.close()

def buscar(cuit):
    txt_row.delete(0.0, 'end')
    label_resultado.config(text=str(''))
    APP_PATH=os.getcwd()
    con=sqlite3.connect(APP_PATH+'\\base.db')
    cursor=con.cursor()
    cuit=miCUIT.get()
    print(cuit)
    cursor.execute('SELECT * FROM BASE WHERE CUIT = '+str(cuit)+'')
    texto=cursor.fetchone()
    if texto == None:
        print('1')
        txt_row.insert(0.0, 'No encontrado')
        label_resultado.config(text=str('No Encontrado'))
    else:    
        txt_row.insert(0.0, texto)
        label_resultado.config(text=str('Encontrado'))
    con.commit()
    con.close()


def salir():
    root.destroy()


#if __name__=='__main__'():





#TK-INTER--------------------------------------------------------------

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
#label de texto nombre archivo entrada
labelDB=Label(root, text="Nombre archivo base de datos: ")
labelDB.grid(row=3, column=1, sticky="w", padx="10", pady="10")

#caja donde escribo el nombre de la base de datos
miDB=StringVar()
cuadroNombreDB=Entry(root, bg="light blue", textvariable=miDB)
cuadroNombreDB.grid(row=3, column=2, sticky="ew", padx="1", pady="10")
cuadroNombreDB.config(fg="blue", justify="left")
#si uso .place(x=100, y=100) es ancho por alto

#label .db
labelDB=Label(root, text=".db           ")
labelDB.grid(row=3, column=3, sticky="w", padx="10", pady="10")

#-----------------------------------------------------------------
#cuadro de texto CUIT a ingresar
labelCUIT=Label(root, text="CUIT a consultar (sin guiones): ")
labelCUIT.grid(row=4, column=1, sticky="w", padx="10", pady="10")

#caja donde escribo el CUIT
miCUIT=IntVar()
cuadroCUIT=Entry(root, bg="light blue", textvariable=miCUIT)
cuadroCUIT.grid(row=4, column=2, sticky="ew", padx="1", pady="1")
cuadroCUIT.config(fg="blue", justify="left")

#-----------------------------------------------------------------

#label de texto resultado
labelResultado=Label(root, text="Resultado: ")
labelResultado.grid(row=5, column=1, sticky="w", padx="10", pady="10")


#label resultado
resultado=[]
label_resultado=Label(root, bg="plum", text=resultado)
label_resultado.grid(row=5, column=2, sticky="w", padx="1", pady="1")

#-----------------------------------------------------------------
#label de texto resultado
labelInformacion=Label(root, text="Informacion: ")
labelInformacion.grid(row=6, column=1, sticky="w", padx="10", pady="10")

#label resultado
txt_row=Text(root, bg="plum", width=25, height=5, wrap=WORD)
txt_row.grid(row=6, column=2, sticky="w", padx="1", pady="1")
#row=[]
#label_row=Label(root, bg="plum", text=row)
#label_row.grid(row=5, column=2, sticky="w", padx="1", pady="1")

#----------------------------------------------------------------

#boton importar
Boton1=Button(root, text="Importar", command=procesar)
Boton1.grid(row=7, column=3, sticky="nswe", padx="1", pady="10")

#boton buscar
Boton2=Button(root, text="Buscar", command=test_cuit)
Boton2.grid(row=8, column=3, sticky="nswe", padx="1", pady="10")

#boton salir
Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=9, column=3, sticky="nswe", padx="1", pady="10")


root.mainloop()




