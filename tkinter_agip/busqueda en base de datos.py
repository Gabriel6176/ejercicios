import os
import sqlite3

cuit=20001019180

APP_PATH=os.getcwd()

#20000948676

def buscar(cuit):
    d1='base'
    print(d1)
    d2=d1+'.db'
    print(d2)
    con = sqlite3.connect(APP_PATH+'\\'+d2)
    cursor=con.cursor()
    #no le pongo comillas a cuit porque es un numero
    instruccion=f"SELECT LINEA FROM '{d1}' WHERE (CUIT = {cuit});"
    #instruccion=f"SELECT LINEA FROM base WHERE (CUIT = 20000948676)"
    cursor.execute(instruccion)
    respuesta=cursor.fetchall()
    con.commit()
    con.close()
    print(respuesta)

if __name__=='__main__':
    buscar(cuit)
