import re

with open('ard.txt', 'r') as f:
    for i in f:
        texto=re.search(('[0-9]{11}'), i).group()
        #devuelve el numero de dni
        #print(texto)
        #devuelve
        texto2=re.split((';$'), i)
        print(texto2)


#patron.search(linea, inicio, fin)

patron=re.compile('d')
#print(patron.search('dog'))
#<re.Match object; span=(0, 1), match='d'>

print(patron.search('dog', 1))
#respuesta None porque le dije que comience desde 1 no desde cero

print(patron.search('dog', 0, 1))
#<re.Match object; span=(0, 1), match='d'>
#respuesta porque le dije que comience desde 0 hasta 1

var=re.compile(r'.*(.).*\1')
resultado=(var.match('717ak')).group(0)
print(resultado)
#resultado 7 si group(1)
#resultado 717 si group(0)
















