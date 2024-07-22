from dispositivoEntrada10 import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclado=0
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada,marca)
        Teclado.contadorTeclado+=1
        self._idTeclado=Teclado.contadorTeclado
        
        
    def __str__(self):
        return f'id: {self.idTeclado}, {super().__str__()}'

    @property
    def idTeclado(self):
        #print('Llamando metodo get')
        return self._idTeclado

    @idTeclado.setter
    def id_Teclado(self, idTeclado):
        #print('Llamando metodo set')
        self._idTeclado = idTeclado  



