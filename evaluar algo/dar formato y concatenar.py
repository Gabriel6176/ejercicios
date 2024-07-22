## funciones

def mi_funcion(num1, num2):
    print(num1+num2)
mi_funcion(3, 4)

# *algo es una tupla
def mi_funcion(cad, v=2, *algo):
    print(cad * v)
    for cadena in algo:
        z = 3
        print(cadena * z)
        
mi_funcion("Hola", 5, "hola", "Como", "Estas")

# si pongo **algo eso sera un diccionario



  
    

