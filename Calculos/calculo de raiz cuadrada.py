## programa calculo de raiz cuadrada

import math

numero = int(input("Por favor ingresa el numero a calcular raiz cuadrada: "))

intentos = 0

while numero<0:
    print("El numero ingresado es negativo y no tiene raiz cuadrada")
   
    if intentos == 2:
        print("El numero de intentos fueron demasiados. El calculo será finalizado")
    
    numero = int(input("Por favor ingresa el numero a calcular raiz cuadrada: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=round(math.sqrt(numero), 3)   #redondea a 3 decimales
    print("La raiz de el " + str(numero) + " es " + str(solucion))


