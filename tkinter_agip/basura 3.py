import linecache
import os
import re

APP_PATH=os.getcwd()
df='ard'
linea=355195
#texto=linecache.getline(APP_PATH+'\\'+df+'.txt', linea)
with open(APP_PATH+'\\'+df+'.txt',encoding='iso-8859-1') as f:
    l1 = f.readlines()
    texto=re.search('(.*)', l1[linea-1]).group()
    print(texto)
