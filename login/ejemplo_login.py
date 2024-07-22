# usuarios

class usuario():

    numUsuarios = 0

    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra
        self.conectado = False
        self.intentos = 3

        usuario.numUsuarios+=1

    def conectar(self):
        myContra = input("Ingrese su contraseña: ")
        if myContra==self.contra:
            print("Se ha conectado con exito!! ")
            self.conectado = True
        else:
            self.intentos-=1
            if self.intentos>0:
                print("Contraseña incorrecta!")
                print("Intentos restantes",self.intentos)
                self.conectar()
            else:
                print("Error no se pudo iniciar sesion")
                print("Adios!!")

    def desconectar(self):
        if self.conectado:
            print("Se cerro la coneccion con exito!!")
            self.conectado = False
        else:
            print("No ha iniciado sesion!")

    def __str__(self):
        if self.conectado:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {conect}"
        
user1 = usuario(input("Ingrese un nombre:"),input("Ingrese una contraseña:"))
print(user1)

user1.conectar()
print(user1)

user1.desconectar()
print(user1)

