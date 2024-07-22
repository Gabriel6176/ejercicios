import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#esto indica a que archivo.kv apuntar
Builder.load_file('lo_que_sea.kv')

#otra opcion es
#Builder.load_string("""
#       pego todo el texto del archivo kivy
#       """)

eleccion=0

class MyGridLayout(Widget):
    iden=ObjectProperty(None)
    nombre=ObjectProperty(None)
    apellido=ObjectProperty(None)
    edad=ObjectProperty(None)
    afiliado=ObjectProperty(None)
    telefono=ObjectProperty(None)
    mama=ObjectProperty(None)
    papa=ObjectProperty(None)    
    derivado=ObjectProperty(None)    
    fecha_ini=ObjectProperty(None)    

    def press(self):
        iden = self.iden.text
        nombre = self.nombre.text
        apellido = self.apellido.text
        edad = self.edad.text
        afiliado = self.afiliado.text
        telefono = self.telefono.text
        mama = self.mama.text
        papa = self.papa.text
        derivado = self.derivado.text
        fecha_ini = self.fecha_ini.text

        #imprime en la pantalla
        #self.add_widget(Label(text=f'Hola' {nombre}))
        print(f'Hola {nombre} {apellido} tu tienes {edad} años')

        #limpia los impuets de los text box
        self.iden.text = ""
        self.nombre.text = ""
        self.apellido.text = ""
        self.edad.text = ""
        self.afiliado.text = ""
        self.telefono.text = ""
        self.mama.text = ""
        self.papa.text = ""
        self.derivado.text = ""
        self.fecha_ini.text = ""



    def switch_on(self, intance, value):
        if value is True:
            eleccion=1
        else:
            eleccion=0

# si en esta clase la llamo class Mongo(App): el archivo kivy debe ser Mongo.kv   
class Agenda(App):
    def build(self):
        return MyGridLayout()
                
if __name__ == '__main__':
    Agenda().run()

