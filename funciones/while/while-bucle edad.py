
#bucle while

edad=int(input("Por favor dinos tu edad: "))

i=1
while edad<5 and i<5 or edad>100 and i<5:
    print("Introdujiste una edad fuera de rango confiable, vuelve a intentarlo") 
    edad=int(input("Por favor dinos tu edad: "))
    i=i+1

print("La edad el aspitrante es " + str(edad))
print("Gracias")

