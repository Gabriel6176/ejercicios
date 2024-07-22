class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre=nombre
        self.sueldo=sueldo
    def __str__(self):
        return f'[Nombre: {self.nombre} Sueldo: {self.sueldo}]'

    #llama metodo str de clase padre
    def mostrar_detalles(self):
        return self.__str__()

