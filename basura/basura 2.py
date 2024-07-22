

flujo_fondos=[-100, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
d4=3/100
NPV=0
for i in range(len(flujo_fondos)):
    NPV+=flujo_fondos[i]/(1+d4)**i
    d5 = round(NPV,3)
print('El VAN es de: '+str(d5))