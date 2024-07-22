class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    #si no creo este metodo cuando llame desde ortro archivo el nombre y edad de la clase persona me va a devolver una direccion de memoria
    def __str__(self):
        return f'Persona: {self.nombre} y Edad {self.edad}'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        #con eso inicializo para acceder a la clase padre
        super().__init__(nombre, edad)
        self.sueldo=sueldo

    #si no agrego esta definicion no voy a poder acceder al sueldo desde afuera
    #con el super llamo al str de la clase padre
    def __str__(self):
        return f'Empleado {super().__str__()} Sueldo {self.sueldo}'

#empleado1=Empleado('Juan', 28, 50000)
#print(empleado1.nombre)
#print(empleado1.edad)
#print(empleado1.sueldo)


