#herencia - un objeto de la subclase es siempre un objeto de la clase principal
#isinstance


class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "Lugar de residencia:", self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario, "Antiguedad:", self.antiguedad)

Manuel=Persona("Manuel", 55, "Colombia")

Manuel.descripcion()

print(isinstance(Manuel, Empleado))
## aca valudo que manuel no es empleado pero si persona



