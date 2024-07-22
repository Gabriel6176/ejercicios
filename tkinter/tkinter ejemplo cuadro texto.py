from tkinter import *

root=Tk()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame, bg="light blue")
cuadroNombre.grid(row=3, column=2, sticky="e", padx="10", pady="10")
cuadroNombre.config(fg="blue", justify="center")
#si uso .place(x=100, y=100) es ancho por alto
#el texto aparecera en azul y alineado al medio

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=3, column=1, sticky="w", padx="10", pady="10")

cuadroApellido=Entry(miFrame, bg="light blue")
cuadroApellido.grid(row=4, column=2, sticky="e", padx="100", pady="100")

apellidoLabel=Label(miFrame, text="Apellido estupendo:")
apellidoLabel.grid(row=4, column=1, sticky="w", padx="100", pady="100")
#pad x es espacios en horizontal
#pad y es espacio en vertical

cuadroEdad=Entry(miFrame, bg="light blue")
cuadroEdad.grid(row=5, column=2, sticky="e", padx="50", pady="50")

edadLabel=Label(miFrame, text="Edad:")
edadLabel.grid(row=5, column=1, sticky="w", padx="50", pady="50")

cuadroPass=Entry(miFrame, bg="light blue")
cuadroPass.grid(row=6, column=2, sticky="e", padx="50", pady="50")
cuadroPass.config(show="!")
#si quiero que cuando excriba aparezcan asteriscos

passLabel=Label(miFrame, text="Pass:")
passLabel.grid(row=6, column=1, sticky="w", padx="50", pady="50")




root.mainloop()

