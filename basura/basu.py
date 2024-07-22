import time
import requests
import datetime as dt
import pandas as pd
import os

APP_PATH = os.getcwd()



def send_request(dni, cont):
    dni=dni
    cont=cont
    #data = {"dni":dni}
    #r=requests.post(url, data=data)
    #print(r.text)
    if cont<12:
        archivo=open(APP_PATH+'\\ahola1.csv', 'a', encoding='utf8')
        archivo.write(str(dni)+"gabriel\n")
        print('Procesado')
    if 12<cont<25:
        archivo=open(APP_PATH+'\\ahola2.csv', 'a', encoding='utf8')
        archivo.write(str(dni)+"gabriel\n")
        print('PProcesando')
    if 25<cont<50:
        archivo=open(APP_PATH+'\\ahola3.csv', 'a', encoding='utf8')
        archivo.write(str(dni)+"gabriel\n")
        print('PPProcesado')

cont=0
dni=1    
contador=0
while contador<15:
    send_request(dni, cont)
    print(contador)
    time.sleep(1)
    contador+=1
    dni+=1
    cont+=1
    if contador==15:
        time.sleep(3)
        contador=0
        

