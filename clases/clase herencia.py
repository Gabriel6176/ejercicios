#clase - herencia
#abuelo (clase 1) - hijo (Clase 2) - nieto X 3 (clase 3 - clase 4 - clase 5)
#casa - moto - nada
# caracteristica - comportamiento


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

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    ## esta parte sobre escribe el metodo "estado" de arriba
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enmarcha,"\nAcelera:", self.acelera,"\nFrena:", self.frena, "\n" ,self.hcaballito)

class Quad(Moto):
    pass

class Furgoneta(Vehiculos):
   
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class VElectricos():
    def __Init__(self):
        self.autonomia=100

    def cargarenergia(self):
        self.cargando=True
    
miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Ford", "F350")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)

class BicicletaElectrica(VElectricos, Vehiculos):  ##da prioridad primero a VElectricos y luego Vehiculos
        pass

miBici=BicicletaElectrica("Marca", "Modelo")   
#debemos dejar vacio
    
    


