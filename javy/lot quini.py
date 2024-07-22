from random import randint

# quini6 del 00 al 45
#loto del 1 al 41

quini_6 = []
loto = []

def numeros_quini():
    numeros = 0

    while numeros <= 5:
        quini_6.append(randrange(0,45))
        numeros += 1
    else:
         quini_6.sort()


(numeros_quini())
print(quini_6)

def numeros_loto():
    numerosloto = 0

    while numerosloto <= 5:
        loto.append(randint(1,41))
        numerosloto += 1
    else:
         loto.sort()


(numeros_loto())
print(loto)