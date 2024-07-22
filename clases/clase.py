#clase - estado - propiedades - comportamiento(metodos)

#clase coche tiene 4 propiedades
#clase coche tiene 2 comportamientos arranca y estado

class Coche():
    largochasis = 550
    anchochasis=160
    ruedas=4
    enmarcha=False

    def arrancar(self):  
        self.enmarcha=True
    
    def estado(self):
        if self.enmarcha:
            return("El coche esta en marcha")
        else:
            return("El coche esta parado")

#instanciacion de clase -ejemplarizar la clase
#crear objeto

miCoche=Coche()

print("El largo del coche es:",miCoche.largochasis)
print("El coche tiene",miCoche.ruedas, "ruedas")
miCoche.arrancar()
print(miCoche.estado())







