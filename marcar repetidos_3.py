import pandas as pd

# Read the Excel file
input_file = 'numeros_repetidos.xlsx'
df = pd.read_excel(input_file)

# Extract the numbers from column "A" starting from row 2
numbers = df.iloc[1:, 0]

# Count the occurrences of each number
counts = numbers.value_counts()

# Create a new column with values based on whether the number is repeated or not
def mark_repeated(x):
    if x in counts:
        return 1 if counts[x] > 1 else 0
    else:
        return 0  # Return 0 for numbers not found in the counts dictionary

df['Repeated'] = df['NUM_DOCUMENTO_PACIENTE'].map(mark_repeated)

# Write the number 1 to column 7 for repeated numbers, and 0 otherwise
df['Column_7'] = df['Repeated'].apply(lambda x: 1 if x == 1 else 0)

# Save the updated DataFrame to a new Excel file
output_file = 'numeros_repetidos_3.xlsx'
df.to_excel(output_file, index=False)

print("New Excel file saved successfully.")
