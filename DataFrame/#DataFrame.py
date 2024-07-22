#DataFrame
import pandas as pd
import numpy as np
import os

#crear un array
data0=np.array([[1,4], [2,5], [3,4]])
df0=pd.DataFrame(data0, index=['row1', 'row2', 'row3'], columns=['cols1', 'cols2'])
print(df0)

#crear array desde lista de listas
data= [[1,4], [2,5], [3,4]]
df1=pd.DataFrame(data, index=['row_x1', 'row_x2', 'row_x3'], columns=['cols_x1', 'cols_x2'])
print(df1)

#array desde diccionarios
states=['California', 'Texas', 'Florida', 'New York']
population=[36987, 32147, 3258, 5698]
dict_states={'States':states, 'Population':population}
df2=pd.DataFrame(dict_states)
print(df2)

#array desde cdv
APP_PATH=os.getcwd()
df3=pd.read_csv(APP_PATH+'\\students.csv', header=0)
print(df3)

