import os
import pandas as pd
import numpy as np

#array desde cdv
APP_PATH=os.getcwd()
df3=pd.read_csv(APP_PATH+'\\students.csv', header=0)
###print(df3)

#leer las primeras 5 filas
#print(df3.head(5))

#leer las ultimas 5 filas
#print(df3.tail(5))

#ver el shape p formato - filas y columnas
#print(df3.shape)

#seteo el maximo de filas que quiero ver
##pd.set_option('display.max_rows', 8) #me muestra las primeras 4 y las ultimas 4 
#tambien te dice abajo cuantas filas y columas tiene en total
df4=pd.read_csv(APP_PATH+'\\students.csv', header=0)
###print(df4)

#para ver el rango:
#dira: RangeIndex(start=0, stop=16, step=1)
###print(df4.index)

#para ver columnas
#Index(['gender', 'rade', 'parental', 'lunch', 'test preparatior', 'math', 'reading', 'writing'], dtype='object')
###print(df4.columns)

#para ver cada columna (veo que las primeras son texto y las ultimas data numerica)
'''
gender              object
rade                object
parental            object
lunch               object
test preparatior    object
math                 int64
reading              int64
writing              int64
dtype: object
'''
###print(df4.dtypes)

#dat info veo si hay data nula
'''
RangeIndex: 16 entries, 0 to 15
Data columns (total 8 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   gender            16 non-null     object
 1   rade              16 non-null     object
 2   parental          16 non-null     object
 3   lunch             16 non-null     object
 4   test preparatior  16 non-null     object
 5   math              16 non-null     int64
 6   reading           16 non-null     int64
 7   writing           16 non-null     int64
dtypes: int64(3), object(5)
memory usage: 1.1+ KB
None
'''
##print(df4.info())


#para ver estadistica del dataframe
#count dice cuantas filas hay
#mean = promedio
#std=division estadand
#min=minimo
#25%=el percentil
#50%=el percentil
#75%=el percentil
#max=maximo
'''
          math    reading    writing
count  16.000000  16.000000  16.000000
mean   64.312500  56.125000  69.750000
std    16.779824   9.457801   9.814955
min    22.000000  31.000000  45.000000
25%    71.500000  58.000000  74.000000
50%    72.000000  58.000000  74.000000
75%    72.000000  58.000000  74.000000
max    72.000000  78.000000  77.000000
'''
print(df4.describe())

