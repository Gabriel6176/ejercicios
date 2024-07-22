import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os


APP_PATH=os.getcwd()

results=pd.read_csv(APP_PATH+'\\survey_results_public.csv', index_col="ResponseId")
resultSchema=pd.read_csv(APP_PATH+'\\survey_results_schema.csv')
print(results.head(5))

languages="LanguageHaveWorkedWith"
salary="ConvertedCompYearly"

results=results.rename({languages: "Languages", salary: "Salary"}, inplace=True)
