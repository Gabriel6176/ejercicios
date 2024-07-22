#242 lambda
#funcion lambda - funcion anonima - solo una linea

#es una funcion anonima y una linea de codigo
# no debo agregar parentesis para funcion landa
# tampoco uso la palabra return

mi_funcion_lambda=lambda a, b: a + b 
print(mi_funcion_lambda(4,5)) 
#9

funcion_lambda_sin_argumentos=lambda: 'Funcion sin argumentos'
print(f'Resultado_0: {funcion_lambda_sin_argumentos()}')
#Resultado_0: Funcion sin argumentos

#funcion con parametros por default
funcion_lambda=lambda a=2, b=3: a+b
print(f'Resultado_1: {funcion_lambda()}')

#funcion lambda con argumentos variables *args y **kwargs
funcion_lambda_1=lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado_2: {funcion_lambda_1(1,2,3, a=2,b=3)}')
#Resultado_2: 5 ya que son 5 elementos 3 de arg y 2 de kwargs

#funciones con argumentos variables y valores por default
mi_funcion_lambda_2=lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado_3: {mi_funcion_lambda_2(1,2,3, 6,7,8, f=3,d=5)}')
#Resultado_3: 11   (1+2+3+3+2) 1+2 +3 +3(es 6/7/8), 2(es fyd)

