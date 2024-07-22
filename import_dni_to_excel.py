import pandas as pd
from pandas import ExcelWriter
import os
from openpyxl import Workbook

# Define the directory containing your CSV files
csv_directory = 'c:/Users/usuario/Downloads'  # Replace with your actual directory

# Initialize an empty set to store unique numbers
unique_numbers = set()

# Initialize an empty list to store dataframes
dataframes = []

# Loop through CSV files from 436.csv to 512.csv
for i in range(436, 504):
    filename = f"{i}.csv"
    filepath = os.path.join(csv_directory, filename)
    print("Hello")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath, sep=';', header=None)  # Assuming ';' as separator
        dataframes.append(df)

        # Extract unique numbers from each dataframe
        unique_numbers.update(df[0].tolist())

# Create a new XLSX file
output_xlsx = 'output.xlsx'
workbook = Workbook()
sheet = workbook.active

# Write data to the XLSX file
for df in dataframes:
    for _, row in df.iterrows():
        number, text, additional_text = row[0], row[1], row[2]
        if number not in unique_numbers:
            sheet.append([number, text, additional_text])
            unique_numbers.add(number)
            
            # Check if we've processed 1000 lines
            if len(unique_numbers) == 1000:
                print("Working...")    

# Save the XLSX file
workbook.save(output_xlsx)
print(f"Data written to {output_xlsx}")