import linecache
import os

APP_PATH=os.getcwd()
txt_name='ard'

with open(APP_PATH+'\\'+txt_name+'.txt', 'rb') as f:
    xlines = len(f.readlines())
    print(xlines)
#linea es porque linea comienza y xlines es el total de lineas del txt
def find_data(linea, xlines):
    #itera hasta que recibe (-1)esto significa que no encontro el dato=() o que no encontro mas
    while True:
        txt=linecache.getline(APP_PATH+'\\'+txt_name+'.txt', linea)
        #veo cuantas lineas tiene el txt
        largo=len(txt)
        dato=';'
        lista=[]
        largo2=largo-1
        x=txt.find(str(dato), 61, largo2)
        #x=txt.find(str(dato), int(x+1), largo)
        if x>0 and linea<=xlines:
            lista.append(x)
            #print(x)
            print(f'El largo de la lista es: {len(lista)} y la linea es: {linea}')
            print(lista)
            linea+=1
        elif x<0 and linea<=xlines:
            #print(linea)
            linea+=1
            #find_data(linea)
            #break
        else:
            break

if __name__=='__main__':
    linea=1
    find_data(linea, xlines)
        