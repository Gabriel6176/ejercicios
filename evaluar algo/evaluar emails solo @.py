from xml.etree.ElementInclude import FatalIncludeError

test = False

email = input("Por favor ingrese una direccion de email: ")

for i in email:
    if (i=="@"):
        test=True

if test == True:
    print("El email es valido")
else:
    print("El email es incorrecto")
