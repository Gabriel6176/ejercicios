#funciones pandas
import os
import pandas as pd
import numpy as np

APP_PATH=os.getcwd()
df=pd.read_csv(APP_PATH+'\\students.csv', header=0)
print(df)

#len
len(df)