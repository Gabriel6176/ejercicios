import linecache
import re
import os

APP_PATH=os.getcwd()

linea=1
line=linecache.getline(APP_PATH+'\\'+'ard'+'.txt', linea)
cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
index=line.find('\'')
#24052022;01062022;30062022;30697880794;D;S;N;0,00;0,10;00;00;PAN ANTONIO''PAN PABLO'PAN GUILLERMO
if index<0:
    text=line
else:
    text=line[:index]+"'"+line[index:]
print(f'{text}')
