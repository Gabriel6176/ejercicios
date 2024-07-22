import sqlite3
import os
import pandas as pd

#insert from csv to db table

def crear_base():
    db_name='base2'
    table_name='table1'
    d1='CAMPO1'
    t1='INT'
    d2='CAMPO2'
    t2='INT'
    APP_PATH = os.getcwd()
    con = sqlite3.connect(APP_PATH+'\\'+db_name+'.db')
    cursor=con.cursor()
    instruction=f"CREATE TABLE IF NOT EXISTS {table_name} ({d1} {t1}, {d2} {t2})"
    cursor.execute(instruction)

#me da error el pandas al intentar importar porque hay tres lineas que tienen ';' en el nombre
#eso hace que entienda que hay mas columnas por el ';' es el separador
def insert_data(db_name):
    csv_name='ardx'
    APP_PATH = os.getcwd()
    con = sqlite3.connect(APP_PATH+'\\'+db_name+'.db')
    cursor=con.cursor()
    #si quiero leer desde registo 1M hasta 1,999M
    #read_csv(..., skiprows=1000000, nrows=999999)
    # load the data into a Pandas DataFrame
    users = pd.read_csv(f"{csv_name}.csv", sep=';')
    # write the data to a sqlite table
    #print(users)
    users.to_sql(csv_name, con, if_exists='append', index = False)
    con.commit()
    cursor.close()

    
if __name__=='__main__':
    crear_base()



