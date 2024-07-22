#212 

#indice de una lista
numeros1=[10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')


#obtener el indice del primer valor
print(f'Indice 4: {numeros1.index(4)}')
#devuelve el valor 3 - el 0 es 10, el 1 es 40, el 2 es 14 y 3 es 4.
#devuelve el primer valor encontrado

numeros1.reverse()
print(f'Lista invertida: {numeros1}')

#orden ascendente
numeros1.sort()
print(f'Ordenada ascendente: {numeros1}')

#orden descendente
numeros1.sort(reverse=True)
print(f'Ordenada descendente: {numeros1}')





