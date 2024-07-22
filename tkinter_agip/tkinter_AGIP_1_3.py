#encoding: ansi
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

root=Tk()
root.title("Lector de TXT AGIP v1.3")

#miFrame=Frame(root, width=500, height=500)

#Size of the window - min and max
root.maxsize(600, 450)
root.minsize(400, 250)

#Setting a fixed size of window on opening
root.geometry("500x300")

#Setting the background colour
root.configure(background="white")

APP_PATH = os.getcwd()

#cuit2=20002545080
#cuit2=20000188299
#cuit2=20041522098
#cuit2=20273742558
#cuit2=20929969422
#cuit2=27115290016
#cuit2=27209836292
#cuit2=27602708123
#cuit2=30711231621
#cuit2=30716597802
#cuit2=34686233482
#cuit2=34688333360
#cuit2=34999032089

#no esta en la lista
#cuit2=34999032088
#cuit2=20273742559
#cuit2=27115290017
#cuit2=34686233483
#cuit2=34999032090



linea=0

def print_resultado(linea, cuit, value, count, d1):
    txt_row.delete(0.0, 'end')
    print(f'La linea es: {linea} el cuit es: {cuit} el value es: {value} el contador es: {count}') 
    if linea>0:
        label_resultado.config(text=str('Encontrado'))
    else:
        label_resultado.config(text=str('No Encontrado'))
    texto = pd.read_csv(APP_PATH+'\\'+d1+'.txt', index_col=linea, encoding='latin-1')
    print(texto)
    txt_row.insert(0.0, texto)
    

def test_cuit():
    d1 = miTXT.get()
    cuit = miCUIT.get()
    value=True
    #label_cuit_error.config(text=str(''))
    txt_row.delete(0.0, 'end')
    label_resultado.config(text=str(''))
    try:
        with open(APP_PATH+'\\'+d1+'.txt', 'rb') as f:
            x = len(f.readlines())
            print(f'Total lineas: {x}')
    except FileNotFoundError as e:
        messagebox.showwarning(title='Error', message=f'Archivo no Encontrado: {e}')
    if cuit>34999999999 or cuit<20000000001:
        messagebox.showerror(title='Error', message=f'Cuit Incorrecto!')
        #label_cuit_error.config(text=str('Cuit Incorrecto'))
        #print('cuit incorrecto')
    else:
        buscar(linea, value, cuit, d1, x)
    
def buscar(linea, value, cuit, d1, x):
    if cuit>34000000000:
        busqueda1(linea, value, cuit, d1, x)
    else:
        busqueda2(linea, value, cuit, d1, x)

def busqueda1(linea, value, cuit, d1, x):
    count=1
    value=value
    d1=d1
    while True:
        try:
            with open(APP_PATH+'\\'+d1+'.txt',encoding='iso-8859-1') as f:
                l1 = f.readlines()
                texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', l1[linea]).group()
        except FileNotFoundError as e:
            messagebox.showwarning(title="Error", message=f'Archivo No Encontrado: {e}')
        #line=linecache.getline(APP_PATH+'\\'+d1+'.txt', linea)
        #texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit)
        print(f'0 {resultado}')
        if count<10000:
            if resultado == 0:
                print(f'es la linea: {linea}')
                print('encontrado')
                print_resultado(linea, cuit, value, count, d1)
                break
            elif resultado<-13000000000:
                print(f'1 {resultado}')
                if linea+449 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+449   
                    print(f'ok b1-line: {linea}')
            elif resultado<-1300000000:
                print(f'2 {resultado}')
                if linea+129 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+129   
                    print(f'ok b1-line: {linea}')
            elif resultado<-130000000:
                print(f'3 {resultado}')
                if linea+99 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+99   
                    print(f'ok b1-line: {linea}')
            elif resultado<-13000000:
                print(f'4 {resultado}')
                if linea+17 > x:
                    linea=x-linea+linea
                    print(f'{linea}')
                else:
                    linea=linea+17   
                    print(f'ok b1-line: {linea}')
            elif resultado<-1300000:
                print(f'5 {resultado}')
                if linea+7 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+7   
                    print(f'ok b1-line: {linea}')
            elif resultado<-130000:
                print(f'6 {resultado}')
                if linea+3 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+3   
                    print(f'ok b1-line: {linea}')
            elif resultado<-13000:
                print(f'7 {resultado}')
                if linea+3 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+3   
                    print(f'ok b1-line: {linea}')
            elif resultado<-1300:
                print(f'8 {resultado}')
                if linea+1 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+1   
                    print(f'ok b1-line: {linea}')
            elif resultado<-130:
                print(f'9 {resultado}')
                if linea+1 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+1   
                    print(f'ok b1-line: {linea}')
            elif resultado<-13:
                print(f'10 {resultado}')
                if linea+1 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+1   
                    print(f'ok b1-line: {linea}')
            elif resultado<13:
                print(f'11 {resultado}')
                if (linea-1) <= 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print(f'ok b1-line: {linea}')
                    count+=1
            elif resultado<130:
                print(f'12 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print(f'ok b1-line: {linea}')
                    count+=1
            elif resultado<1300:
                print(f'13 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print(f'ok b1-line: {linea}')
                    count+=1
            elif resultado<13000:
                print(f'14 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print(f'ok b1-line: {linea}')
                    count+=1
            elif resultado<130000:
                print(f'15 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1  
                    print(f'ok b1-line: {linea}')
                    count+=1
            elif resultado<1300000:
                print(f'16 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print(f'ok b1-line: {linea}')
                    count+=1
            elif resultado<13000000:
                print(f'17 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1
                    print(f'ok b1-line: {linea}')
                    count+=1
            elif resultado<130000000:
                print(f'18 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print(f'ok b1-line: {linea}')
                    count+=1
            elif resultado<1300000000:
                print(f'19 {resultado}')
                if linea-1 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print(f'ok b1-line: {linea}')
                    count+=1
        else:
            value=False
            print('No encontrado')
            linea=0
            print_resultado(linea, cuit, value, count, d1)
            break

def busqueda2(linea, value, cuit, d1, x):
    count=1
    value=True
    count=1
    while True:
        try:
            with open(APP_PATH+'\\'+d1+'.txt',encoding='iso-8859-1') as f:
                print('Hola')
                l1 = f.readlines()
                texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', l1[linea]).group()
        except FileNotFoundError as e:
            messagebox.showwarning(title="Error", message=f'Archivo No Encontrado: {e}')
        #line=linecache.getline(APP_PATH+'\\'+d1+'.txt', linea)
        #texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
        resultado=int(texto)-int(cuit)
        print(f'0 {resultado}')
        if count<10000:
            if resultado == 0:
                print(f'es la linea: {linea}')
                print('encontrado')
                print_resultado(linea, cuit, value, count, d1)
                break
            elif resultado<-13000000000:
                print(f'1 {resultado}')
                if linea+99999 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+99999   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-1300000000:
                print(f'2 {resultado}')
                if linea+25089 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+25089   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-130000000:
                print(f'3 {resultado}')
                if linea+15049 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+15049   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-13000000:
                print(f'4 {resultado}')
                if linea+10029 > x:
                    linea=x-linea+linea
                    print(f'{linea}')
                else:
                    linea=linea+10029   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-1300000:
                print(f'5 {resultado}')
                if linea+4555 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+4555   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-530000:
                print(f'6 {resultado}')
                if linea+755 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+755   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-130000:
                print(f'7 {resultado}')
                if linea+555 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+255   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-53000:
                print(f'8 {resultado}')
                if linea+55 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+55   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-13000:
                print(f'9 {resultado}')
                if linea+9 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+9   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-1300:
                print(f'10 {resultado}')
                if linea+5 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+5   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-130:
                print(f'11 {resultado}')
                if linea+3 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+3   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<-13:
                print(f'12 {resultado}')
                if linea+1 > x:
                    linea=x-linea+linea
                    print('eror')
                else:
                    linea=linea+1   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<13:
                print(f'13 {resultado}')
                if linea-1 <= 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<130:
                print(f'14 {resultado}')
                if linea-2 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-2   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<1300:
                print(f'15 {resultado}')
                if linea-2 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-2   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<13000:
                print(f'16 {resultado}')
                if linea-4 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-4   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<130000:
                print(f'17 {resultado}')
                if linea-16 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-16  
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<1300000:
                print(f'18 {resultado}')
                if linea-52 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-52   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<13000000:
                print(f'19 {resultado}')
                if linea-480 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-480
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<130000000:
                print(f'20 {resultado}')
                if linea-1056 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-1056   
                    print(f'ok b2-line: {linea}')
                    count+=1
            elif resultado<1300000000:
                print(f'21 {resultado}')
                if linea-5046 < 1:
                    linea=1
                    print('eror')
                else:
                    linea=linea-5046   
                    print(f'ok b2-line: {linea}')
                    count+=1
        else:
            value=False
            print('no encontrado')
            linea=0
            print_resultado(linea, cuit, value, count, d1)
            break

   
def salir():
    root.destroy()


#TK-INTER--------------------------------------------------------------

#messagebox.showwarning(title='Error', message='Archivo no Encontrado')

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

#label cuit incorrecto - no usada
#cuit_error=[]
#label_cuit_error=Label(root, bg="plum", text=cuit_error)
#label_cuit_error.grid(row=3, column=3, sticky="ew", padx="1", pady="1")

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

#label resultado
txt_row=Text(root, bg="plum", width=25, height=5, wrap=WORD)
txt_row.grid(row=5, column=2, sticky="w", padx="1", pady="1")
#row=[]
#label_row=Label(root, bg="plum", text=row)
#label_row.grid(row=5, column=2, sticky="w", padx="1", pady="1")

#----------------------------------------------------------------

#boton buscar
Boton2=Button(root, text="Buscar", command=test_cuit)
Boton2.grid(row=6, column=3, sticky="nswe", padx="1", pady="10")

#boton salir
Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=7, column=3, sticky="nswe", padx="1", pady="10")


root.mainloop()




