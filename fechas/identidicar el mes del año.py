
mes=int(input('Indica el mes del año: '))

estacion=None

if mes == 1 or mes == 2 or mes == 12:
    print('La estacion es Invierno')

elif mes == 3 or mes == 4 or mes == 5:
    print('La estacion es Preimavera')

elif mes == 6 or mes == 7 or mes == 8:
    print('La estacion es Verano')

elif mes == 9 or mes == 10 or mes == 11:
    print('La estacion es Otoño')

else:
    print('El valor ingresado es incorrecto')



    