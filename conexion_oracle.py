import cx_Oracle

try:
    connection=cx_Oracle.connect(
        user='noematica',
        password='noematica',
        dsn='172.21.14.22:1521/WBMD',
        encoding='UTF-8'
    )
    print(connection.version)
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM adtmap_conf;')
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    
except Exception as ex:
    print(ex)

finally:
    connection.close()
    print('coneccion cerrada')