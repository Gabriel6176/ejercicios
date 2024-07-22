from tkinter import *

root=Tk()

root.title("Ejemplo")

Playa=IntVar()
Plurificador=IntVar()
Montaña=IntVar()

def opcionesviajes():
    opcionelegida=""
    if(Playa.get()==1):
        opcionelegida+=" Playa"
    if(Plurificador.get()==1):
        opcionelegida+=" Plurificador"
    if(Montaña.get()==1):
        opcionelegida+=" Montaña"
    
    Textofinal.config(text=opcionelegida)

foto=PhotoImage(file="descarga.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=Playa, onvalue=1, offvalue=0, command=opcionesviajes).pack()
Checkbutton(frame, text="Plurificador", variable=Plurificador, onvalue=1, offvalue=0, command=opcionesviajes).pack()
Checkbutton(frame, text="Montaña", variable=Montaña , onvalue=1, offvalue=0, command=opcionesviajes).pack()

Textofinal=Label(frame)
Textofinal.pack()


root.mainloop()



