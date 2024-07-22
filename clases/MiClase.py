
# si creo una variable antes del def __init__ esta sera,
# una variable de clase

class MiClase:
    #aca creo un valor para la variable de clase
    variable_clase='Valor variable Clase'
    
    def __init__(self, variable_instancia):
        self.variable_instancia=variable_instancia


print(MiClase.variable_clase)

#aca creo un valor para la variable de instancia
miclase1=MiClase('Valor variable Instancia')

print(miclase1.variable_instancia)

#desde el objeto puedo acceder al valor de 
# variable de clase que es unico para todos los objetos

print(miclase1.variable_clase)

miclase2=MiClase('Otro Valor variable Instancia')
print(miclase2.variable_instancia)
print(miclase2.variable_clase)