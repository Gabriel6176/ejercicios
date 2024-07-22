import pandas as pd


data = pd.read_excel(r"C:/users/usuario/downloads/excel.xlsx")

df = pd.DataFrame(data, columns=['product', 'price'])

print(df)





