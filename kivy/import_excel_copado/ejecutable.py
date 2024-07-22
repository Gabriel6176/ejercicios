import sqlite3
import pandas as pd
import os
from os import remove

APP_PATH = os.getcwd()
print(APP_PATH)
DB_PATH = APP_PATH+'\\excel.db'
con = sqlite3.connect('excel.db')
wb = pd.read_excel(APP_PATH+'\\archivo.xlsx',sheet_name = None)
for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)

APP_PATH = os.getcwd()
DB_PATH = APP_PATH+'\\excel.db'
con = sqlite3.connect(DB_PATH)
cursor = con.cursor()
cursor.execute('SELECT CAMPO1, CAMPO2, CAMPO3, CAMPO4, CAMPO5, CAMPO6, CAMPO7, CAMPO8, CAMPO9, CAMPO10 FROM Hoja1')

contador=1
for i in cursor:
    if contador<2:
        c1 = str(i[0])
        c2 = str(i[1])
        c3 = str(i[2])
        c4 = str(i[3])
        c5 = str(i[4])
        c6 = str(i[5])
        c7 = str(i[6])
        c8 = str(i[7])
        c9 = str(i[8])
        c10 =str(i[9])
        c11 = str(";")
        c12 = str('"')
        data_id=(c1+c11+c2+c11+c3+c11+c4+c11+c5+c11+c6+c11+c7+c11+c8+c11+c9+c11+c10)
        contador=contador+1
        try:
            archivo=open(APP_PATH+'\\archivo_csv.csv', 'a', encoding='utf8')
            archivo.write(data_id+"\n")
        except Exception as e:
            print(e)
        finally:    
            archivo.close()
            print('Procesando..')
            
            
    else:
        for i in cursor:
            c1 = str(i[0])
            c2 = str(i[1])
            c3 = str(i[2])
            c4 = str(i[3])
            c5 = str(i[4])
            c6 = str(i[5])
            c7 = str(i[6])
            c8 = str(i[7])
            c9 = str(i[8])
            c10 =str(i[9])
            c11 = str(";")
            c12 = str('"')
            data2_id=(c12+c1+c12+c11+c12+c2+c12+c11+c12+c3+c12+c11+c12+c4+c12+c11+c12+c5+c12+c11+c12+c6+c12+c11+c12+c7+c12+c11+c12+c8+c12+c11+c12+c9+c12+c11+c12+c10+c12)
            try:
                archivo=open(APP_PATH+'\\archivo_csv.csv', 'a', encoding='utf8')
                archivo.write(data2_id+"\n")
            except Exception as e:
                print(e)
            finally:    
                archivo.close()
                print('Procesando...')
                
con.close()
remove("excel.db")



