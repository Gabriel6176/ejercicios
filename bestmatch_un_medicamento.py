import pandas as pd

def find_exact_match(input_file, input_column, values_file, values_column, output_file):
    # Read input and value files
    input_df = pd.read_excel(input_file)
    values_df = pd.read_excel(values_file)

    # Get input values and value list
    input_values = input_df[input_column].tolist()
    values_list = values_df[values_column].tolist()

    # Store matched rows
    matched_rows = []

    # Iterate through the input values
    for input_value in input_values:
        # Convert the input value to lowercase
        input_value_lower = input_value.lower()
        # Split the input value to extract the first word
        first_word = input_value_lower.split()[0]
        
        # Iterate through the values list
        for value in values_list:
            # Convert the value to lowercase
            value_lower = value.lower()
            # Split the value to extract its first word
            value_first_word = value_lower.split()[0]

            # Check if the first word exactly matches any value in the list
            if first_word == value_first_word:
                # Find the full row in values_df that matches the value
                matched_row = values_df.loc[values_df[values_column] == value].iloc[0].to_dict()
                matched_rows.append((input_value,) + tuple(matched_row.values()))

    # Create DataFrame with matched rows
    columns = ["Value Searched"] + list(values_df.columns)
    df = pd.DataFrame(matched_rows, columns=columns)

    # Write DataFrame to Excel file
    df.to_excel(output_file, index=False)

# Example usage:
input_file = "medicamentos_a.xlsx"
input_column = "TIPO"
values_file = "Kairos_c.xlsx"
values_column = "concatenar"
output_file = "output.xlsx"

find_exact_match(input_file, input_column, values_file, values_column, output_file)
print(f"Excel file '{output_file}' created.")