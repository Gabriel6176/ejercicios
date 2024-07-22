#excepciones 3 us una excepcion generica no es recomendable ya que no cual es el problema

def divide():
    try:
        op1=(float(input("Introduce el primer numero:")))
        op2=(float(input("Introduce el segundo numero:")))
        print("La division es: " + str(op1/op2))
    except:
        print("Ha ocurrido un error")
        
    print("Calculo finalizado")

divide()
