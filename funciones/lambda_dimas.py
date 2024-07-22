#lambda son funciones anonimas
#permite multiples argumentos
#solo permite una sola expresion
#Estructura: lambda arg1, arg2, argx: expresion


#ejemplo_1
suma= lambda a, b: a+b
print(suma(5,5))
print(suma(3,2))

saludar=lambda nombre: print(f'Hola {nombre}')
saludar("Juan")

#ejemplo_2
maximo = lambda a, b, c: f'El maximo es: {a}, {b}, {c} es {max(a,b,c)}'
print(maximo(3,4,5))

#ejemplo_3
#puedo usarla dentro de funciones

def poner_prefijo(prefijo):
    return lambda nombre: f"{prefijo} {nombre}"

addMr = poner_prefijo("Mr")    
addSr = poner_prefijo("Sr")
addMiss = poner_prefijo("Miss")

print(addMr("Juan"))
print(addSr("Julian"))
print(addMiss("Nerea"))

#ejemplo 4
def elevarA(exponente):
    return lambda base: base**exponente

elevarCuadrado=elevarA(2)
elevarCubo=elevarA(3)

print(elevarCuadrado(4))
print(elevarCubo(3))