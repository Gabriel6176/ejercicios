import os
import sqlite3


def crear_base():
    APP_PATH = os.getcwd()
    #le pone el mismo nombre a la base que al txt
    db_name= 'base1'
    #la tabla no puede tener nombre 'table'
    table_name= 'table1'
    d1= 'CAMPO1'
    t1= 'INT'
    d2= 'CAMPO2'
    t2= 'NVARCHAR(200)'
    index_name= 'index_name'
    DB_PATH = APP_PATH+'\\'+db_name+'.db'
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    instruction=f"CREATE TABLE IF NOT EXISTS {table_name} ({d1} {t1}, {d2} {t2})"
    print(instruction)
    cursor.execute(instruction)
    con.commit()
    index_text=f"CREATE UNIQUE INDEX IF NOT EXISTS {index_name} on {table_name} ({d1})"
    cursor.execute(index_text)
    #importar(con, cursor)
    con.close()

if __name__=='__main__':
    crear_base()