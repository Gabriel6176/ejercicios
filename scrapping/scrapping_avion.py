
import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


url= "https://www.flightradar24.com/-27.33,-72.59/3"
#url="https://gum.criteo.com/syncframe?origin=publishertag&topUrl=www.flightradar24.com"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

nom_avion = soup.find_all('h2', class_='airline-info__flight-no')
nom_avion2 = soup.find_all('h3', class_='airline-info__callsign airline-info__cell')
#data-v-33b584d1="">/ARG1800</h3>


avion1 = list()
count = 0
for i in nom_avion:
    if count < 2:
        avion1.append(i.text) 
    else:
        break
    count += 1

avion2 = list()
count = 0
for i in nom_avion2:
    if count < 2:
        avion2.append(i.text) 
    else:
        break
    count += 1



df1 = pd.DataFrame({'Avion1': avion1}, index=list(range(1,3)))
#aca lo que hice fue sacar la primera linea
#df1.drop(index=df1.index[0],axis=0,inplace=True)
#aca lo que hice fue reindexar
#df1.reset_index(drop=True, inplace=True)
df2 = pd.DataFrame({'Avion2': avion2}, index=list(range(1,3)))


#-----aca uno el df1 con df2
dff=df1.join(df2, how='outer')

#-----aca saco un archivo de saluda csv
#dff.to_excel('moneda.xlsx')

APP_PATH = os.getcwd()
#DB_PATH = self.APP_PATH+'/my_avion.db'
#------si lo quiero exportar sin index
dff.to_excel(APP_PATH+'/avion.xlsx', index=False)



