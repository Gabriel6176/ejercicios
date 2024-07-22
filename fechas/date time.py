#from datetime import datetime
#import calendar


#dt = datetime.datetime.today()
#dia = str(dt.day)
#mes = str(dt.month)
#anio = str(dt.year)
#print(dia + "/" + mes + "/" + anio)

###---------------------------------------------------
#test_date = datetime(2020, 4, 8)
# getting month name using %B
#res = test_date.strftime("%B")
 
# printing result
#print("Month Name from Date : " + str(res))
"""
#----------------------------------------------------
import calendar
year = 2018
month = 12
print(calendar.month(year, month, w=8, l=0))
"""
import calendar, locale
locale.setlocale(locale.LC_ALL, 'es-ES')
'es-ES'
anio = 2018
mes = 2
print(calendar.month(anio, mes))










