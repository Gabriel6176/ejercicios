from tkinter import *
import tkinter as tk
from tkinter import filedialog
import sqlite3
import pandas as pd
import os


root=Tk()
root.title("Importador de Excel a F2668")

miFrame=Frame(root, width=500, height=500)
#miFrame.pack()


#def abreFichero():
#    global fichero
#    fichero = filedialog.askopenfilename(title="Seleccionar Excel a Importar", initialdir="C:/", filetypes=(("Todos los archivos excel", "*.xlsx"),("Todos los archivos", "*.*")))
    
def procesar():
    d1 = miExcel.get()
    d2 = miDB.get()
    APP_PATH = os.getcwd()
    DB_PATH = APP_PATH+'\\'+d2+'.db'
    con = sqlite3.connect(APP_PATH+'\\'+d2+'.db')
    wb = pd.read_excel(APP_PATH+'\\'+d1+'.xlsx',sheet_name = None)
    for sheet in wb:
        wb[sheet].to_sql(sheet,con,index=False)

def salir():
    root.destroy()

#Boton1=Button(root, text="Seleccionar Archivo Excel", command=abreFichero)
#Boton1.grid(row=2, column=1, sticky="w", padx="10", pady="10")

Boton2=Button(root, text="Procesar", command=procesar)
Boton2.grid(row=6, column=1, sticky="nswe", padx="10", pady="10")

Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=7, column=2, sticky="nswe", padx="10", pady="10")

labelExcel=Label(root, text="Nombre archivo de entrada .xlsx:")
labelExcel.grid(row=2, column=1, sticky="w", padx="10", pady="10")

miExcel=StringVar()
cuadroNombreExcel=Entry(root, bg="light blue", textvariable=miExcel)
cuadroNombreExcel.grid(row=2, column=2, sticky="w", padx="10", pady="10")
cuadroNombreExcel.config(fg="blue", justify="left")

labelDB=Label(root, text="Nombre archivo de salida .csv:")
labelDB.grid(row=3, column=1, sticky="w", padx="10", pady="10")

miDB=StringVar()
cuadroNombreDB=Entry(root, bg="light blue", textvariable=miDB)
cuadroNombreDB.grid(row=3, column=2, sticky="w", padx="10", pady="10")
cuadroNombreDB.config(fg="blue", justify="left")
#si uso .place(x=100, y=100) es ancho por alto

root.mainloop()

