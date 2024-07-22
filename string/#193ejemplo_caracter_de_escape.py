#193

#caracter de escape "\"
resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')
#imprime: Resultado: Hola ' Mundo

#usando \b - esto elimina el caracter a izquierda
#puedo usar varios \b\b\b\b
resultado = 'Hola Mundo xxx\b\b\b'
print(f'Resultado: {resultado}')
#imprime: Resultado: Hola Mundo

#si quiero usar e imprimir '\' debo imprimir dos veces '\\'
resultado = 'Hola \\ Mundo'
print(f'Resultado: {resultado}')
#imprime : Resultado: Hola \ Mundo

#raw string - no me da problema los caracteres especiales
resultado = r'Cadena con \n saldo de linea'
print(f' Resultado: {resultado}')
#imprime: Resultado: Cadena con \n saldo de linea

