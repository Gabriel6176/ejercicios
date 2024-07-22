from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Juan", "Procesador 2018")

def infoHelp():
    messagebox.showwarning(tittle="Help", message="Grita Panchin")

def infoPT():
    messagebox.showerror(tittle="Error", message="Error Catastrofico")

def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "Quieres Salir?")
    #=="yes"
    valor=messagebox.askokcancel("Salir", "Salir?")
    ##==True
    if valor==True:
        root.destroy()
def cerrarDocumento():
    valor=messagebox.askyesno("YesNo", "Si-No")
    if valor==False:
        root.destroy()
#askyesno
#tkinter.messagebox.askquestion(title=None, message=None, **options)
#tkinter.messagebox.askokcancel(title=None, message=None, **options)
#tkinter.messagebox.askretrycancel(title=None, message=None, **options)
#tkinter.messagebox.askyesno(title=None, message=None, **options)
#tkinter.messagebox.askyesnocancel(title=None, message=None, **options)¶

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)
root.title("Panchin")

archivoMenu=Menu(barraMenu, tearoff=0) 
###tearoff son unos ------- en la parte superior arriba de Nuevo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
### si quiero poner un separador hago
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="PT", command=infoPT)
archivoHerramientas.add_command(label="PO")

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Help", command=infoHelp)
archivoAyuda.add_command(label="Version", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)





root.mainloop()

