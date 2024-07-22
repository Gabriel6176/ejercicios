tupla_str=('Hola Mundo', 'Universidad', 'Python')
mensaje = ','.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular']
mensaje= ', '.join(lista_cursos)
print(f'Lista Cursos: ', {mensaje})

#separa los caracteres por un punto
cadena = 'HolaMundo'
mensaje= '.'.join(cadena)
print(f'mensaje', {mensaje})

diccionario = {'nombre':'Juan', 'apellido':'Perez', 'edad':'18'}
llaves='-'.join(diccionario.keys())
valores='-'.join(diccionario.values())
print(f'llaves:' {llaves}, type: {type(llaves)])
print(f'valores:' {valores}, type: {type(valores)])


