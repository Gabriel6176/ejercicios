from datetime import date
import pandas as pd
from workalendar.europe import France

cal=France
cal.holidays(2022)






#-----------feriados x pais-----------
#cal = France()
#feriados=cal.holidays(2022)
#df=pd.DataFrame(feriados,columns=['fecha','nombre'])
#df['fecha']=pd.to_datetime(df['fecha'])
#df['fecha'] = df['fecha'].dt.day_name()
#df=df.groupby('fecha').count().sort_values('nombre', ascending=False)
#print(df)
#-----------------------




# import pandas as pd
# from datetime import date
# from workalendar.europe import France
# cal=France()


# a=int(input('Ingresa un año para informarte los dias feriados'))
# anio=2022
# anio_minimo=1900
# feriados=cal.holidays(a)

# if a > anio:
#     print(f'El numero informado es mayor al {anio} en curso')
#     a
# elif a < anio:
#     print(f'El numero informado {anio} en menor a 1900')
#     a
# else:
#     print(feriados)
