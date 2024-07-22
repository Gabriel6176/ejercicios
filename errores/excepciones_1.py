from numerosidenticos import NumerosIdenticosException

resultado=None
try: 
    a=int(input('Primer Numero: '))
    b=int(input('Segundo Numero: '))
    if a == b:
        raise NumerosIdenticosException('Numeros Identicos')
    resultado=a/b

except ZeroDivisionError as e:
    print(f'ZeroDiv - Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'Type - Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
#se ejecuta si no hay excepciones
else:
    print('No hubo excepciones')
#este bloque siempre se ejecuta
finally:
    print('Fin del proceso - finally')

print(f'Resultado: {resultado}')
print(f'Continuamos...')

