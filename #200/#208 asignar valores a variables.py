#208 asignar valores a variables

valores=1,2,3
print(valores)
#(1, 2, 3)
print(type(valores))
#<class 'tuple'>

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)
# 1 2 3

valor1, _, valor3 = 1, 2, 3
print(valor1)
#1
print(_)
#2
print(valor3)
#3

#lo que hace el * adelante de valor3 es asignarles del 3 en adelante
valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)
#1 2 [3, 4, 5, 6, 7, 8, 9]

#lo que hace el * adelante de valor3 es asignarles del 3 en adelante, y los dos finales se los asigna a valor4 y valor5
valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)
#1 2 [3, 4, 5, 6, 7] 8 9
