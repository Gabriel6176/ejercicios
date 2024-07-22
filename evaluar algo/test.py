#clase - estado - propiedades - comportamiento(metodos)
#clase coche tiene 4 propiedades
#clase coche tiene 2 comportamientos arranca y estado

class Coche():
    largochasis = 550
    anchochasis=160
    ruedas=4
    enmarcha=False

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if self.enmarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
    
    def estado(self):
        print("El coche tiene ", self.ruedas, "ruedas. Un ancho de", self.anchochasis, "y un largo de", self.largochasis )

#instanciacion de clase -ejemplarizar la clase
#crear objeto

miCoche=Coche()

## necesitamos ponerle argumento
print(miCoche.arrancar(True))
miCoche.estado()

print("----------Segundo Obejeto-------------------")
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()





