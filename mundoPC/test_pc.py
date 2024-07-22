from teclado10 import Teclado
from raton10 import Raton
from monitor10 import Monitor
from computadora10 import Computadora
from orden10 import Orden

monitor1=Monitor('HP', 15)
teclado1=Teclado('usb', 'Acer')
raton1=Raton('bluetooth', 'HP')
computadora1=Computadora('HP', monitor1, teclado1, raton1)
#print(computadora1)

monitor2=Monitor('Acer', 21)
teclado2=Teclado('usb1', 'HP')
raton2=Raton('usb2', 'Asus')
computadora2=Computadora('Bangoo', monitor2, teclado2, raton2)
#print(computadora2)

teclado3=Teclado('usb', 'gamer')
raton3=Raton('usb','picho')
monitor3=Monitor('PachaCardozo', 32)
computadora3=Computadora('Gamer', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1=Orden(computadoras1)
print(orden1)

orden1.agregar_computadora(computadora3)
print(orden1)

