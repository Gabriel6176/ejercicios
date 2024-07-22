#encoding: ANSI
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


root=Tk()
root.title("Lector de TXT AGIP v1.5")
#esta version lee el txt verifica si es UTF-8 sino convierte el txt dejandolo de igual nombre al original en formato UTF-8

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
    txt_row.delete(0.0, 'end')
    resultado=[]
    label_resultado.config(text=resultado)
    label_resultado.config(text=str('Procesando'))
    print('hola')
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
    value=True
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
        buscar(linea, value, cuit, d1, x)


def print_resultado(linea, cuit, value, count, d1):
    txt_row.delete(0.0, 'end')
    print(f'La linea es: {linea} el cuit es: {cuit} el value es: {value} el contador es: {count}') 
    if linea>0:
        label_resultado.config(text=str('Encontrado'))
    else:
        label_resultado.config(text=str('No Encontrado'))
    texto=linecache.getline(APP_PATH+'\\'+d1+'.txt', linea)
    txt_row.insert(0.0, texto)


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
        line=linecache.getline(APP_PATH+'\\'+d1+'.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
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
        line=linecache.getline(APP_PATH+'\\'+d1+'.txt', linea)
        texto=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
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
Boton2=Button(root, text="Buscar", command=detectar_si_utf)
Boton2.grid(row=6, column=3, sticky="nswe", padx="1", pady="10")

#boton salir
Boton3=Button(root, text="Salir", command=salir)
Boton3.grid(row=7, column=3, sticky="nswe", padx="1", pady="10")


root.mainloop()




