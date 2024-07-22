from tkinter import *

root=Tk()

miFrame=Frame(root, width=2000, height=600)
miFrame.pack()

miNombre=StringVar()

cuadroNombre=Entry(miFrame, bg="light blue", textvariable=miNombre)
cuadroNombre.grid(row=3, column=2, sticky="w", padx="10", pady="10")
cuadroNombre.config(fg="blue", justify="center")
#si uso .place(x=100, y=100) es ancho por alto
#el texto aparecera en azul y alineado al medio

cuadroApellido=Entry(miFrame, bg="light blue")
cuadroApellido.grid(row=4, column=2, sticky="w", padx="10", pady="10")

cuadroEdad=Entry(miFrame, bg="light blue")
cuadroEdad.grid(row=5, column=2, sticky="w", padx="10", pady="10")

cuadroPass=Entry(miFrame, bg="light blue")
cuadroPass.grid(row=6, column=2, sticky="w", padx="10", pady="10")
cuadroPass.config(show="!")
#si quiero que cuando excriba aparezcan signos

cuadroComentarios=Text(miFrame, bg="light blue", width=16, height=5)
cuadroComentarios.grid(row=7, column=2, sticky="w", padx="10", pady="10")
scrollVert=Scrollbar(miFrame, command=cuadroComentarios.yview)
scrollVert.grid(row=7, column=3, sticky="nsew")
cuadroComentarios.config(yscrollcommand=scrollVert.set)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=3, column=1, sticky="w", padx="10", pady="10")

apellidoLabel=Label(miFrame, text="Apellido estupendo:")
apellidoLabel.grid(row=4, column=1, sticky="w", padx="10", pady="10")
#pad x es espacios en horizontal
#pad y es espacio en vertical

edadLabel=Label(miFrame, text="Edad:")
edadLabel.grid(row=5, column=1, sticky="w", padx="10", pady="10")

passLabel=Label(miFrame, text="Pass:")
passLabel.grid(row=6, column=1, sticky="w", padx="10", pady="10")

comentariosLabel=Label(miFrame, text="Comentario:")
comentariosLabel.grid(row=7, column=1, sticky="w", padx="10", pady="10")

def codigoBoton():
    miNombre.set("Juan")


botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()

