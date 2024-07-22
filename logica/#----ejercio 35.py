#----ejercio 35

edad=int(input('Proporciona tu edad: '))
mensaje=None

try:
    if 0<edad<=10:
        mensaje='Tu edad es de joven'
        print(f'{mensaje}')
    elif 10<edad<=20:
        mensaje='Tu edad es de adolescente'
        print(f'{mensaje}')
    elif 20<edad<=30:
        mensaje='Tu edad es de adulto'
        print(f'{mensaje}')
    else:
        mensaje='Estas fuera de rango'
        print(f'{mensaje}')
except Exception as e:
    print(e)

    
