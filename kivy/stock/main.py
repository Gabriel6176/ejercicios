# -*- coding: utf-8 -*-
# En ocasiones el widget TextInput muestra un error para
# solucionar instala xclip 
# $ sudo apt-get install xclip
import kivy
import os
import sqlite3

from kivy.config import Config
Config.set("graphics","width","340")
Config.set("graphics","hight","640")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.screenmanager import FadeTransition
from kivy.properties import StringProperty

def connect_to_database(path):
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        create_table_pacientes(cursor)
        con.commit()
        con.close()
    except Exception as e:
        print(e)

def create_table_pacientes(cursor):
    cursor.execute(
        '''
        CREATE TABLE Pacientes(
        ID INT PRIMARY KEY NOT NULL, 
        Nombre TEXT NOT NULL, 
        Apellido TEXT NOT NULL, 
        Telefono TEXT NOT NULL,
        Diagnostico TEXT NOT NULL
        )'''
    )

class MessagePopup(Popup):
    pass

class MainWid(ScreenManager):
    def __init__(self,**kwargs):
        super(MainWid,self).__init__()
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH+'/my_agenda.db'
        self.MenuScreen = MenuScreen(self)
        self.DataBaseWid = DataBaseWid(self)
        self.InsertDataWid = BoxLayout()
        self.UpdateDataWid = BoxLayout()
        self.Popup = MessagePopup()
        
        wid = Screen(name='menu')
        wid.add_widget(self.MenuScreen)
        self.add_widget(wid)
        wid = Screen(name='database')
        wid.add_widget(self.DataBaseWid)
        self.add_widget(wid)
        wid = Screen(name='insertdata')
        wid.add_widget(self.InsertDataWid)
        self.add_widget(wid)
        wid = Screen(name='updatedata')
        wid.add_widget(self.UpdateDataWid)
        self.add_widget(wid)
        
        self.goto_menu()
        
    def goto_menu(self):
        self.current = 'menu'
        
    def goto_database(self):
        self.DataBaseWid.check_memory()
        self.current = 'database'
        
    def goto_insertdata(self):
        self.InsertDataWid.clear_widgets()
        wid = InsertDataWid(self)
        self.InsertDataWid.add_widget(wid)
        self.current = 'insertdata'

    def goto_updatedata(self,data_id):
        self.UpdateDataWid.clear_widgets()
        wid = UpdateDataWid(self,data_id)
        self.UpdateDataWid.add_widget(wid)
        self.current = 'updatedata'

class MenuScreen(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(MenuScreen,self).__init__()
        self.mainwid = mainwid
        
    def create_database(self):
        connect_to_database(self.mainwid.DB_PATH)
        self.mainwid.goto_database()

class DataBaseWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(DataBaseWid,self).__init__()
        self.mainwid = mainwid
        
    def check_memory(self):
        self.ids.container.clear_widgets()
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        cursor.execute('select ID, Nombre, Apellido, Telefono, Diagnostico from Pacientes')
        for i in cursor:
            wid = DataWid(self.mainwid)
            r1 = 'ID: '+str(1000+i[0])[1:9]+'\n'
            r2 = i[1]+' '+i[2]+'\n'
            r3 = 'Tel: '+i[3]+'\n'
            r4 = 'Diag: '+i[4]
            wid.data_id = str(i[0])
            wid.data = r1+r2+r3+r4
            self.ids.container.add_widget(wid)
        wid = NewDataButton(self.mainwid)
        self.ids.container.add_widget(wid)
        con.close()
        
class UpdateDataWid(BoxLayout):
    def __init__(self,mainwid,data_id,**kwargs):
        super(UpdateDataWid,self).__init__()
        self.mainwid = mainwid
        self.data_id = data_id
        self.check_memory()

    def check_memory(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s = 'select Nombre, Apellido, Telefono, Diagnostico from Pacientes where ID='
        cursor.execute(s+self.data_id)
        for i in cursor:
            self.ids.ti_nombre.text = i[0]
            self.ids.ti_apellido.text = i[1]
            self.ids.ti_telefono.text = str(i[2])
            self.ids.ti_diagnostico.text = str(i[3])
        con.close()

    def update_data(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        d1 = self.ids.ti_nombre.text
        d2 = self.ids.ti_apellido.text
        d3 = self.ids.ti_telefono.text
        d4 = self.ids.ti_diagnostico.text
        a1 = (d1,d2,d3,d4)
        s1 = 'UPDATE Pacientes SET'
        s2 = 'Nombre="%s",Apellido="%s",Telefono=%s,Diagnostico="%s"' % a1
        s3 = 'WHERE ID=%s' % self.data_id
        try:
            cursor.execute(s1+' '+s2+' '+s3)
            con.commit()
            con.close()
            self.mainwid.goto_database()
        except Exception as e:
            message = self.mainwid.Popup.ids.message
            self.mainwid.Popup.open()
            self.mainwid.Popup.title = "Data base error"
            if '' in a1:
                message.text = 'Uno o más campos están vacíos'
            else: 
                message.text = str(e)
            con.close()

    def delete_data(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        s = 'delete from pacientes where ID='+self.data_id
        cursor.execute(s)
        con.commit()
        con.close()
        self.mainwid.goto_database()

    def back_to_dbw(self):
        self.mainwid.goto_database()
        
class InsertDataWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(InsertDataWid,self).__init__()
        self.mainwid = mainwid

    def insert_data(self):
        con = sqlite3.connect(self.mainwid.DB_PATH)
        cursor = con.cursor()
        d1 = self.ids.ti_id.text
        d2 = self.ids.ti_nombre.text
        d3 = self.ids.ti_apellido.text
        d4 = self.ids.ti_telefono.text
        d5 = self.ids.ti_diagnostico.text
        a1 = (d1,d2,d3,d4,d5)
        s1 = 'INSERT INTO Pacientes(ID, Nombre, Apellido, Telefono, Diagnostico)'
        s2 = 'VALUES(%s,"%s","%s",%s,%s)' % a1
        try:
            cursor.execute(s1+' '+s2)
            con.commit()
            con.close()
            self.mainwid.goto_database()
        except Exception as e:
            message = self.mainwid.Popup.ids.message
            self.mainwid.Popup.open()
            self.mainwid.Popup.title = "Data base error"
            if '' in a1:
                message.text = 'Uno o más campos están vacíos'
            else: 
                message.text = str(e)
            con.close()

    def back_to_dbw(self):
        self.mainwid.goto_database()
    
class DataWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(DataWid,self).__init__()
        self.mainwid = mainwid
        
    def update_data(self,data_id):
        self.mainwid.goto_updatedata(data_id)
        
class NewDataButton(Button):
    def __init__(self,mainwid,**kwargs):
        super(NewDataButton,self).__init__()
        self.mainwid = mainwid
        
    def create_new_paciente(self):
        self.mainwid.goto_insertdata()

class MainApp(App):
    def build(self):
        return MainWid()
        
if __name__ == '__main__':
    MainApp().run()