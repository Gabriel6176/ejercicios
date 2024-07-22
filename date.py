from time import *
import datetime
from datetime import date

var1= datetime.datetime.now()
print(var1)
#2022-09-19 09:03:14.532241

var2=datetime.date.today()
print(var2)
#2022-09-19

var3=date.today()
print(var3)
#2022-09-19

var4= datetime.datetime.now()
print(var4.hour, var4.minute, var4.second)
#10 37 53    //hora minuto segundos