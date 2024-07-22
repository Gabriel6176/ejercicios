#206

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido}'

#esto quiere decir que solo se ejecutra si se lo llama desde la clase/archivo
if __name__ == '__main__':
    persona1=Persona('Juan', 'Perez')
    print(persona1)

