###se uso lambda funciones anonimas

from tkinter import *

root=Tk()

miFrame=Frame(root)
miFrame.pack()

operacion=""

resultado=0

reset_pantalla=False

numeropantalla=StringVar()

## ----------------PANTALLA------------------------------
pantalla=Entry(miFrame, bg="light blue", textvariable=numeropantalla)
pantalla.grid(row=1, column=1, padx="1", pady="1", columnspan=4)
pantalla.config(bg="black", fg="green", justify="right")

##-----------------PULSACIONES TECLADO-------------------
def numeropulsado(num):
    global operacion
    global reset_pantalla    
    if reset_pantalla!=False:
        numeropantalla.set(num)
        reset_pantalla=False    
    else:
        numeropantalla.set(numeropantalla.get() + num)    
    
##-----------------suma---------------------------------
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=float(num)
    ## esto es lo mismo que resultado=resultado + float(num)
    operacion="suma"
    reset_pantalla=True
    numeropantalla.set(resultado)

##-----------------resta---------------------------------
def resta(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado-=float(num)
    operacion="resta"
    reset_pantalla=True
    numeropantalla.set(resultado)

##-----------------multiplicacion--------------------------
def multiplicacion(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado*=float(num)
    operacion="multiplicacion"
    reset_pantalla=True
    numeropantalla.set(resultado)

##-----------------division---------------------------------
def division(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado/=float(num)
    operacion="division"
    reset_pantalla=True
    numeropantalla.set(resultado)

##-----------------Ce----------------------------------------
def Ce(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado==float(num)
    operacion="CE"
    reset_pantalla=True
    numeropantalla.set(resultado)

##-----------------FUNCION ELRESULTADO--------------------
def elresultado():
    global resultado
    numeropantalla.set(resultado+float(numeropantalla.get()))
    resultado=0

## ----------------BOTONES-------------------------------

boton7=Button(miFrame, text="7", width="4", command=lambda:numeropulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width="4", command=lambda:numeropulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width="4", command=lambda:numeropulsado("9"))
boton9.grid(row=2, column=3)
botondiv=Button(miFrame, text="/", width="4", command=lambda:division(numeropantalla.get()))
botondiv.grid(row=2, column=4)

boton4=Button(miFrame, text="4", width="4", command=lambda:numeropulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width="4", command=lambda:numeropulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width="4", command=lambda:numeropulsado("6"))
boton6.grid(row=3, column=3)
botonmult=Button(miFrame, text="X", width="4", command=lambda:multiplicacion(numeropantalla.get()))
botonmult.grid(row=3, column=4)

boton1=Button(miFrame, text="1", width="4", command=lambda:numeropulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width="4", command=lambda:numeropulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width="4", command=lambda:numeropulsado("3"))
boton3.grid(row=4, column=3)
botonresta=Button(miFrame, text="-", width="4", command=lambda:resta(numeropantalla.get()))
botonresta.grid(row=4, column=4)

boton0=Button(miFrame, text="0", width="4", command=lambda:numeropulsado("0"))
boton0.grid(row=5, column=1)
botoncoma=Button(miFrame, text=",", width="4")
botoncoma.grid(row=5, column=2)
botonigual=Button(miFrame, text="=", width="4", command=lambda:elresultado())
botonigual.grid(row=5, column=3)
botonsum=Button(miFrame, text="+", width="4", command=lambda:suma(numeropantalla.get()))
botonsum.grid(row=5, column=4)

botonCe=Button(miFrame, text="CE", width="4",command=lambda:Ce(num=0))
botonCe.grid(row=6, column=4)

root.mainloop()

