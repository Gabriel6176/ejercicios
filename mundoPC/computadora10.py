from teclado10 import Teclado
from raton10 import Raton
from monitor10 import Monitor


class Computadora:
    contadorComputadora=0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadora+=1
        self.idComputadora=Computadora.contadorComputadora
        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton
        

    def __str__(self):
        return f'''
        {self._nombre}: {self.idComputadora} 
        Monitor: {self._monitor} 
        Teclado: {self._teclado} 
        Raton: {self._raton}
        '''

    @property
    def nombre(self):
        #print('Llamando metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        #print('Llamando metodo set')
        self._nombre = nombre    
    
    @property
    def monitor(self):
        #print('Llamando metodo get')
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        #print('Llamando metodo set')
        self._monitor = monitor

    @property
    def teclado(self):
        #print('Llamando metodo get')
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        #print('Llamando metodo set')
        self._teclado = teclado    
    
    @property
    def raton(self):
        #print('Llamando metodo get')
        return self._raton

    @raton.setter
    def raton(self, raton):
        #print('Llamando metodo set')
        self._raton = raton    

