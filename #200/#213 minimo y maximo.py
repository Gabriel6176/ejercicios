#213 minimo y maximo

#indice de una lista
numeros1=[10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')


# obtener valor minimo y maximo
print(f'Minimo:{min(numeros1)}')
print(f'Maximo:{max(numeros1)}')

#copiar elementos de una lista
numeros2=numeros1.copy()
print(numeros1)
print(numeros2)

#Opcion 1 de copia
#no es el mismo objeto es otro objeto
print(f'Es la misma referencia_1? {numeros1 is numeros2}')
#respuesta False
print(f'Es misma contenido_1? {numeros1 == numeros2}')
#respuesta True
#---------------------------------
#Opcion 2 de copia
#podemos usar constructor
numeros2= list(numeros1)
print(f'Es la misma referencia_2? {numeros1 is numeros2}')
print(f'Es misma contenido_2? {numeros1 == numeros2}')

#----------------------------------
#Opcion 3 de copia - slicing - al dejar vacio antes y desp de : es que recorro de inicio a fin
numeros2 = numeros1[:]
print(f'Es la misma referencia_3? {numeros1 is numeros2}')
print(f'Es misma contenido_3? {numeros1 == numeros2}')
#-------------------------------------
