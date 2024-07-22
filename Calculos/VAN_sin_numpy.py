from tkinter import *
import tkinter as tk

root=Tk()
root.title("Calculo de VAN")

miFrame=Frame(root, width=500, height=500)

# funcion para salir del programa
def salir():
    root.destroy()



# def es_numero(numero):
#     try:
#         float(numero)
#         return True
#     except ValueError:
#         return False


def procesar():
    #con esto lo que hago es dejar la lista resultado y recomend vacia por si presiono varias veces procesar para que no se sigan sumando recomendaciones
    resultado=[]
    recomend=[]
    #aca limpio la lista flujo_fondos
    flujo_fondos = []
    d1 = float(t_efvo.get())
    d2 = float(t_v_cuotas.get())
    d3 = float(t_c_cuotas.get())
    d4 = float(t_interes.get())/12/100
    d5 = 0
    if d1>0 and d2>0 and d3>0 and d4>0:
        flujo_fondos.append(d1*-1)
        contador=0
        while contador<d3:
            flujo_fondos.append(d2)
            contador+=1
        NPV=0
        for i in range(len(flujo_fondos)):
            NPV+=flujo_fondos[i]/(1+d4)**i
            d5 = round(NPV,3)
        resultado.append('El VAN es de: '+str(d5))
        if d1==0 or d2==0 or d3==0 or d4==0:
            pass
        elif NPV > 0:
            recomend.append('Conviene invertir con los ingresos previstos')
        else:
            recomend.append('No conviene invertir con los ingresos previstos')  
    else:
        if float(d1)<=0:
            resultado.append('El importe de inversion inicial es incorrecto.')
        else:
            pass 
        if float(d2)<=0:
            resultado.append('El importe ingresado en valor de ingreso es incorrecto.')
        else:
            pass 
        if float(d3)<=0: 
            resultado.append('El valor de cantidad de periodos es incorrecto.')
        else:
            pass 
        if float(d4)<=0:
            resultado.append('El importe ingresado de interes es incorrecto.')
        else:
            pass 
    l_t_resultado.config(text=str(resultado[0]))
    l_t_recomend.config(text=str(recomend[0]))
    # t_efvo=0
    # t_v_cuotas=0
    # t_c_cuotas=0
    # t_interes=0
        
b_procesar=Button(root, text="Procesar", command=procesar)
b_procesar.grid(row=8, column=2, sticky="nswe", padx="10", pady="10")

b_salir=Button(root, text="Salir", command=salir)
b_salir.grid(row=8, column=3, sticky="nswe", padx="1", pady="10")

l_comp_efvo=Label(root, text="Valor de inversion inicial: ")
l_comp_efvo.grid(row=2, column=1, sticky="w", padx="10", pady="10")

l_val_cuotas=Label(root, text="Ingresos en cuotas futuras: ")
l_val_cuotas.grid(row=3, column=1, sticky="w", padx="10", pady="10")

l_cant_cuotas=Label(root, text="Cantidad de periodos: ")
l_cant_cuotas.grid(row=4, column=1, sticky="w", padx="10", pady="10")

l_interes=Label(root, text="Interes Anual Plazo Fijo: ")
l_interes.grid(row=5, column=1, sticky="w", padx="10", pady="10")

l_porcentaje=Label(root, text=" %")
l_porcentaje.grid(row=5, column=3, sticky="w", padx="1", pady="1")

l_resultado=Label(root, text="Resultado: ")
l_resultado.grid(row=6, column=1, sticky="w", padx="10", pady="10")

resultado=[]
l_t_resultado=Label(root, text=resultado)
l_t_resultado.grid(row=6, column=2, sticky="w", padx="10", pady="10")

l_recomend=Label(root, text="Recomendación: ")
l_recomend.grid(row=7, column=1, sticky="w", padx="10", pady="10")

recomend=[]
l_t_recomend=Label(root, text=recomend)
l_t_recomend.grid(row=7, column=2, sticky="w", padx="10", pady="10")

t_efvo=StringVar()
cuadroCompraEfectivo=Entry(root, bg="light blue", textvariable=t_efvo)
cuadroCompraEfectivo.grid(row=2, column=2, sticky="w", padx="1", pady="10")
cuadroCompraEfectivo.config(fg="blue", justify="left")

t_v_cuotas=StringVar()
cuadroValorCuotas=Entry(root, bg="light blue", textvariable=t_v_cuotas)
cuadroValorCuotas.grid(row=3, column=2, sticky="w", padx="1", pady="10")
cuadroValorCuotas.config(fg="blue", justify="left")

t_c_cuotas=StringVar()
cuadroCantidadCuotas=Entry(root, bg="light blue", textvariable=t_c_cuotas)
cuadroCantidadCuotas.grid(row=4, column=2, sticky="w", padx="1", pady="10")
cuadroCantidadCuotas.config(fg="blue", justify="left")

t_interes=StringVar()
cuadroInteres=Entry(root, bg="light blue", textvariable=t_interes)
cuadroInteres.grid(row=5, column=2, sticky="w", padx="1", pady="10")
cuadroInteres.config(fg="blue", justify="left")

l_ver=Label(root, text="v 1.1 ")
l_ver.grid(row=9, column=3, sticky="w", padx="1", pady="1")

root.mainloop()




    



