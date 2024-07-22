#194
#Python usa caracter unicode

# \u0020 es espacio en blanco

print('Hola\u0020Mundo')
#resuldado: Hola Mundo

print('\u0041')
#resuldado: A

#esta es notacion extendida -completo con ceros a la izquierda
print('\U00000041')
#resuldado: A

#esto es hexdecimal solo p/cuando tiene 2 caracteres la notacion
print('\x41')
#resuldado: A

#puedo usar iconos con unicode
print('\u2665')
#resuldado: dibujo_corazon


