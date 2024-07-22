#243 funcion closure

#Es una funcion que define a otra y ademas la va a regresar

def operacion(a, b):
    #definimos funcion interna anidada
    def sumar():
        return a+b
    
    return sumar

#opcion1
mi_funcion_closure=operacion(5,2)
print(mi_funcion_closure())
#7

#opcion2
print(f'{operacion(5,3)()}')
#8