import os
import sqlite3


def crear_base():
    APP_PATH = os.getcwd()
    #le pone el mismo nombre a la base que al txt
    DB_PATH = APP_PATH+'\\'+'base'+'.db'
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS BASE
        (CUIT INT, 
        LINEA NVARCHAR(200)
        )''')
    con.commit()
    cursor.execute('''CREATE UNIQUE INDEX IF NOT EXISTS cuit_index on base (CUIT)''')
    #importar(con, cursor)
    con.close()

if __name__=='__main__':
    crear_base()