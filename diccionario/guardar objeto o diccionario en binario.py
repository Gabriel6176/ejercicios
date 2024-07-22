import pickle

#dump() es guardar
#load() es levantarla desde afuera

#lista_nombres=["predro", "ana", "maria", "isabel"]
#fichero_binario=open("lista_nombres","wb")
#write binary
#pickle.dump(lista_nombres, fichero_binario)
#fichero_binario.close()
#del (fichero_binario) #lo borra de la memoria

#importar y leer lista binaria
fichero=open("lista_nombres", "rb")
lista=pickle.load(fichero)
print(lista)









