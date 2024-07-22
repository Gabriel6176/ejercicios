dato_seg = int(input(print("Por favor ingresar el numero de segundos: ")))

if dato_seg = str:
    print("El Dato ingresado es incorrecto intente nuevamente.")
    dato_seg = int(input(print("Por favor ingresar el numero de segundos: ")))

hora = int(dato_seg/60/60)
dato_seg -= hora*60*60
minutos = int(dato_seg/60)
dato_seg -= minutos*60
segundos = int(dato_seg)

print("\tLa Duracion en hh:mm:ss es:",f"{hora}:{minutos}:{segundos}")


