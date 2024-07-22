#de cadena crear una lista - split por default separador es espacio
cursos= 'Java Python Angular Spring Excel'
lista_cursos= cursos.split()
print(f'lista_crusos: {lista_cursos}')


#de cadena crear una lista - split usando separador coma
cursos_separados_coma='Java,Python,Angular,Spring,Excel'
lista_cursos= cursos_separados_coma.split(',')
print(f'lista_crusos2: {lista_cursos}')

#de cadena crear una lista - split usando separador coma + max_split
cursos_separados_coma='Java,Python,Angular,Spring,Excel'
lista_cursos= cursos_separados_coma.split(',', 2)
print(f'lista_crusos2: {lista_cursos}')
#solo se va a separar 2 elementos, el resto queda todo junto



