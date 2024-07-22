from class_Figurageometrica import FiguraGeometrica
from class_Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        # cuando tengo dos clases padre (Nombre clase + __init__(self, atributos))
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

    def calcular_area(self):
        return self.ancho * self.alto


        