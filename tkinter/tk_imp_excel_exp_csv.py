from tkinter import *
import tkinter as tk
from tkinter import filedialog
import sqlite3
import pandas as pd
import os
from os import remove
from tkinter import messagebox


root=Tk()
root.title("Importador de Excel a *.CSV AFIP F2668")

miFrame=Frame(root, width=500, height=500)

def procesar():
    d1 = miExcel.get()
    d2 = miCSV.get()
    #APP_PATH = os.getcwd()
    #DB_PATH = APP_PATH+'\\'+d2+'.db'
    #con = sqlite3.connect(APP_PATH+'\\'+d2+'.db')
    #wb = pd.read_excel(APP_PATH+'\\'+d1+'.xlsx',sheet_name = None)
    #for sheet in wb:
    #    wb[sheet].to_sql(sheet,con,index=False)
    APP_PATH = os.getcwd()
    #print(APP_PATH)
    DB_PATH = APP_PATH+'\\excel.db'
    con = sqlite3.connect('excel.db')
    wb = pd.read_excel(APP_PATH+'\\'+d1+'.xlsx',sheet_name = None)
    for sheet in wb:
        wb[sheet].to_sql(sheet,con,index=False)

    APP_PATH = os.getcwd()
    DB_PATH = APP_PATH+'\\excel.db'
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute('SELECT CAMPO1, CAMPO2, CAMPO3, CAMPO4, CAMPO5, CAMPO6, CAMPO7, CAMPO8, CAMPO9, CAMPO10 FROM Hoja1')

    contador=1
    for i in cursor:
        if contador<2:
            c1 = str(i[0])
            c2 = str(i[1])
            c3 = str(i[2])
            c4 = str(i[3])
            c5 = str(i[4])
            c6 = str(i[5])
            c7 = str(i[6])
            c8 = str(i[7])
            c9 = str(i[8])
            c10 =str(i[9])
            c11 = str(";")
            c12 = str('"')
            data_id=(c1+c11+c2+c11+c3+c11+c4+c11+c5+c11+c6+c11+c7+c11+c8+c11+c9+c11+c10)
            contador=contador+1
            try:
                archivo=open(APP_PATH+'\\'+d2+'.csv', 'a', encoding='utf8')
                archivo.write(data_id+"\n")
            except Exception as e:
                print(e)
            finally:    
                archivo.close()
                print('Procesando..')
                
                
        else:
            for i in cursor:
                c1 = str(i[0])
                c2 = str(i[1])
                c3 = str(i[2])
                c4 = str(i[3])
                c5 = str(i[4])
                c6 = str(i[5])
                c7 = str(i[6])
                c8 = str(i[7])
                c9 = str(i[8])
                c10 =str(i[9])
                c11 = str(";")
                c12 = str('"')
                data2_id=(c12+c1+c12+c11+c12+c2+c12+c11+c12+c3+c12+c11+c12+c4+c12+c11+c12+c5+c12+c11+c12+c6+c12+c11+c12+c7+c12+c11+c12+c8+c12+c11+c12+c9+c12+c11+c12+c10+c12)
                try:
                    archivo=open(APP_PATH+'\\'+d2+'.csv', 'a', encoding='utf8')
                    archivo.write(data2_id+"\n")
                except Exception as e:
                    print(e)
                finally:    
                    archivo.close()
                    print('Procesando...')
                    
    con.close()
    remove("excel.db")
    messagebox.showinfo(message="El proceso finalizo con exito", title="Mensaje")

def salir():
    root.destroy()

#Boton1=Button(root, text="Seleccionar Archivo Excel", command=abreFichero)
#Boton1.grid(row=2, column=1, sticky="w", padx="10", pady="10")

Boton2=Button(root, text="Procesar", command=procesar)
Boton2.grid(row=6, column=2, sticky="nswe", padx="10", pady="10")

Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=6, column=3, sticky="nswe", padx="1", pady="10")

labelExcel=Label(root, text="Nombre archivo de entrada: ")
labelExcel.grid(row=2, column=1, sticky="w", padx="10", pady="10")

labelExt=Label(root, text=".xlsx       ")
labelExt.grid(row=2, column=3, sticky="w", padx="1", pady="1")

miExcel=StringVar()
cuadroNombreExcel=Entry(root, bg="light blue", textvariable=miExcel)
cuadroNombreExcel.grid(row=2, column=2, sticky="w", padx="1", pady="10")
cuadroNombreExcel.config(fg="blue", justify="left")

labelCSV=Label(root, text="Nombre archivo de salida: ")
labelCSV.grid(row=3, column=1, sticky="w", padx="10", pady="10")

label_Ext_CSV=Label(root, text=".csv       ")
label_Ext_CSV.grid(row=3, column=3, sticky="w", padx="1", pady="1")

miCSV=StringVar()
cuadroNombreCSV=Entry(root, bg="light blue", textvariable=miCSV)
cuadroNombreCSV.grid(row=3, column=2, sticky="w", padx="1", pady="10")
cuadroNombreCSV.config(fg="blue", justify="left")
#si uso .place(x=100, y=100) es ancho por alto

label_Ver=Label(root, text="v 1.1 ")
label_Ver.grid(row=9, column=4, sticky="w", padx="1", pady="1")

root.mainloop()

