#formato cadena
#upper()    mayusculas
#lower()    minusculas
#capitalize() primera letra en mayusculas
#count()    cuenta letra o cadena dentro de texto
#find()     posicion que aparece un caracter
#isdigitl() devuleve buleano
#isalum()   si son alfanumericos
#isalpha()  si son solo letras
#split()    separa palabras usando espacios
#strip()    borra espacios principio y final    
#replace()  cambia una letra por otr en un string
#rfind      reprecenta el indice de un caracter de derecha a izquierda
# www.pyspanishdoc.sourceforge.net  metodos de cadenas

#nombreUsuario=input("Introduce tu nombre de usuario:")
#print("El nombre es: ", nombreUsuario.capitalize())

#objeto.metodo

edad=input("Introduce tu edad de usuario:")

while(edad.isdigit()==False):
    print("Por favor introduce un valor numerico    ")
    edad=input("Introduce tu edad de usuario:")

if (int(edad)>18):
    print("Puede pasar")
else:
    print("No pasa")






    