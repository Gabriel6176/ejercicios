class Monitor:
    contadorMonitor=0
    def __init__(self, marca, tamano):
        Monitor.contadorMonitor+=1
        self._idMonitor=Monitor.contadorMonitor
        self._marca=marca
        self._tamano=tamano

    def __str__(self):
        return f'id: {self._idMonitor} Marca: {self._marca} Tamaño: {self._tamano}'

    @property
    def idMonitor(self):
        print('Llamando metodo get')
        return self._idMonitor

    @idMonitor.setter
    def idMonitor(self, idMonitor):
        print('Llamando metodo set')
        self._idMonitor = idMonitor

    @property
    def marca(self):
        print('Llamando metodo get')
        return self._marca

    @marca.setter
    def marca(self, marca):
        print('Llamando metodo set')
        self._marca = marca
    
    @property
    def tamano(self):
        print('Llamando metodo get')
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        print('Llamando metodo set')
        self._tamano = tamano

    


