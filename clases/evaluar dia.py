import time
import datetime

print(time.strftime("%d:%m:%Y"))

tiempo=time.strftime("%d:%m:%Y")

ahora = datetime.datetime.now()
print(ahora)
print(ahora.minute)
print(ahora.month)
print(ahora.year)

#para imprimir el año
print(datetime.date.today().year)
fecha0= "11/04/2022"
fecha0=datetime.datetime.strptime(fecha0,"%d/%m/%Y")

fecha = "21/01/1991"
print(fecha)
# es strp srt parce
fecha=datetime.datetime.strptime(fecha,"%d/%m/%Y")
print(fecha)

if fecha0 < fecha:
    print('pa atomica')
    pass
else:
    break
    print('pty an dep')
    

'''
f_date = time.localtime()
print(f_date)
s_date = "2019/10/01"
print(s_date)

f_d1 = datetime.strptime(f_date, "%d/%m/%Y")
f_d2 = datetime.strptime(s_date, "%d/%m/%Y")
print(f_d1 > f_d2)

if f_d1 < f_d2:
    print('hola')
else:
    print('big pete y ano')
'''