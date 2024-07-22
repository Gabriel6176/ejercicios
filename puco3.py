#enconding: utf-8
import time
import requests
import datetime as dt
import pandas as pd
import os
from urllib.request import Request
from urllib.request import urlopen

#url2 = Request("http://190.52.34.65/Notificaciones/Informacion/ConsultaPuco")
#url2.add_header=('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
#url2.add_header=('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')

url = "http://190.52.34.65/Notificaciones/Informacion/ConsultaPuco"


APP_PATH = os.getcwd()


def send_request(dni):
    data = {"dni":dni}
    r=requests.post(url, data=data)
    print(r.text)
    narchivo=1000
    rango=40000
    if 0<cont<rango:
        archivo=open(APP_PATH+'\\dni'+(str(narchivo))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif rango<cont<(rango*2):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+1))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*2)<cont<(rango*3):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+2))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*3)<cont<(rango*4):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+3))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*4)<cont<(rango*5):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+4))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*5)<cont<(rango*6):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+5))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*6)<cont<(rango*7):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+6))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*7)<cont<(rango*8):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+7))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*8)<cont<(rango*9):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+8))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*9)<cont<(rango*10):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+9))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*10)<cont<(rango*11):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+10))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*11)<cont<(rango*12):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+11))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*12)<cont<(rango*13):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+12))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*13)<cont<(rango*14):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+13))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*14)<cont<(rango*15):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+14))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*15)<cont<(rango*16):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+15))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*16)<cont<(rango*17):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+16))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*17)<cont<(rango*18):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+17))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*18)<cont<(rango*19):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+18))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*19)<cont<(rango*20):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+19))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*20)<cont<(rango*21):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+20))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*21)<cont<(rango*22):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+21))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*22)<cont<(rango*23):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+22))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*23)<cont<(rango*24):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+23))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*24)<cont<(rango*25):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+24))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*25)<cont<(rango*26):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+25))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*26)<cont<(rango*27):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+26))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*27)<cont<(rango*28):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+27))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*28)<cont<(rango*29):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+28))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*29)<cont<(rango*30):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+29))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*30)<cont<(rango*31):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+30))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*31)<cont<(rango*32):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+31))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*32)<cont<(rango*33):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+32))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*33)<cont<(rango*34):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+33))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*34)<cont<(rango*35):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+34))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*35)<cont<(rango*36):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+35))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*36)<cont<(rango*37):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+36))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*37)<cont<(rango*38):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+37))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*38)<cont<(rango*39):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+38))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*39)<cont<(rango*40):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+39))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*40)<cont<(rango*41):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+40))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*41)<cont<(rango*42):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+41))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        
    elif (rango*42)<cont<(rango*43):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+42))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")

    elif (rango*43)<cont<(rango*44):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+43))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")        

    elif (rango*44)<cont<(rango*45):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+44))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")

    elif (rango*45)<cont<(rango*46):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+45))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")

    elif (rango*46)<cont<(rango*47):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+46))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")

    elif (rango*47)<cont<(rango*48):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+47))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")

    elif (rango*48)<cont<(rango*49):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+48))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")

    elif (rango*49)<cont<(rango*50):
        archivo=open(APP_PATH+'\\dni'+(str(narchivo+49))+'.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")




cont=0
numero_dni=20100100
d1='"'
contador=1

while contador<500000000:
    timeout = 15
    mustend = time.time()+timeout
    if time.time()<mustend:
        try:
            if contador<6000:
                send_request(str(numero_dni))
                #print(d1+str(numero_dni)+d1)
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