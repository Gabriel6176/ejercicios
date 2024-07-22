#clase coche- estado - propiedades - comportamiento(metodos)
#dos instancias miCoche1 y miCoche2
#2 metodos arranca - estado
#clase coche tiene 4 propiedades
#clase coche tiene 2 comportamientos arranca y estado

#
# Hay que generar un constructor inicial del objeto
#

class Coche():

    def __init__(self):
        self.__largochasis = 550
        self.__anchochasis=160
        self.__ruedas=4    #se encapsula con "__" y no se puede cambiar desde fuera
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo fue mal en el chequeo no se ha podido arrancar"
        else:
            return "El coche esta parado"
    
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de", self.__anchochasis, "y un largo de", self.__largochasis )

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="OK"
        self.aceite="OK"
        self.puertas="Cerradas"
        
        if(self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="Cerradas"):
            return True
        else:
            return False

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

