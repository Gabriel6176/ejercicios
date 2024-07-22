from datetime import datetime
from Empleado09 import Empleado
from Gerente09 import Gerente



def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    # si quiero saber si el objeto es de clase hija de clase padre empleado que imprima xx
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado=Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente =Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)
