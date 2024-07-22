import os
import sqlite3
import csv
import linecache
import re

APP_PATH=os.getcwd()

linea=2
line=linecache.getline(APP_PATH+'\\'+'1'+'.txt', linea)
cuit=re.search('(\d\d\d\d\d\d\d\d\d\d\d)', line).group()
index=line.find('\'')
if index<0:
    text=line
else:
    text=line[:index]+"'"+line[index:]
print(text)
#text=re.search('(.*)', line).group(1)
#print(f'{text}')
linea+=1     
