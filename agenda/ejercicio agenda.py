import os
import pathlib
2
SALIR = 0
AGREGAR = 1
MOSTRAR = 2
BUSCAR = 3
SALIR = 4

def mostrar_menu():
    os.system('cls')
    print(f'''             Mi agenda    
{AGREGAR}) Agregar Contacto
{MOSTRAR}) Mostrar Contacto
{BUSCAR}) Buscar Contacto
{SALIR}) Salir''')

def cargar_agenda(agenda, nombre_archivo):
    if pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contacto, telefono, email = linea.strip().split(',')
                agenda.setdefault(contacto, (telefono, email))
    else:
        with open(nombre_archivo, 'w') as archivo:
           pass

def agregar_contacto(agenda, nombre_archivo):
    os.system('cls')
    print('               Agregar Contacto')
    nombre=input('Nombre: ')
    if agenda.get(nombre):
        print('El nombre ya existe')
    else:
        telefono=input('Telefono: ')
        email=input('Email:  ')
        agenda.setdefault(nombre, (telefono, email))
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f'{nombre},{telefono},{email}\n')
        print('Contacto agregado con exito')

def mostrar_contacto(agenda):
    os.system('cls')
    print('                   Mis Contactos')
    if len(agenda) > 0:
        for contacto, datos in agenda.items:
            print(f'Nombre: {contacto}')
            print(f'Telefono: {datos[0]}')
            print(f'Email: {datos[1]}')
            print('*'*50)
        else:
            print('No hay contactos registrados')

def buscar_contacto(agenda):
    os.system('cls')
    print('                   Buscar Contactos')
    if len(agenda) > 0:
        nombre = input('Ingresa el nombre: ')
        coincidencias=0
        for contacto, datos in agenda.items:
            if nombre in contacto:
                print(f'Nombre: {contacto}')
                print(f'Telefono: {datos[0]}')
                print(f'Email: {datos[1]}')
                coincidencias+=1
                print('*'*50)
        if coincidencias==0:
            print('no se encontro el contacto')
        else:
            print('Se encontraron {coincidencias} contactos')

def main():
    continuar=True
    agenda=dict()
    nombre_archivo = 'agenda.txt'
    cargar_agenda(agenda, nombre_archivo)

    while continuar:
        mostrar_menu()
        opc = int(input('Selecciona una opcion: '))
        if opc == AGREGAR:
            agregar_contacto(agenda, nombre_archivo)
        elif opc == MOSTRAR:
            mostrar_contacto(agenda)
        elif opc == BUSCAR:
            buscar_contacto(agenda)
        elif opc == SALIR:
            continuar=False
        else:
            print('Opcion no valida')
        input('Precio enter para continuar....')
    print('Nos vemos')    

if __name__ == '__main__':
    main()



















