#204 justificar derecha izq

titulo="El sitio web mas imoportante de mundo"

print(titulo.ljust(len(titulo)+10,'-'))
#imprime: El sitio web mas imoportante de mundo----------

print(titulo.rjust(len(titulo)+10,'-'))
#imprime: ----------El sitio web mas imoportante de mundo

print(titulo.rjust(50,'-'))
#imprime hasta completar 50 caracteres: -------------El sitio web mas imoportante de mundo

