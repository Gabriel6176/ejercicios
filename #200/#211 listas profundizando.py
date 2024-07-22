#211 listas profundizando
#las listas son mutables
#sumandos dos listas


#puedo escribir una lista con corechetes
nombres1=['Juan', 'Karla', 'Pedro']
print(nombres1)

#puedo escribir una lista sin corchetes
nombres2 = 'Laura Maria Gonzalo Ernesto'.split()

#sumando listas
print(f'Sumas listas {nombres1+nombres2}')

#extender una lista con otra lista
nombres1.extend(nombres2)
print(nombres1)


