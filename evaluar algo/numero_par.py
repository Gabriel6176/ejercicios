from operator import mod


a=int(input('Por favor ingresa un numero entero para saber si es PAR o IMPAR: '))
if a % 2 == 0:
    print(f'El numero {a} es par')

else:
    print(f'El numero {a} es impar')