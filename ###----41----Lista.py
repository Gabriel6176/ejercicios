###----41----Lista

nombres = ['Juan', 'Carla', 'Ricardo', 'Maria']

#print(nombres[0])
#print(nombres[1])
###--- para ver el ultimo nombre de la lista
#print(nombres[-1])

###-----preguntar el largo de una lista
print(len(nombres))

nombres.append('Lorenzo')
print(nombres)
#-------------------------
#insertar un nuvo elemento en un lugar
nombres.insert(2,'Octavio')
print(nombres)

#--------elimina el ultimo item 
#nombre.pop()

#-------borrar un item----
del nombres[3]

##--------borrar todos los elementos
nombres.clear()

##--------