from class_Rectangulo import Rectangulo

rectangulo1 = Rectangulo(5, 10, 'verde')
print(f'El area del rectangulo es: {rectangulo1.calcular_area()} {rectangulo1}')

#esto sirve para ver como se va ajecutando el orden Method Resolution Order
print(Rectangulo.mro())