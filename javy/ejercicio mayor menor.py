#ejercicio mayor menor

num1=int(input('Ingresa el numero 1:'))
num2=int(input('Ingresa el numero 2:'))
num3=int(input('Ingresa el numero 3:'))

lista=[num1,num2,num3]
lista.sort()
res=num1+num2+num3

if (res)<10:
    print(f'El numero es: {lista[0]}')
elif 10<(res)<15:
    print(f'El numero es: {lista[1]}')
elif res>15:
    print(f'El numero es: {lista[2]}')


