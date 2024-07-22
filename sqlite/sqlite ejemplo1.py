import sqlite3

miConexion=sqlite3.connect("PrimeraBase.db")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCT (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(50))")

#miCursor.execute("INSERT INTO PRODUCT VALUES('BALON', 15, 'DEPORTES')")

###variosProductos=[
#
#    ("Camiseta", 20, "Jugeteria"),
#    ("Jaroon", 20, "Cerramica"),
#    ("Camion", 20, "Jugueteria")
#]
####miCursor.executemany("INSERT INTO PRODUCT VALUES(?,?,?)", variosProductos) 

miCursor.execute("SELECT * FROM PRODUCT")

variosProductos=miCursor.fetchall()
for producto in variosProductos:
## solo devuelve la primera columna
##    print(producto[0])
## solo devuelve todo
##    print(producto)
## selecciono solo las columnas que quiero 
    print("Nombre Producto", producto[0], " Seccion", producto[2])

    
miConexion.commit()

miConexion.close()












