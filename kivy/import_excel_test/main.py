
#from distutils.log import error
import sqlite3
import pandas as pd
import os

from kivy.config import Config
Config.set("graphics","width","340")
Config.set("graphics","hight","640")

from kivy.app import App
#from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.properties import StringProperty
from kivy.lang.builder import Builder
from distutils.command.build import build

Builder.load_string('''
#:import Factory kivy.factory.Factory

<ImportExcel>:
    canvas:
        Color:
            rgb: 1,1,1
        Rectangle:
            pos: self.pos
            size: self.size

<MenuScreen>:
    orientation: 'vertical'
    nombre_excel:nombre_excel
    nombre_db:nombre_db
    canvas:
        Color:
            rgb: .3,.3,.9
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation:"vertical"
        size_hint_y: .4
        cols:2
        padding: 5
        Label:
            text:"Nombre del Excel a Importar"
            size_hint_y: .2  
        TextInput:
            id:nombre_excel
            #text: 'Nombre_del_Excel.xlsx'
            hint_text: 'Ingrese Nombre del Excel sin extension xlsx'
            halign: 'center'
            multiline:False
            on_text_validate: nombre_db.focus = True
            write_tab: False
            size_hint_y: .2    
        Label:
            text:"Nombre DB a Crear"
            size_hint_y: .2  
        TextInput:
            id:nombre_db
            #text: 'Nombre_de_la_Base.db'
            hint_text: 'Ingrese Nombre Archivo DB sin extension'
            halign: 'center'
            multiline:False
            size_hint_y: .2  
    BoxLayout:
        orientation:"vertical"
        size_hint_y: .1
        padding: 5
        Button:
            text: 'Importar Archivo'
            on_press: root.importar_excel()
    BoxLayout:
        size_hint_y: .1
    BoxLayout:
        orientation:"vertical"
        size_hint_y: .1
        padding: 5
        Button:
            text: 'Salir'
            on_press: app.stop()
    BoxLayout:
        size_hint_y: .2
''')

#class MessagePopup(Popup):
#    pass  

class ImportExcel(ScreenManager):
    def __init__(self,**kwargs):
        super(ImportExcel,self).__init__()
        self.MenuScreen=MenuScreen(self)
    
        wid=Screen(name='menu')
        wid.add_widget(self.MenuScreen)
        self.add_widget(wid)

        self.goto_menu()

    def goto_menu(self):
        self.current = 'menu'

class MenuScreen(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(MenuScreen,self).__init__()
        self.mainwid = mainwid
    
    def importar_excel(self):
        d1 = self.ids.nombre_excel.text
        d2 = self.ids.nombre_db.text
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH+'\\'+d2+'.db'
        #self.DB_PATH = self.APP_PATH+'/excel.db'
        con = sqlite3.connect(self.APP_PATH+'\\'+d2+'.db')
        wb = pd.read_excel(self.APP_PATH+'\\'+d1+'.xlsx',sheet_name = None)
        #wb = pd.read_excel(self.APP_PATH+'/archivo.xlsx',sheet_name = None)
        for sheet in wb:
            wb[sheet].to_sql(sheet,con,index=False)
    
class MainApp(App):
    def build(self):
        return ImportExcel()
        
if __name__ == '__main__':
    MainApp().run()








