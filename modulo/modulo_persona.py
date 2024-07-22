

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    #el decorador properti me permite entrar a nombre de forma indirecta
    @property
    def nombre(self):
        print('Llamando metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Llamando metodo get1')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print('Llamando metodo set1')
        self._apellido = apellido

    @property
    def edad(self):
        print('Llamando metodo get2')
        return self._edad

    @edad.setter
    def edad(self, edad):
        print('Llamando metodo set2')
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    print(persona1._nombre, persona1._apellido, persona1._edad)
    persona1.nombre = 'Juan Carlos'
    print(persona1.nombre, persona1.apellido, persona1.edad)
    persona1.apellido='Lara'
    persona1.edad=30
    persona1.mostrar_detalle()

    print(__name__)