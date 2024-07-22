from tkinter import *
from tkinter import messagebox
import sqlite3

##-------------------FUNCIONES-----------------------------------------

def conexionBBDD():
    miConexion=sqlite3.connect("Usuarios.db")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOS_USUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRE VARCHAR(50), 
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(30),
            DIRECCION VARCHAR(50),
            COMENTARIO VARCHAR(150))
            ''')
        messagebox.showinfo("BBDD", "Base de datos creada con exito")
    except:
        messagebox.showwarning("!Atencion!", "La base de datos ya existe")
    miConexion.commit()
    miConexion.close()

def saliraplicacion():
    valor=messagebox.askquestion("Salir", "Deseas Salir de la Apliacion?")
    if valor=="yes":
        root.destroy()
        
def limpiarCampos():
    miArchivo.set("")
    miId.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    cuadroComentarios.delete(1.0, END)
    ##lo que hice fue forrar el texto de cuadro comentarios indicando el punto de partida y final

def crear():
    miConexion=sqlite3.connect("Usuarios.db")
    miCursor=miConexion.cursor()
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadroComentarios.get("1.0", END)
    miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)", (datos))
    """miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + miNombre.get() + "','" + miPass.get() + "','" + miApellido.get() + "','" + miDireccion.get() + "','" + cuadroComentarios.get(1.0, END) + "')")"""
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con exito")
    miConexion.close()

def borrar():
    miConexion=sqlite3.connect("Usuarios.db")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + miId.get())
    miConexion.commit()
    messagebox.showinfo("Borrar", "El item se borro con exito")
    miConexion.close()

def actualizar():
    miConexion=sqlite3.connect("Usuarios.db")
    miCursor=miConexion.cursor()
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadroComentarios.get(1.0, END)
    miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIO=? WHERE ID=" + miId.get(), (datos))
            
    ###miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE='" + miNombre.get() + 
    ###    "', PASSWORD='" + miPass.get() + 
    ###    "', APELLIDO='" + miApellido.get() + 
    ###    "', DIRECCION='" + miDireccion.get() + 
    ###    "', COMENTARIO='" + cuadroComentarios.get(1.0, END) + 
    ###    "' WHERE ID=" + miId.get())
        
    miConexion.commit()
    messagebox.showinfo("Actualizar", "El item se actualizo con exito")
    miConexion.close()

def leer():
    miConexion=sqlite3.connect("Usuarios.db")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + miId.get())
    elUsuario=miCursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        cuadroComentarios.insert(1.0, usuario[5])
    miConexion.commit()
    miConexion.close()

##---------------------------------------------------------------------

root=Tk()

barraTitulo=Menu(root)
root.config(menu=barraTitulo, width=1200, height=600)
root.title("Base de Datos")

####---------------------------------------------------------------------
archivoBBDD=Menu(barraTitulo, tearoff=0) 
archivoBBDD.add_command(label="Conectar", command=conexionBBDD)
archivoBBDD.add_command(label="Salir", command=saliraplicacion)

archivoCRUD=Menu(barraTitulo, tearoff=0)
archivoCRUD.add_command(label="Crear", command=crear)
archivoCRUD.add_command(label="Leer", command=leer)
archivoCRUD.add_command(label="Actualizar", command=actualizar)
archivoCRUD.add_command(label="Borrar", command=borrar)

archivoAyuda=Menu(barraTitulo, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

barraTitulo.add_cascade(label="BBDD", menu=archivoBBDD)
barraTitulo.add_cascade(label="CRUD", menu=archivoCRUD)
barraTitulo.add_cascade(label="Ayuda", menu=archivoAyuda)



#### ------------------CUADRO MI NOMBRE------------------------
miFrame=Frame(root)
miFrame.pack()

#digo al programa que son stringvar y eso me permite usar los datos que esten dentro del recuadro
miArchivo=StringVar()
miId=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()

cuadroNombreArchivo=Entry(miFrame, textvariable=miArchivo)
cuadroNombreArchivo.grid(row=1, column=1, sticky="w", padx="10", pady="10")
cuadroNombreArchivo.config(bg="light blue", fg="red", justify="right")


cuadroId=Entry(miFrame, bg="light blue", textvariable=miId)
cuadroId.grid(row=2, column=1, sticky="w", padx="10", pady="10")

cuadroNombre=Entry(miFrame, bg="light blue", textvariable=miNombre)
cuadroNombre.grid(row=3, column=1, sticky="w", padx="10", pady="10")

cuadroPass=Entry(miFrame, bg="light blue", textvariable=miPass)
cuadroPass.grid(row=4, column=1, sticky="w", padx="10", pady="10")
cuadroPass.config(show="*", bg="light blue", fg="red", justify="left")

cuadroApellido=Entry(miFrame, bg="light blue", textvariable=miApellido)
cuadroApellido.grid(row=5, column=1, sticky="w", padx="10", pady="10")

cuadroDireccion=Entry(miFrame, bg="light blue", textvariable=miDireccion)
cuadroDireccion.grid(row=6, column=1, sticky="w", padx="10", pady="10")

cuadroComentarios=Text(miFrame, bg="light blue", width=16, height=5)
cuadroComentarios.grid(row=7, column=1, sticky="w", padx="10", pady="10")
scrollVert=Scrollbar(miFrame, command=cuadroComentarios.yview)
scrollVert.grid(row=7, column=2, sticky="nsew")
cuadroComentarios.config(yscrollcommand=scrollVert.set)


##------------------LABELS---------------------------------------------

nombreArcLabel=Label(miFrame, text="Nombre Archivo:")
nombreArcLabel.grid(row=1, column=0, sticky="e", padx="10", pady="10")

idLabel=Label(miFrame, text="id:")
idLabel.grid(row=2, column=0, sticky="e", padx="10", pady="10")

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=3, column=0, sticky="e", padx="10", pady="10")

passwordLabel=Label(miFrame, text="Password:")
passwordLabel.grid(row=4, column=0, sticky="e", padx="10", pady="10")

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=5, column=0, sticky="e", padx="10", pady="10")

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=6, column=0, sticky="e", padx="10", pady="10")

comentariosLabel=Label(miFrame, text="Comentario:")
comentariosLabel.grid(row=7, column=0, sticky="e", padx="10", pady="10")

##---------------------BOTONES----------------------------------
miFrame2=Frame(root)
miFrame2.pack()

botonCreate=Button(miFrame2, text="Create", command=crear)
botonCreate.grid(row=1, column=0, sticky="s", padx="10", pady="10")

botonRead=Button(miFrame2, text="Leer", command=leer)
botonRead.grid(row=1, column=1, sticky="s", padx="10", pady="10")

botonUpdate=Button(miFrame2, text="Actualizar", command=actualizar)
botonUpdate.grid(row=1, column=2, sticky="s", padx="10", pady="10")

botonDelete=Button(miFrame2, text="Borar", command=borrar)
botonDelete.grid(row=1, column=3, sticky="s", padx="10", pady="10")

botonLimpiar=Button(miFrame2, text="Limpiar", command=limpiarCampos)
botonLimpiar.grid(row=1, column=4, sticky="s", padx="10", pady="10")

root.mainloop()
















