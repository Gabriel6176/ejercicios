#205 replace y quitar caracteres

titulo="El sitio web mas imoportante de mundo"

print(titulo.replace(' ',"-"))
#reemplaza todos los espacios por un "-" o el caracter que le indique

#permite eliminar caracteres al inicio y final de una cadena
titulo2=" ***El sitio web mas imoportante de mundo*** "
print(titulo2)
#imprime:  ***El sitio web mas imoportante de mundo*** -tiene un espacio al inicio y final 

titulo2=titulo2.strip()
print(titulo2)
#imprime: ***El sitio web mas imoportante de mundo*** - quito el espacio a inicio y final

titulo2=titulo2.strip('*')
print(titulo2)
#imprime: El sitio web mas imoportante de mundo

titulo3="***El sitio web mas imoportante de mundo***"
titulo3=titulo3.lstrip('*')
print(titulo3)
#imprime: El sitio web mas imoportante de mundo*** - quito asteriscos a izquierda

titulo4="1 ***El sitio web mas imoportante de mundo*** 1".strip("1").strip()
print(titulo4)
#quito el 1 y despues el espacio, pordria poner .strip(*) y quitar los asteriscos


