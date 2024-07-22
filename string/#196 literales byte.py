#196 / 197

#Literales tipo byte

caracteres_en_bytes = b'Hola Mundo'

print(caracteres_en_bytes)
#resultado: b'Hola Mundo'

mensaje = b'Universidad Python'
print(mensaje[0])
#imprime: 85 - que es la U en byte
print(chr(mensaje[0]))
#imprime U

lista_caracteres=mensaje.split()
print(lista_caracteres)
#imprime: [b'Universidad', b'Python']
