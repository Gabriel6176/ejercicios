import os
import pandas as pd
from pathlib import Path
import sqlite3


# Specify the directory where your CSV files are located
csv_directory = 'C:/Users/usuario/Downloads/'

# Initialize empty lists to store data
numbers = []
text1 = []
text2 = []

# Iterate through files matching the pattern
for number in range(436, 504):
    filename = f"dni{number}.csv"
    file_path = os.path.join(csv_directory, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        # Read the CSV file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as csv_file:
            lines = csv_file.readlines()

            # Process each line
            for line in lines:
                # Split the line by semicolon or comma
                parts = line.strip().split(';')  # Adjust delimiter as needed
                if len(parts) >= 1:
                    # Extract the number (first part)
                    number = parts[0]
                    number = number.rstrip(",")
                    numbers.append(number)
                    

                    # Extract text1 (second part, if available)
                    if len(parts) >= 2:
                        text1.append(parts[1])
                    else:
                        text1.append("")  # If no text1, add an empty string

                    # Extract text2 (third part, if available)
                    if len(parts) >= 3:
                        text2.append(parts[2])
                    else:
                        text2.append("")  # If no text2, add an empty string

# Create a DataFrame from the extracted data
data = {
    'Number': numbers,
    'Text1': text1,
    'Text2': text2
}
df = pd.DataFrame(data)

# Path to your SQLite database file
db_file = 'base.db'

# Establish a connection to the SQLite database
conn = sqlite3.connect(db_file)

# Export the DataFrame to SQLite database
df.to_sql('DNI', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

'''


# Write the DataFrame to an Excel file (replace 'output.xlsx' with your desired output file name)
output_file = 'output_x.xlsx'
df.to_excel(output_file, index=False)

print(f"Data written to {output_file}")'''