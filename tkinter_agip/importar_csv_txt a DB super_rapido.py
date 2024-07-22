import linecache
import re
import pandas as pd
import os
import sqlite3

APP_PATH=os.getcwd()

def importar_db(df):
    #podes importar csv o txt
    table='base'
    APP_PATH = os.getcwd()
    con = sqlite3.connect(APP_PATH+'\\'+df+'.db')
    cursor=con.cursor()
    #si quiero leer desde registo 1M hasta 1,999M
    #read_csv(..., skiprows=1000000, nrows=999999)
    # load the data into a Pandas DataFrame
    users = pd.read_csv(f"{df}_2.txt", sep=';', usecols=['CUIT', 'LINEA']) [['CUIT', 'LINEA']]
    # write the data to a sqlite table
    #print(users)
    #users.to_sql(csv_name, con, if_exists='append', index = False)
    users.to_sql(table, con, if_exists='append', index=False)
    con.commit()
    cursor.close()

if __name__=='__main__':
    importar_db('ard')