class MiClase:
    variable_clase="Valor Estatico"

    def __init__(self, variable_instancia):
        self.variable_instancia=variable_instancia
    
    @staticmethod
    #esto es estatico de la clase y no puede acceder a las variable_instancia
    def metodo_estatico():
        print(MiClase.variable_clase)
        #tampoco puedo usar la variable de clase directamente ejemplo "print(mi_variable)"

    @classmethod
    def metodo_clase(cls):
        #con cls uso las variables de clase
        print(cls.variable_clase)

    #desde metodo de instancia puedo acceder al contexto @estaticmethod y de @clasmethod
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()


MiClase.metodo_estatico()
Objeto1=MiClase('variable instancia 1')
Objeto1.metodo_clase()




