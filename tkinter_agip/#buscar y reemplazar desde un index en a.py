#buscar y reemplazar desde un index en adelante
import linecache
import os

APP_PATH=os.getcwd()
linea=1

line=linecache.getline(APP_PATH+'\\'+'ardx'+'.txt', linea)
#find('valor buscado',desde que index,hasta que index)
index=line.find('5', 0)
print(index)
#24052022;01062022;30062022;30697880794;D;S;N;0,00;0,10;00;00;PAN ANTONIO''PAN PABLO';PAN GUILLERMO
#if index<0:
#    text=line
#else:
#    text=line[:index]+"'"+line[index:]
#print(f'{text}')
