import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado un persona con el nombre ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas():
    
    personas=[]

    def __init__(self):
        listadepersonas=open("ficheroexterno", "ab+")   
        #append binario y + opciones como lectura
        listadepersonas.seek(0)

        try:
            self.personas=pickle.load(listadepersonas)
            print("secargaron {} personas del fichero externo".formart(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listadepersonas.close()
            del(listadepersonas)
        
    def agregarpersonas(self, p):
        self.personas.append(p)
        self.guardarpersonasenficheroexterno()

    def mostrarpersonas(self):
        for p in self.personas:
            print(p)
    
    def guardarpersonasenficheroexterno(self):
        listadepersonas=open("ficheroexterno", "wb")
        pickle.dump(self.personas, listadepersonas)
        listadepersonas.close()
        del (listadepersonas)
    
    def mostrarficheroexterno(self):
        print("la informacion de la persona es ")
        for p in self.personas:
            print(p)


miLista=ListaPersonas()
persona=Persona("amancio", "masculino", 72)
miLista.agregarpersonas(persona)
miLista.mostrarficheroexterno()


