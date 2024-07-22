from mi_clase import MiClase

print(MiClase.__doc__)
#va a devolver el texto "Informacion"

print(MiClase.__init__.__doc__)
#va a devolver la documentacion/el texto "texto init"

print(MiClase.mi_metodo.__doc__)
#va a devolver la documentacion/el texto "texto mi metodo"
#si huvier puesto print(MiClase.mi_metodo().__doc__) estaria ejecutando el metodo

print(type(MiClase.mi_metodo))
#me dice que tipo de objeto es mi_metodo, el cual esta dentro de MiClase

#------------------------------
mensaje = 'hola' + 'Mundo'
print(mensaje)

#es igual a 
mensaje= 'hola' 'mundo'
print(mensaje)

#concatenando cadenas con variables
variable= 'aqui'
mensaje= 'hola' 'mundo' + variable
print(mensaje)

#concatenando cadenas con variables + nueva informacion
variable= 'aqui'
mensaje= 'hola' 'mundo' + variable
mensaje += 'estoy yo'
print(mensaje)

#solicito ayuda de la clase - esta dentro de python
#clase object es la clase madre de todos los objetos
#capitalize es una funcion dentro de la clase str
help(str)
help(str.capitalize)
help(math)

