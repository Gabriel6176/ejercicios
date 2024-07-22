import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import time


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

dni = soup.find_all('span', class_='name col')


dni = list()
count = 0

class scrapping():
    for i in dni:
        if count < 100:
            dni.append(i.text) 
        else:
            break
        count += 1
        # --- este es el tiempo que debe esperar en segundo para hacer el siguiente bucle for
        time.sleep(10)

df1 = pd.DataFrame({'DNI': dni}, index=list(range(1,157)))

#---aca lo que quiero es que casa 100 de acout grabe en excel y que el excel que grabe para cambiando el nombre asi no se sobre escribe
lista=0
if lista < 1000:
    APP_PATH = os.getcwd()
    df1.to_excel(APP_PATH+'/excel'+lista+'.xlsx', index=False)
    lista += 1



#url = requests.get("https://analytics.usa.gov/data/live/ie.json")
#print(url.json()['totals']['ie_version']['6.0'])

