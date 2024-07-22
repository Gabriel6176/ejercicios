import sqlite3

miConexion=sqlite3.connect("Gestion productos1.db")

miCursor=miConexion.cursor()

##miCursor.execute('''
##    CREATE TABLE PRODUCT (
##    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
##    NOMBRE_ARTICULO VARCHAR(50), 
##    PRECIO INTEGER, 
##    SECCION VARCHAR(50))
##''')

productos=[

    ("Pelota", 10, "Artculos Vestir"),
    ("Pantalon", 20, "Ropa"),
    ("Destornillador", 20, "Ferreteria")
]

miCursor.executemany("INSERT INTO PRODUCT VALUES(NULL,?,?,?)", productos) 

   
miConexion.commit()

miConexion.close()












