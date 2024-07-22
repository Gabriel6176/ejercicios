import pandas as pd

# Input file path and sheet name
file_path = 'test_1.xlsx'
sheet_name = 'Hoja1'

# Output file path
file_path_out = 'output.xlsx'

# Load the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Fill missing values with empty strings
df['NOMBRE_PACIENTE'].fillna('', inplace=True)
df['NOMBRE'].fillna('', inplace=True)

# Function to check if any value in NOMBRE_PACIENTE is partially contained in NOMBRE
def check_contains(row):
    for nombre_paciente in df['NOMBRE_PACIENTE']:
        if nombre_paciente in row['NOMBRE']:
            return 1
    return 0

# Apply the function to each row
df['EVALUACION'] = df.apply(check_contains, axis=1)

# Write the result to the output Excel file
with pd.ExcelWriter(file_path_out, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("-------------------JOB DONE---------------")

"""import pandas as pd

# Input file path and sheet name
file_path = 'test_1.xlsx'
sheet_name = 'Hoja1'

# Output file path
file_path_out = 'output.xlsx'

# Load the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Check if values in column "NOMBRE_PACIENTE" are partially contained in column "NOMBRE"
df['EVALUACION'] = df.apply(lambda row: 1 if df['NOMBRE'].str.contains(row['NOMBRE_PACIENTE']).any() else 0, axis=1)

# Write the result to the output Excel file
with pd.ExcelWriter(file_path_out, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("-------------------JOB DONE---------------")

import pandas as pd

# Input file path and sheet name
file_path = 'test_1.xlsx'
sheet_name = 'Hoja1'

# Output file path
file_path_out = 'output.xlsx'

# Load the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Check if values in column "NOMBRE_PACIENTE" are partially contained in column "NOMBRE"
df['EVALUACION'] = df['NOMBRE'].str.contains(df['NOMBRE_PACIENTE'], regex=False).astype(int)

# Write the result to the output Excel file
with pd.ExcelWriter(file_path_out, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("-------------------JOB DONE---------------")"""    