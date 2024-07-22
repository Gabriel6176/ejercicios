from class_Cuadrado import Cuadrado
from class_Rectangulo import Rectangulo


print('Creacion de objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5,'rojo')
#con estas dos lineas que siguen le doy nuevo valor despues de haberlo creado pero dentro de rango permitido
cuadrado1.alto = 9
cuadrado1.ancho = 9
#------------------------------
print(f'Calculo area del Cuadrado es: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creacion de objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(9, 8,'verde')
#con estas linea que sigue le doy nuevo valor despues de haberlo creado pero fuera de rango permitido
#por eso no lo usa al momento de hacer el calculo, usa los primeros que estaban bien dentro rango
rectangulo1.alto=15
print(Cuadrado.mro())

#--------------------
print(f'Calculo area del Rectangulo es: {rectangulo1.calcular_area()}')
print(rectangulo1)
print('Fin'.center(50,'-'))

#esto sirve para ver como se va ajecutando el orden Method Resolution Order
#print(Cuadrado.mro())