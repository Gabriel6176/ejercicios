#241 leccion

#poner una funcion como argumento
a=5
b=3

def sumar(a, b):
    return a+b
#1 Asignar una funcion a una variable
mi_funcion=sumar

#llamamos a la funcion desde una variable
print(mi_funcion(4,6))

#miro que tipo de variable es
print(type(mi_funcion))
#<class 'function'> No me dice que es una variable(int,float,str)

#2 Funcion como argumento
def operacion(a,b,sumar_arg):
    print(f'resultado sumar: {sumar_arg(a,b)}')

#aca estoy mandando los parametros 4 y 5 a operacion y llamando a sumar
operacion(4, 5, sumar)
# resultado sumar: 9

#3 retornar funcion
def retornar_funcion():
    return sumar

mi_funcion_retornada=retornar_funcion()
print(f'resultado de funcion retornada: {mi_funcion_retornada(5,7)}')
#resultado de funcion retornada: 12