import math
import re

dato = input("Ingrese numero: ")
numero = re.compile(r'^\-?[1-9][0-9]*$')   
#^ inicio \-? valor positivo o negativo [1-9] el primer num. no puede ser cero [0-9] sig. dig de 0 a 9 y $ final cadena
es = re.match(numero,dato)

i=1
if es:
    print("el numero es valido")
else:
    while es==None and i<5:
        dato = input("Ingrese numero: ")
        numero = re.compile(r'^\-?[1-9][0-9]*$')   
        #^ inicio \-? valor positivo o negativo [1-9] el primer num. no puede ser cero [0-9] sig. dig de 0 a 9 y $ final cadena
        es = re.match(numero,dato)
        i=i+1
    else:
        print("Intentaste mucho nabo")
        print("chau papu")
