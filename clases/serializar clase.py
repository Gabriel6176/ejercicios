import pickle



class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enmarcha,"\nAcelera:", self.acelera,"\nFrena:", self.frena)

coche1=Vehiculos("Seat", "Leon")
coche2=Vehiculos("Ford", "Focus")
coche3=Vehiculos("Renault", "Clio")

coches=[coche1, coche2, coche3]

fichero=open("lista_coches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)


ficheroapertura=open("lista_coches", "rb")
listado=pickle.load(ficheroapertura)
ficheroapertura.close()

for c in listado:
    print(c.estado())



