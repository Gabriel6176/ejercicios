from tkinter import *
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
from os import remove
from tkinter import messagebox


root=Tk()
root.title("Lector de TXT AGIP")

miFrame=Frame(root, width=500, height=500)

APP_PATH = os.getcwd()

def buscar():
    d1 = miTXT.get()
    try:
        archivo=open(APP_PATH+'\\'+d1+'.txt', 'r', encoding='utf8')
        
        
    except Exception as e:
        print(e)
    finally:    
        archivo.close()
        print('Procesando..')

def salir():
    root.destroy()

#TK-INTER

#boton buscar
Boton2=Button(root, text="Procesar", command=buscar)
Boton2.grid(row=6, column=2, sticky="nswe", padx="10", pady="10")

#boton salir
Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=6, column=3, sticky="nswe", padx="1", pady="10")

#cuadro de texto nombre archivo entrada
labelTXT=Label(root, text="Nombre archivo de entrada: ")
labelTXT.grid(row=3, column=1, sticky="w", padx="10", pady="10")

#extencion archvio de entrada
label_TXT=Label(root, text=".txt       ")
label_TXT.grid(row=3, column=3, sticky="w", padx="1", pady="1")

#caja donde escribo el nombre del archivo para importar
miCSV=StringVar()
cuadroNombreTXT=Entry(root, bg="light blue", textvariable=miTXT)
cuadroNombreTXT.grid(row=3, column=2, sticky="w", padx="1", pady="10")
cuadroNombreTXT.config(fg="blue", justify="left")
#si uso .place(x=100, y=100) es ancho por alto

#label version de programa
label_Ver=Label(root, text="v 1.1 ")
label_Ver.grid(row=9, column=4, sticky="w", padx="1", pady="1")

root.mainloop()



