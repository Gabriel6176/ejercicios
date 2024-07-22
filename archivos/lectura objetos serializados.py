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


ficheroapertura=open("lista_coches", "rb")
listado=pickle.load(ficheroapertura)
ficheroapertura.close()

for c in listado:
    print(c.estado())

