#ABC Abstract Base Class
from abc import ABC, abstractmethod

#cuando creo clase abstracta obligo a las hijas a que implementen 
# ejemplo "def calcular_area()" si o si

#si saco el metodo @ancho.setter no podre asignarle 
# nuevo valor una vez iniciado el objeto ej:cuadrado1


#aca le agrego entre parentesis (ABC)
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        #estas son validaciones al momento de crear el objeto
        if self._validar_valor(ancho):
            self._ancho=ancho
        else:
            self._ancho=0
            print(f'Valor erronero ancho: {ancho}')
        if self._validar_valor(alto):
            self._alto=alto
        else:
            self._alto=0
            print(f'Valor erronero alto: {alto}')
   
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self,ancho):
        if self._validar_valor(ancho):
            self._ancho=ancho
        else:
            print(f'Valor erronero ancho: {ancho}')
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self,alto):
        if self._validar_valor(alto):
            self._alto=alto
        else:
            print(f'Valor erronero alto: {alto}')
    
    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self.ancho} Alto: {self.alto}]'
    
    @abstractmethod
    def calcular_area(self):
        pass

    # uso el _ para que no se pueda acceder desde fuera de la clase y lo uso en el def __init__
    #para hacer la validacion desde la creacion del objeto
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

    


        

