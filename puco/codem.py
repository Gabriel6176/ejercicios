import time
import requests
import datetime as dt
import pandas as pd
import os

url = "http://servicioswww.anses.gob.ar/ooss2/"

#time = dt.datetime.now()
#print(time)

APP_PATH = os.getcwd()

d1="__EVENTTARGET"
d2=""
d3="__EVENTARGUMENT"
d4=""
d5="__VIEWSTATE"
d6="/wEPDwUJNTExMTIwMjIzDxYCHghGZWNoYVNRTAUKMTgvMDMvMjAyMhYCZg9kFgICAw9kFgYCAw8PFgIeBFRleHQFBHYxLjFkZAIFDxYCHglpbm5lcmh0bWwF8gE8ZGl2IGlkPSdtZW51Jz48ZGl2IGlkPSdfX2RpdlBhc28xJyBjbGFzcz0nYWN0aXZvJz48YSBocmVmPSdqYXZhc2NyaXB0OnZvaWQoMCk7Jz4xLiBJbmdyZXNhciBDdWlsIG8gTnJvIGRlIERvY3VtZW50byBkZSBJZGVudGlkYWQ8L2E+PC9kaXY+PGRpdiBpZD0nX19kaXZQYXNvMicgY2xhc3M9J2luYWN0aXZvJz48YSBocmVmPSdqYXZhc2NyaXB0OnZvaWQoMCk7Jz4yLiBDb25zdGFuY2lhPC9hPjwvZGl2PjwvZGl2PjxiciAvPmQCBw9kFgYCBQ9kFgJmD2QWBgIBDw9kFgQeB29uS2V5VXAFHnJldHVybiBhdXRvVGFiKHRoaXMsIDIsIGV2ZW50KR4Hb25mb2N1cwUZcmV0dXJuIHNlbGVjY2lvbih0aGlzLCAyKWQCAw8PZBYEHwMFHnJldHVybiBhdXRvVGFiKHRoaXMsIDgsIGV2ZW50KR8EBRlyZXR1cm4gc2VsZWNjaW9uKHRoaXMsIDgpZAIFDw9kFgQfAwUecmV0dXJuIGF1dG9UYWIodGhpcywgMSwgZXZlbnQpHwQFGXJldHVybiBzZWxlY2Npb24odGhpcywgMSlkAhMPDxYCHgdWaXNpYmxlaGQWAgIBDzwrAAsAZAIVDw8WAh8BBStMb3MgZGF0b3MgZXN0w6FuIGFjdHVhbGl6YWRvcyBhbCAxOC8wMy8yMDIyZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFK2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkbWVuc2FqZSRpbWdDZXJyYXLE0Pg6lIZD8PJ73/GNJdMitQq4u1x82dR/Sg1AoisL3Q=="
d7="__VIEWSTATEGENERATOR"
d8="85A7BA68"
d9="__EVENTVALIDATION"
d10="/wEdAAzjqNjt94ESipCFqqKenSUn0JcPQZRczZ7KHL6vOZ5InO1/O3L1/xJ8QnozRybIU5qdXrqsbkaSHEKYmzqYUqEiHpiEu0R7takrHOJWf39cdWuq8aT80eSLyZQYnc6EFMOMO7fmjkJSfq6Zbgk2kTWnitppBoWdcpou47WwpGbh74rjhqKy4xkNMCbEy8CfpoBN/4+VrNjQYiLFBQLJp926SLwHHNaaQRs0j2+MfYfB+hgYJ4+6XoMvJ43qiosOoPZNLZM3ilboufw3uBvTI56DrcxX5aOYcKWEWh1oeXdKMQ=="
d11="ctl00$ContentPlaceHolder1$ctrlCuil$txtCodigo"
d12="20"
d13="ctl00$ContentPlaceHolder1$ctrlCuil$txtNumero"
d14="25675503"
d15="ctl00$ContentPlaceHolder1$ctrlCuil$txtDigito"
d16="4"
d17="ctl00$ContentPlaceHolder1$txtDoc"
d18="25675503"
d19="ctl00$ContentPlaceHolder1$CodeNumberTextBox"
d20="296366"
d21="ctl00$ContentPlaceHolder1$Button1"
d22="Continuar"

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
        d19:d20,
        d21:d22
        }
    r=requests.post(url, data=data)
    print(r.text)
    archivo=open(APP_PATH+'\\dni2.csv', 'a', encoding='utf8')
    archivo.write(r.text+"\n")
    print('Procesado')

numero_dni=25675600
contador=1


while contador<2:
    send_request(int(25675503))
    #send_request(str(numero_dni))
    #print(str(numero_dni))
    numero_dni+=1
    contador+=1
    #time.sleep(1)
else:
    print('llego a else')
    pass