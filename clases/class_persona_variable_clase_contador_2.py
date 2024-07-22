

class Persona:
    contador_personas=0

    #si quiero que classmethod no se use desde afuera el tengo que poner "def _generar_siguinete(cls):"
    @classmethod
    def generar_siguiente(cls):
        cls.contador_personas+=1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona}, {self.nombre}, {self.edad}]'

persona1=Persona('Juan', 28)
print(persona1)
persona2=Persona('Carla', 20)
print(persona2)
persona3=Persona('Pepo', 30)
print(persona3)
# puedo generar siguiente valor sin consignar persona
Persona.generar_siguiente()
#como incremente el valor en uno la persona 4 tiene el numero 5
persona4=Persona('Maria', 30)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')


