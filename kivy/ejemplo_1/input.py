import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class TextInput():
    pass

class MyGridLayout(GridLayout):
    #inicialize infinite keywords
    def __init__(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        #set columns
        self.cols = 1
        #------------------------
        self.top_grid = GridLayout(size_hint_y=.9)
        self.top_grid.cols = 2
        
        #------------------------
        self.top_grid.add_widget(Label(text="#ID"))
        self.id_paciente = TextInput(multiline=False)
        self.top_grid.add_widget(self.id_paciente)
        #------------------------
        self.top_grid.add_widget(Label(text="Nombre"))
        self.nombre_paciente = TextInput(multiline=False)
        self.top_grid.add_widget(self.nombre_paciente)
        #------------------------
        self.top_grid.add_widget(Label(text="Apellido"))
        self.apellido_paciente = TextInput(multiline=False)
        self.top_grid.add_widget(self.apellido_paciente)
        #------------------------
        self.top_grid.add_widget(Label(text="Edad"))
        self.edad_paciente = TextInput(multiline=False)
        self.top_grid.add_widget(self.edad_paciente)
        #------------------------
        self.top_grid.add_widget(Label(text="Diagnostico"))
        self.diagnostico_paciente = TextInput(multiline=False)
        self.top_grid.add_widget(self.diagnostico_paciente)
        #------------------------
        self.top_grid.add_widget(Label(text="Telefono"))
        self.telefono_paciente = TextInput(multiline=False)
        self.top_grid.add_widget(self.telefono_paciente)
        #------------------------
        self.top_grid.add_widget(Label(text="Numero Socio"))
        self.numerosocio_paciente = TextInput(multiline=False)
        self.top_grid.add_widget(self.numerosocio_paciente)
        #------------------------
        self.top_grid.add_widget(Label(text="Nombre Mamá"))
        self.nombre_mama = TextInput(multiline=False)
        self.top_grid.add_widget(self.nombre_mama)
        #----------------------------
        self.top_grid.add_widget(Label(text="Telefono Mamá"))
        self.telefono_mama = TextInput(multiline=False)
        self.top_grid.add_widget(self.telefono_mama)
        #----------------------------
        self.top_grid.add_widget(Label(text="DNI Mamá"))
        self.dni_mama = TextInput(multiline=False)
        self.top_grid.add_widget(self.dni_mama)
                #----------------------------
        self.top_grid.add_widget(Label(text="Nombre Papá"))
        self.nombre_papa = TextInput(multiline=False)
        self.top_grid.add_widget(self.nombre_papa)
        #----------------------------
        self.top_grid.add_widget(Label(text="Telefono Papá"))
        self.telefono_papa = TextInput(multiline=False)
        self.top_grid.add_widget(self.telefono_papa)
        #----------------------------
        self.top_grid.add_widget(Label(text="DNI Papá"))
        self.dni_papa = TextInput(multiline=False)
        self.top_grid.add_widget(self.dni_papa)
        #---------------------------
        self.add_widget(self.top_grid)
        #--bottom grid-------------------
        self.bottom_grid = GridLayout(size_hint_y=.1)
        self.bottom_grid.cols = 2        
        #-create a submit button---------------
        #, font_size=20, size_hint_y=None, height=30
        self.bottom_grid.agregar = Button(text="Agregar", font_size=15)
        self.bottom_grid.agregar.bind(on_press=self.press)
        self.bottom_grid.add_widget(self.bottom_grid.agregar)
        #------------------
        self.bottom_grid.buscar = Button(text="Buscar", font_size=15)
        self.bottom_grid.buscar.bind(on_press=self.press)
        self.bottom_grid.add_widget(self.bottom_grid.buscar)
        #------------------
        self.bottom_grid.actualizar = Button(text="Actualizar", font_size=15)
        self.bottom_grid.actualizar.bind(on_press=self.press)
        self.bottom_grid.add_widget(self.bottom_grid.actualizar)
        #------------------
        self.bottom_grid.listado = Button(text="Listado", font_size=15)
        self.bottom_grid.listado.bind(on_press=self.press)
        self.bottom_grid.add_widget(self.bottom_grid.listado)
        #---------------------------
        self.add_widget(self.bottom_grid)

    def press (self, instance):
        pass
    
class MyApp(App):
    def build(self):
        return MyGridLayout()
                
if __name__ == '__main__':
    MyApp().run()

