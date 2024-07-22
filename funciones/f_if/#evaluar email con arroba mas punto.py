#evaluar email con arroba mas punto

contador=0
email = input("ingresa tu email:")

for i in email:
    if (i=="@" or i=="."):
        contador=contador+1

if contador == 2:
    print("email valido")
else:
    print("email invalido")


