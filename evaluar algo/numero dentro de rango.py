#-----ver si el numero esta dentro de un rango---

a=int(input('Ingrese un numero:'))
valor_minimo=0
valor_maximo=5

dentro_rango=a>=valor_minimo and a<=valor_maximo

if dentro_rango==True:
    print(f'El valor {a} esta dentro del rango definido')
else:
    print(f'El valor {a} esta fuera del rango definido')

#-------------------------------------------------
