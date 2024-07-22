##----Calculadora de Cuotas vs Efectivo------




total_contado=int(input('Cual es el valor del producto de contado: '))
cantidad_cuotas=int(input('Cuantas cuotas vas a pagar: '))
valor_cuota=int(input('Cual es el valor de la cuota: '))
int_pf=float(input('Cual es el interes mensual de plazo fijo: '))

importe_total_financiado=cantidad_cuotas*valor_cuota

VAN=total_contado/((1+(float(int_pf)/100))**cantidad_cuotas)

diferencia=(total_contado*-1)+(importe_total_financiado)

if total_contado<VAN:
    print(f'Te conviene comprar de contado, vas a pagar {diferencia} pesos de menos')
else:
    print(f'Te conviene comprar en cuotas, vas a pagar {diferencia} pesos de menos')    