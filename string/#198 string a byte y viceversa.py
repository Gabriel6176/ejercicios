#198 string a byte y viceversa

string= 'Programación con Python'
print('string original:', string)
#imprime: string original: Programacion con Python

byte=string.encode('UTF-8')
print('string codificado:', byte)
#imprime: string codificado: b'Programaci\xc3\xb3n con Python'

string2= bytes.decode('UTF-8')
print('string decodificado:, string2')
#imprime: string decodificado: Programación con Python'

#si quiero saber si la cadena string es la misma que string2
print(string == string2)
#devuelve valor True
