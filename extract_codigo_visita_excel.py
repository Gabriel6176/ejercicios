import pandas as pd
import re

EXCEL_INPUT='set_codigo_visita.xlsx'
EXCEL_OUTPUT=f'{EXCEL_INPUT}'+'_salida.xlsx'

# Function to extract values from sets in a string
def extract_values(set_str):
    values = re.findall(r"'(.*?)'", set_str)
    return values

# Read the Excel file
df = pd.read_excel(f"{EXCEL_INPUT}")

# Assume the column containing the sets is named 'SET_COLUMN'
# Extract values from sets and create new columns
for index, row in df.iterrows():
    set_values = row['SET_CODIGO_VISITA']
    extracted_values = extract_values(set_values)
    for i, value in enumerate(extracted_values):
        df.at[index, f'Value_{i+1}'] = value

# Save the modified DataFrame to a new Excel file
df.to_excel(f"{EXCEL_OUTPUT}", index=False)
print('-----------------JOB DONE-------------------------')