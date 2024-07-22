from tkinter import *
import os


raiz=Tk()

raiz.title("ventana de pruebas")

#raiz.resizable(0,0)
#al poner (0, 0) no me deja redimencionar

raiz.iconbitmap("gato.ico")
raiz.geometry("750x450")
raiz.config(bg="blue")

miFrame=Frame()
miFrame.pack(side="right", anchor="s")
#right and south
miFrame.pack(fill="x", expand="true")
#expande en horizontal que quiero ambos pongo both
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
#borde
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")
#el curso es un mano cuando pasa sobre mi frame
raiz.mainloop()

