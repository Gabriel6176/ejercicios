import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


#url = 'http://190.52.34.65/Notificaciones/Informacion/Puco#'
url_cero = 'https://www.tiendam22.com.ar/19-herrajes-pvc?page='
url_uno = 1
contador = 1

while contador < 28:
    url = url_cero + str(url_uno)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_title = soup.find_all('h1', class_='h3 product-title')
    Precio = soup.find_all('span', class_='price')


    listado = list()
    count = 0
    for i in product_title:
        if count < 9:
            listado.append(i.text) 
        else:
            break
        count += 1

    precio = list()
    count = 0
    for i in Precio:
        if count < 9:
            precio.append(i.text) 
        else:
            break
        count += 1

    df1 = pd.DataFrame({'Detalle': listado}, index=list(range(1,10)))
    #aca lo que hice fue sacar la primera linea
    #df1.drop(index=df1.index[0],axis=0,inplace=True)

    #aca lo que hice fue reindexar
    df1.reset_index(drop=True, inplace=True)
    df2 = pd.DataFrame({'Precio': precio}, index=list(range(1,10)))
    df2.reset_index(drop=True, inplace=True)


    #-----aca uno el df1 con df2 y despues con df3
    dff=df1.join(df2, how='outer')
    #dff=dff.join(df3, how='outer')
    print(dff)
    #-----aca saco un archivo de saluda csv
    #dff.to_excel('moneda.xlsx')

    APP_PATH = os.getcwd()
    #DB_PATH = self.APP_PATH+'/my_agenda2.db'
    #------si lo quiero exportar sin index
    #--si lo quiero exportar a excel
    ##dff.to_excel(APP_PATH+'/excel_roto1.xlsx', index=False)
    
    archivo=open(APP_PATH+'\\m22.csv', 'a', encoding='utf8')
    archivo.write(str(dff)+"\n")

    #--------ejemplo-------------------
    #gf1 = pd.DataFrame(np.random.randn(8, 3), columns=['A','B','C'], index=range(8))
    #gf2 = pd.DataFrame(np.random.randn(8, 1), columns=['D'], index=range(2,10))
    #gf3 = pd.DataFrame(np.random.randn(8, 2), columns=['E','F'], index=range(4,12))
    #gf = gf1.join(gf2, how='outer')
    #gf = gf.join(gf3, how='outer')

    url_uno+=1
