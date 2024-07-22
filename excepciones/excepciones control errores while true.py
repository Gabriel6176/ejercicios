#excepciones error en tiempo de ejecucion

def suma (num1,num2):
    return num1+num2
def resta (num1,num2):
    return num1-num2
def multiplicacion (num1,num2):
    return num1*num2
def division (num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Introdujo un cero para dividir y eso no es posible")
        return "Operacion erronea"

while True:
    try:
        op1=(int(input("Escribe un numero 1: ")))
        op2=(int(input("Escribe un numero 2: ")))
        break;
    except ValueError:
        print("Introdujo un valor erroneo")
        
operacion=input("Escribe que operacion quieres realizar (suma, resta, multiplicacion, division): ")

if operacion=="suma":
    print(suma(op1,op2))
elif operacion=="resta":
    print(resta(op1,op2))
elif operacion=="multipliacion":
    print(multiplicacion(op1,op2))
elif operacion=="division":
    print(division(op1,op2))
else:
    print("Operacion no contemplada")

print("Continua el programa")







    










