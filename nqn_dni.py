import time
import requests
import datetime as dt
import pandas as pd
import os

url = "http://www.saludnqn.gob.ar/PadroncONSULTASWeb/"

#time = dt.datetime.now()
#print(time)

APP_PATH = os.getcwd()

d1="__LASTFOCUS"
d2=""
d3="__EVENTTARGET"
d4=""
d5="__EVENTARGUMENT"
d6=""
d7="__MAGICAJAX_SCRIPT_FINGERPRINTS"
d8=""
d9="__MAGICAJAX_HEAD_FINGERPRINTS"
d10="C4A56AAA;889758E3"
d11="__VIEWSTATE"
d12="/wEPDwULLTEyNzkzOTMzNTkPZBYCZg9kFgICAw9kFgICAw9kFgQCAQ8PZBYCHgpvbmtleXByZXNzBTtyZXR1cm4gY29udHJvbEVudGVyKCdDb250ZW50UGxhY2VIb2xkZXIxX2J0bkJ1c2NhcicsIGV2ZW50KWQCCQ9kFgQCAQ8PZA8QFgFmFgEWAh4OUGFyYW1ldGVyVmFsdWVkFgECAmRkAgMPPCsAEQMADxYEHgtfIURhdGFCb3VuZGceC18hSXRlbUNvdW50ZmQBEBYAFgAWAAwUKwAAZBgBBSRjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGd2UGVyc29uYXMPPCsADAEIZmQ2XjF/zzMTIqlXFqIjMZgEajbHss3Qp8mHjW27fytBPg=="
d13="__VIEWSTATEGENERATOR"
d14="7397EAF2"
d15="__EVENTVALIDATION"
d16="/wEdAAPA7cilTJ2bole72tCaxbahMfyS3NajvWkq6DDPrG6uMeFj+uPXOTppB7k1mvUecKW5xK8UKx4qAWJWIHqb5WTitMUqP3iysiMwqJK1D5tbMw=="
d17="ctl00$ContentPlaceHolder1$txtNumero"
d18=""
d19="ctl00$ContentPlaceHolder1$btnBuscar"
d20="Buscar"

def send_request(dni):
    data = {
        d1:d2,
        d3:d4,
        d5:d6,
        d7:d8,
        d9:d10,
        d11:d12,
        d13:d14,
        d15:d16,
        d17:dni,
        d19:d20
        }
    r=requests.post(url, data=data)
    print(r.text)
    archivo=open(APP_PATH+'\\dni2.csv', 'a', encoding='utf8')
    archivo.write(r.text+"\n")
    print('Procesado')

numero_dni=25675600
contador=1


while contador<2:
    send_request(int(25676123))
    #send_request(str(numero_dni))
    #print(str(numero_dni))
    numero_dni+=1
    contador+=1
    #time.sleep(1)
else:
    print('llego a else')
    pass