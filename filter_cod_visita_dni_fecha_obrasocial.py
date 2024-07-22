import pandas as pd

# Read the Excel file
df = pd.read_excel("Prestaciones2024_puco.xlsx")

# Group by 'NUM_DOCUMENTO_PACIENTE' and 'FECHA'
grouped_df = df.groupby(['NUM_DOCUMENTO_PACIENTE', 'FECHA'])

# Filter groups where 'NUM_DOCUMENTO_PACIENTE' and 'FECHA' have unique values within each group
filtered_groups = grouped_df.filter(lambda x: x['NUM_DOCUMENTO_PACIENTE'].nunique() == 1 and x['FECHA'].nunique() == 1)

# Further filter to include groups where 'dobrasocial' has different values within the group
filtered_df = filtered_groups.groupby(['NUM_DOCUMENTO_PACIENTE', 'FECHA']).filter(lambda x: x['dobrasocial'].nunique() > 1)

# Export the filtered DataFrame to an Excel file
filtered_df.to_excel("resultado_15052024.xlsx", index=False)

print("Filtered data exported to resultado_15052024.xlsx")

'''
import pandas as pd

# Read the Excel file
df = pd.read_excel("Prestaciones2024_puco.xlsx")

# Filter the dataframe based on your conditions
filtered_df = df[df['CODIGO_VISITA'].duplicated(keep=False) & 
                 df['NUM_DOCUMENTO_PACIENTE'].duplicated(keep=False) & 
                 df['FECHA'].duplicated(keep=False) &
                 df['dobrasocial'].duplicated(keep=True)]

# Export the filtered DataFrame to an Excel file
filtered_df.to_excel("resultado_15052024.xlsx", index=False)

print("Filtered data exported to resultado_15052024.xlsx")
'''