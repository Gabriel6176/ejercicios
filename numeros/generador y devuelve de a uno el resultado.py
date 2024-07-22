#generador numeros pares

def generapares(limite):
    num=1
    miLista=[]
    while num<limite:
        yield num*2
        num=num+1

devuelvepares=generapares(10)

print(next(devuelvepares))
print("mas codigo de programa")
print(next(devuelvepares))
print("mas codigo de programa")
print(next(devuelvepares))
print("mas codigo de programa")
print(next(devuelvepares))
print("mas codigo de programa")
### entre llamada y llamada entra en stand by





    










