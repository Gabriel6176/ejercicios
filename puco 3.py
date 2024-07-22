#enconding: utf-8
import time
import requests
import datetime as dt
import pandas as pd
import os
import re

url = "http://190.52.34.65/Notificaciones/Informacion/ConsultaPuco"

APP_PATH = os.getcwd()

def guardado(datos, cont):
    narchivo=200
    rango=40000
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
    f=str(r.text)
    if len(f)>35:
        print()
        d1 = re.search('(\d\d\d\d\d\d\d\d)', f).group(1)
        d2 = re.search('bre":"(.+?)","Fech', f).group(1)
        d3 = re.search('al":"(.+?)","Si', f).group(1)
        d4 = re.search('as":"(.+?)"}', f).group(1)
        d5=cont
        print(d5)
        data=d1+","+d2+","+d3+","+d4
        print(data, d5)
        guardado(data, d5)
    else:
        d6=cont
        guardado(data, d6)
        
cont=0
numero_dni=40000000
contador=1

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
        print(f"Exception has been raised: {e}")
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