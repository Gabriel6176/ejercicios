class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada=tipo_entrada
        self._marca=marca

    def __str__(self):
        return f'Entrada: {self._tipo_entrada}, Marca: {self._marca}'

    @property
    def tipo_entrada(self):
        print('Llamando metodo get')
        return self._tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        print('Llamando metodo set')
        self._tipo_entrada = tipo_entrada    

    @property
    def marca(self):
        print('Llamando metodo get')
        return self._marca

    @marca.setter
    def marca(self, marca):
        print('Llamando metodo set')
        self._marca = marca

        