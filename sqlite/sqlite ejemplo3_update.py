import sqlite3

miConexion=sqlite3.connect("ejemplo3.db")

miCursor=miConexion.cursor()

##miCursor.execute('''
##    CREATE TABLE PRODUCT (
#    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#    NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
#    PRECIO INTEGER, 
#    SECCION VARCHAR(50))
#''')

#productos=[
#    ("Pelota", 10, "Artculos Vestir"),
#    ("Pantalon", 20, "Ropa"),
#    ("Destornillador", 20, "Ferreteria"),
#    ("Jarron", 55, "Petaso")
#]

#miCursor.executemany("INSERT INTO PRODUCT VALUES(NULL,?,?,?)", productos) 


#miCursor.execute("UPDATE PRODUCT SET PRECIO=45 WHERE NOMBRE_ARTICULO='Pelota'")

miCursor.execute("DELETE PRODUCT SET PRECIO=45 WHERE NOMBRE_ARTICULO='Pelota'")

miConexion.commit()

miConexion.close()

