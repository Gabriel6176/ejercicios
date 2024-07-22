#bucle for
#for VARIABLE in ELEMENTO A RECORRER(lista, tupla, cadena de texto)
#   cuerpo bucle

## for i in ["primavera","verano","otoño","invierno"]:
##   print(i, end=" ")
    #si quiero que lo imprima uno al lado del otro - print(i, end="")
    #si quiero que lo imprima uno al lado del otro con espacio entre palabras - print(i, end=" ")

#esto solo lo va hacer 4 veces porque la lista es de 3 elementos    
#el programa hace, i=primavera despues i=verano despues i=otoño depues i=invierno

email = False
for i in "gaby@gmail.com":
    if(i=="@"):
        email = True

if email == True:   # tambien puedo poner "if email:" es lo mismo
    print("El email es correcto")

else:
    print("El email es incorrecto")


