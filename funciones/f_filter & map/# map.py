# funcion map

import math

#la funcion map(funcion, iterable)
# ejecuta la funcion usando como parametro cada elemento del iterable

palabras= ('dale', 'un', 'buen', 'like', 'y', 'suscribete')
longitudes=list(map(lambda palabra: len(palabra), palabras))
print(longitudes)

eje_x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eje_xx=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#redondeo a 2 decimales con round(),2 
eje_y= list(map(lambda x, y: round(math.cos(x) + math.exp(y),2), eje_x, eje_xx))
