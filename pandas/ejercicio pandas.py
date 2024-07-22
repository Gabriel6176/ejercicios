import pandas as pd
import numpy as np


base=pd.read_csv('ard.txt', header=None, encoding='Latin-1', sep=';', error_bad_lines=False)
print(base)

#base=pd.read_csv('ard.txt', header=None, encoding='Latin-1', sep=';', warn_bad_lines=True)
#print(base)