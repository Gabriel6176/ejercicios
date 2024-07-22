from dispositivoEntrada10 import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRaton=0
    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada,marca)
        Raton.contadorRaton+=1
        self._idRaton=Raton.contadorRaton
        
        
    def __str__(self):
        return f'id: {self.idRaton} {super().__str__()}'

    @property
    def idRaton(self):
        #print('Llamando metodo get')
        return self._idRaton

    @idRaton.setter
    def id_Raton(self, idRaton):
        #print('Llamando metodo set')
        self._idRaton = idRaton    



    