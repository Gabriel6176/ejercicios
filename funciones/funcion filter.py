##---------------funcion filter----------------------------

#def numero_par(num):
#    if num % 2==0:
#        return True

#-----------ejemplo de lambda con filter en una linea------
#from mailbox import NoSuchMailboxError

#numeros=[3,344,35,38,36,29,48,65]

#print(list(filter(lambda numero_par: numero_par%2==0, numeros)))

##-------------------ejemplo empleado-----------------------

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}€".format(self.nombre, self.cargo, self.salario)


listaEmpleados=[
Empleado("Juan", "Director", 75000),
Empleado("Ana", "Presidenta", 85000),
Empleado("Antonio", "Administrativo", 25000),
Empleado("Sara", "Secretario", 27000),
Empleado("Mario", "Botones", 21000),
]

salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)
    






