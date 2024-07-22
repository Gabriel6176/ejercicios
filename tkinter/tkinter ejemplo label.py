from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=500)

miFrame.pack()

miImagen=PhotoImage(file="descarga.png")
miLabel=Label(miFrame, image=miImagen, text="Hola alumnos", fg="red", font=("arial", 18))
miLabel.place(x=300, y=100)




root.mainloop()

