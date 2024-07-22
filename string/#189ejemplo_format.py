#clase 189

#usando place holders

nombre='Juan'
edad='28'
sueldo=3000
mensaje_con_formato= 'Nombre {} Edad {} Sueldos{:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje= 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre,edad,sueldo)
print(mensaje)

#cuando quiero alterar el orden de como los nombro y los uso
#al poner el indice entre los corchetes evito errores
mensaje= 'Sueldo {2:.2f} Nombre {0} Edad {1}'.format(nombre,edad,sueldo)
print(mensaje)

#cuando a los indices le asigno letras y no numeros
mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)

#usando diccionario
diccionario = {'nombre':'ivan', 'edad':'38', 'sueldo':'8000'}
mensaje='Nombre {nn[nombre]} Edad {nn[edad]} Sueldo {nn[sueldo]:.2f}'.format(nn=diccionario)
print(mensaje)






