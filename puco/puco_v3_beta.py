#enconding: utf-8
import time
import requests
import datetime as dt
import pandas as pd
import os
import re

numero_dni=20000000
narchivo=100
contador=1
cont=0


url = "http://190.52.34.65/Notificaciones/Informacion/ConsultaPuco"

APP_PATH = os.getcwd()

def guardado(datos, cont):
    rango=40000
    datos=str(datos)
    if 0<cont<rango:
        archivo=open(APP_PATH+'\\dni'+(str(narchivo))+'.csv', 'a', encoding='utf8')
        archivo.write(datos+"\n")
       
    elif rango<cont<(rango*2):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+1))+'.csv', 'a', encoding='utf8')
        archivo.write(datos+"\n")


def send_request(dni):
    data = {"dni":dni}
    r=requests.post(url, data=data)
    print(r.text)
    linea=(r.text)
    if len(linea)>35:
        try:
            #con \d busca digitos
            d1 = re.search('(\d\d\d\d\d\d\d\d)', linea).group(1)
            #con texto.+texto busca texto que comience con texto(algo en el medio)texto, al poner parentesis lo que me retorna es lo que esta entre () sino todo entre ''
            #si lo del medio lo pongo entre parentesis y al group le pongo(1) me regresa lo que esta entre parentesis (.+) 
            # 
            # el ? es para que la ocurrencia sera zero o una, agarra la primera que encuentra
            d2 = re.search('bre":"(.+?)","Fech', linea).group(1)
            d3 = re.search('al":"(.+?)","Si', linea).group(1)
            d4 = re.search('as":"(.+?)"}', linea).group(1)
            data=(d1+","+d2+","+d3+","+d4)
            print(cont)
            guardado(data, cont)
        except Exception as e:
            print(f'Exception has been raised_2: {e}')
    else:
        d6=cont
        dato=(str(dni)+str(","))
        guardado(dato, d6)
       
while contador<500000000:
    try:
        if contador<6000:
            send_request(str(numero_dni))
            numero_dni+=1
            contador+=1
            cont+=1
            time.sleep(0)
        else:
            print('NUEVO CICLO XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            time.sleep(10)
            print('NUEVO CICLO XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            contador=0
    except Exception as e:
        print(f"Exception has been raised_1: {e}")
        send_request(str(numero_dni))
        numero_dni+=1
        contador+=1
        cont+=1
        print('XXXXXXXXXXXXXXX-EXCEPT-XXXXXXXXXXXXXXXXXXXXXXXXX')
else:
    archivo=open(APP_PATH+'\\dni200.csv', 'a', encoding='utf8')
    archivo.write(numero_dni+"\n")
    numero_dni+=1
    contador+=1
    cont+=1
    print('XXXXXXXXXXXXXXX-ELSE-XXXXXXXXXXXXXXXXXXXXXXXXX')
