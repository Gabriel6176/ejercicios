import math

numero = int(input("Ingrese el numero para calcular raiz cuadrada: "))
intentos = 0

while numero<0:
    print("No tiene raiz un numero negativo")
    
    if intentos==2:
        print("Intentates muchas veces, adios")
        break;
   
    numero = int(input("Ingrese el numero para calcular raiz cuadrada: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print(str(solucion))