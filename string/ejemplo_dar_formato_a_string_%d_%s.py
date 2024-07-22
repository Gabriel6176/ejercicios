nombre='Juan'
edad=28

#%s = string y %d = numero
mensaje_con_formato= 'Mi nombre es %s y tengo %d años '%(nombre,edad)
print(mensaje_con_formato)

# cuando uso %.2f significa dos decimales flotante
persona=('Karla', 'Gomez', 5000)
mensaje_con_formato= 'Hola %s %s.Tu sueldo es %.2f'%persona
print(mensaje_con_formato)

#otra opcion es
persona=('Karla', 'Gomez', 5000)
mensaje_con_formato= 'Hola %s %s.Tu sueldo es %.2f'
print(mensaje_con_formato%persona)




