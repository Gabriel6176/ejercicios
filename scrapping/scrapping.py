import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


#url = 'http://190.52.34.65/Notificaciones/Informacion/Puco#'
url = 'https://www.cronista.com/MercadosOnline/monedas.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

nombre_moneda = soup.find_all('span', class_='name col')
buy_num = soup.find_all('span', class_='buy-value')
sell_num = soup.find_all('div', class_='sell col')

moneda = list()
count = 0
for i in nombre_moneda:
    if count < 156:
        moneda.append(i.text) 
    else:
        break
    count += 1

compra = list()
count = 0
for i in buy_num:
    if count < 155:
        compra.append(i.text) 
    else:
        break
    count += 1

venta = list()
count = 0
for i in sell_num:
    if count < 155:
        venta.append(i.text) 
    else:
        break
    count += 1


df1 = pd.DataFrame({'Moneda': moneda}, index=list(range(1,157)))
#aca lo que hice fue sacar la primera linea
df1.drop(index=df1.index[0],axis=0,inplace=True)
#aca lo que hice fue reindexar
df1.reset_index(drop=True, inplace=True)
df2 = pd.DataFrame({'Compra': compra}, index=list(range(1,156)))
df2.reset_index(drop=True, inplace=True)
df3 = pd.DataFrame({'Venta': venta}, index=list(range(1,156)))
df3.reset_index(drop=True, inplace=True)

#-----aca uno el df1 con df2 y despues con df3
dff=df1.join(df2, how='outer')
dff=dff.join(df3, how='outer')

#-----aca saco un archivo de saluda csv
#dff.to_excel('moneda.xlsx')

APP_PATH = os.getcwd()
#DB_PATH = self.APP_PATH+'/my_agenda2.db'
#------si lo quiero exportar sin index
dff.to_excel(APP_PATH+'/excel.xlsx', index=False)


#--------ejemplo-------------------
#gf1 = pd.DataFrame(np.random.randn(8, 3), columns=['A','B','C'], index=range(8))
#gf2 = pd.DataFrame(np.random.randn(8, 1), columns=['D'], index=range(2,10))
#gf3 = pd.DataFrame(np.random.randn(8, 2), columns=['E','F'], index=range(4,12))
#gf = gf1.join(gf2, how='outer')
#gf = gf.join(gf3, how='outer')


