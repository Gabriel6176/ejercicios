#enconding: utf-8
import time
import requests
import datetime as dt
import pandas as pd
import os

url = "http://190.52.34.65/Notificaciones/Informacion/ConsultaPuco"

#time = dt.datetime.now()
#print(time)

APP_PATH = os.getcwd()


def send_request(dni):
    data = {"dni":dni}
    r=requests.post(url, data=data)
    print(r.text)
    try:
        if 0<cont<10000:
            archivo=open(APP_PATH+'\\dni45.csv', 'a', encoding='utf8')
            archivo.write(r.text+"\n")
        elif 10000<cont<20000:
            archivo=open(APP_PATH+'\\dni46.csv', 'a', encoding='utf8')
            archivo.write(r.text+"\n")   
        elif 20000<cont<30000:
            archivo=open(APP_PATH+'\\dni47.csv', 'a', encoding='utf8')
            archivo.write(r.text+"\n")
        elif 30000<cont<40000:
            archivo=open(APP_PATH+'\\dni48.csv', 'a', encoding='utf8')
            archivo.write(r.text+"\n") 
                  
    except Exception as e:
        print('-----------llego a except-111------------')
        time.sleep(150)
        send_request(str(numero_dni))

cont=0
numero_dni=26117482
d1='"'
contador=1
#for i in numero_dni:
#    send_request(i)
#    time.sleep(2)

while contador<50000:
    try:
        if contador<400:
            send_request(str(numero_dni))
            #print(d1+str(numero_dni)+d1)
            numero_dni+=1
            contador+=1
            cont+=1
            time.sleep(1)
        else:
            print('NUEVO CICLO XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            time.sleep(25)
            print('NUEVO CICLO XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            contador=0
    except ValueError:
        print('-----------llego a except-------------')
        time.sleep(150)
        send_request(str(numero_dni))

else:
    print('llego a else')
    pass


"""
{TipoDocumento: "DNI",
NroDocumento: "25675503", 
ClaseDocumento: "Propio",
FechaNacimiento: "--",
Nombre: "ALVAREZ MEIJIDE GABRIEL ALEJAN",
NroDocumento: "25675503",
ObraSocial: "OBRA SOCIAL UNION PERSONAL DE LA UNION DEL  PERSONAL CIVIL DE LA NACION",
Siglas: "OSPCN",
TipoDocumento: "DNI"}

{"Estado":"OK","Items":[{"TipoDocumento":"DNI","NroDocumento":"25675503","ClaseDocumento":"Propio","Nombre":"ALVAREZ MEIJIDE GABRIEL ALEJAN","FechaNacimiento":"--","ObraSocial":"OBRA SOCIAL UNION PERSONAL DE LA UNION DEL  PERSONAL CIVIL DE LA NACION","Siglas":"OSPCN"}]}

elif 10001<cont<20000:
        archivo=open(APP_PATH+'\\dni5.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 10001<cont<30000:
        archivo=open(APP_PATH+'\\dni5.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 20001<cont<30000:
        archivo=open(APP_PATH+'\\dni6.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')      
    elif 30001<cont<40000:
        archivo=open(APP_PATH+'\\dni7.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 40001<cont<50000:
        archivo=open(APP_PATH+'\\dni8.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 50001<cont<60000:
        archivo=open(APP_PATH+'\\dni9.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 60001<cont<70000:
        archivo=open(APP_PATH+'\\dni10.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 70001<cont<80000:
        archivo=open(APP_PATH+'\\dni11.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 80001<cont<90000:
        archivo=open(APP_PATH+'\\dni12.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 90001<cont<100000:
        archivo=open(APP_PATH+'\\dni13.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 100001<cont<110000:
        archivo=open(APP_PATH+'\\dni14.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 110001<cont<120000:
        archivo=open(APP_PATH+'\\dni15.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 120001<cont<130000:
        archivo=open(APP_PATH+'\\dni16.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 130001<cont<140000:
        archivo=open(APP_PATH+'\\dni17.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 140001<cont<150000:
        archivo=open(APP_PATH+'\\dni18.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 150001<cont<160000:
        archivo=open(APP_PATH+'\\dni19.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 160001<cont<170000:
        archivo=open(APP_PATH+'\\dni20.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 170001<cont<180000:
        archivo=open(APP_PATH+'\\dni21.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 170001<cont<180000:
        archivo=open(APP_PATH+'\\dni22.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 180001<cont<190000:
        archivo=open(APP_PATH+'\\dni23.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 190001<cont<200000:
        archivo=open(APP_PATH+'\\dni24.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 200001<cont<210000:
        archivo=open(APP_PATH+'\\dni25.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 210001<cont<220000:
        archivo=open(APP_PATH+'\\dni26.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 220001<cont<230000:
        archivo=open(APP_PATH+'\\dni27.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 230001<cont<240000:
        archivo=open(APP_PATH+'\\dni28.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 240001<cont<250000:
        archivo=open(APP_PATH+'\\dni29.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 250001<cont<260000:
        archivo=open(APP_PATH+'\\dni30.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 260001<cont<270000:
        archivo=open(APP_PATH+'\\dni31.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 270001<cont<280000:
        archivo=open(APP_PATH+'\\dni32.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 280001<cont<290000:
        archivo=open(APP_PATH+'\\dni33.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 290001<cont<300000:
        archivo=open(APP_PATH+'\\dni34.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 300001<cont<310000:
        archivo=open(APP_PATH+'\\dni35.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 310001<cont<320000:
        archivo=open(APP_PATH+'\\dni36.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 320001<cont<330000:
        archivo=open(APP_PATH+'\\dni37.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 330001<cont<340000:
        archivo=open(APP_PATH+'\\dni38.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 340001<cont<350000:
        archivo=open(APP_PATH+'\\dni39.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 350001<cont<360000:
        archivo=open(APP_PATH+'\\dni40.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 360001<cont<370000:
        archivo=open(APP_PATH+'\\dni41.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 370001<cont<380000:
        archivo=open(APP_PATH+'\\dni42.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 380001<cont<390000:
        archivo=open(APP_PATH+'\\dni43.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 390001<cont<400000:
        archivo=open(APP_PATH+'\\dni44.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 400001<cont<410000:
        archivo=open(APP_PATH+'\\dni45.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 410001<cont<420000:
        archivo=open(APP_PATH+'\\dni46.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 420001<cont<430000:
        archivo=open(APP_PATH+'\\dni47.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 430001<cont<440000:
        archivo=open(APP_PATH+'\\dni48.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 440001<cont<450000:
        archivo=open(APP_PATH+'\\dni49.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 450001<cont<460000:
        archivo=open(APP_PATH+'\\dni50.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 460001<cont<470000:
        archivo=open(APP_PATH+'\\dni51.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 470001<cont<480000:
        archivo=open(APP_PATH+'\\dni52.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 480001<cont<490000:
        archivo=open(APP_PATH+'\\dni53.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    elif 490001<cont<500000:
        archivo=open(APP_PATH+'\\dni54.csv', 'a', encoding='utf8')
        archivo.write(r.text+"\n")
        print('Procesado')
    


"""


