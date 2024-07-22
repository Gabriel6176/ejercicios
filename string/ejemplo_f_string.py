nombre='Juan'
edad='28'
sueldo=5000

#incluso entre corchete podria mandar a llamar una funcion para que complete el dato
mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
print(mensaje)

#metodo print puede dar formato
print(nombre, edad, sueldo)

#si quiero separar los elementos por coma y espacio
print(nombre, edad, sueldo, sep=', ')

