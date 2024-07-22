import pandas as pd

# Sample DataFrame for demonstration (Assuming df_combined is ANA)
data = {
    "A1": [1, 2, 3],
    "A2": [4, 5, 6],
    "A3": [7, 8, 9],
    "A4": [10, 11, 12],
    "A5": [13, 14, 15],
    "A6": [16, 17, 18],
    "A7": [19, 20, 21],
    "A8": [22, 23, 24],
    "A9": [25, 26, 27],
    "A10": [28, 29, 30],
    "A11": [31, 32, 33],
    "A12": [34, 35, 36],
    "A13": [37, 38, 39],
    "A14": [40, 41, 42],
    "A15": [43, 44, 45]
}
ANA = pd.DataFrame(data)
print("Original DataFrame:")
print(ANA)

# Define the column names for the new DataFrame
column_names = ["AA", "AB", "AC", "AD", "AE"]

# Initialize an empty list to store the reshaped data
reshaped_data = []

# Reshape the DataFrame
num_columns = 5
for i in range(0, ANA.shape[1], num_columns):
    chunk = ANA.iloc[:, i:i + num_columns]
    reshaped_data.extend(chunk.values.flatten())

# Create the new DataFrame from the reshaped data
df_final = pd.DataFrame([reshaped_data[i:i + num_columns] for i in range(0, len(reshaped_data), num_columns)], columns=column_names)

# Display the new DataFrame
print("Reshaped DataFrame:")
print(df_final)


'''
ANA = pd.DataFrame(data)
print(ANA)


# Define the column names for the new DataFrame
column_names = ["AA", "AB", "AC", "AD", "AE"]

# Initialize an empty dictionary to store the data for the new DataFrame
df_final_final = {}

# Define the number of columns for the final DataFrame
num_columns = 5

# Reshape the stacked series into a DataFrame with the specified number of columns
df_final = pd.DataFrame(ANA.values.reshape(-1, num_columns), columns=column_names)


# Iterate over the columns of the reshaped DataFrame and organize the values into the desired format
for idx, col_name in enumerate(column_names):
    start_idx = idx * num_columns
    end_idx = start_idx + num_columns
    df_final_final[col_name] = df_final.iloc[:, start_idx:end_idx].values.flatten()


# Create the new DataFrame from the organized data
df = pd.DataFrame(df_final_final)
print(df.head())

print(df_final)
'''

"""# Stack the DataFrame 'ANA' to create a single column Series
stacked_series = ANA.stack()

# Define the number of columns for the final DataFrame
num_columns = 5

# Reshape the stacked series into a DataFrame with the specified number of columns
df_final = pd.DataFrame(stacked_series.values.reshape(-1, num_columns), columns=["A1", "A2", "A3", "A4", "A5"])
"""
