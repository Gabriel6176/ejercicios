
from mailbox import NoSuchMailboxError


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad =edad
    #el decorador properti me permite entrar a nombre de forma indirecta
    @property
    def nombre(self):
        print('Llamando metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando metodo set')
        self._nombre = nombre


persona1 = Persona('Juan', 'Perez', 28)
print(persona1._nombre, persona1.apellido, persona1.edad)
persona1.nombre = 'Juan Carlos'

print(persona1.nombre, persona1.apellido, persona1.edad)

