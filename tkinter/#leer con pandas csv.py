#leer con pandas csv
import pandas as pd

#problema cuando no se puede armar dataset porque hay una linea que tiene mas columnas que otras
csv_name='ard'
users = pd.read_csv(f"{csv_name}.txt", sep=';')

print(users)
