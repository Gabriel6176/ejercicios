
from tkinter import *

root=Tk()

varOption=IntVar()

def imprimir():
    #print(varOption.get())
    if varOption.get()==1:
        etiqueta.config(text="as elegido masculino")
    elif varOption.get()==2:
        etiqueta.config(text="as elegido femenino")
    elif varOption.get()==3:
        etiqueta.config(text="as elegido otras opciones")


Label(root, text="Genero:").pack()

Radiobutton(root, text="Masculino", variable=varOption, value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOption, value=2, command=imprimir).pack()

Radiobutton(root, text="Otras Opciones", variable=varOption, value=3, command=imprimir).pack()

etiqueta=Label(root, bg="light blue")
etiqueta.pack()


root.mainloop()

