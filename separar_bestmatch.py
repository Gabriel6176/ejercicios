import pandas as pd
import re

# Example usage:
input_file = "medicamentos.xlsx"
input_column = "TIPO"
values_file = "Kairos_c.xlsx"
values_column = "concatenar"
output_file = "output_x.xlsx"

def extract_info(value):
    # Initialize variables
    mg = None
    tipo = None
    cantidad = None

    # Find mg value
    mg_match = re.search(r"(\d+)mg", value, re.IGNORECASE)
    if mg_match:
        mg = int(mg_match.group(1))

    # Define a dictionary of patterns and corresponding values to write
    patterns_to_write = {
        r"Aer\.?": "Aer.",
        r"Amp\.?": "Amp.",
        r"Blst\.?": "Blst.",
        r"Bolsa Doble": "Bolsa Doble.",
        r"Bolsa Simple": "Bolsa Simple.",
        r"Bolsa\.?": "Bolsa.",
        r"Caja\.?": "Caja.",
        r"Caps\.?": "Caps.",
        r"Caram\.?": "Caram.",
        r"Cart\.?": "Cart.",
        r"Champú\.?": "Champu.",
        r"Colir\.?": "Colir.",
        r"Colut\.?": "Colut.",
        r"Comp\.?": "Comp.",
        r"Crema": "Crema.",
        r"Desodorante\.?": "Desodorante.",
        r"Dosficador\.?": "Dosificador.",
        r"Dosificador\.?": "Dosificador.",
        r"Elixir\.?": "Elixir.",
        r"Emul\.?": "Emul.",
        r"Env\.?": "Env.",
        r"Espuma\.?": "Espuma.",
        r"Est\.?": "Est.",
        r"Espátula\.?": "Espatula.",
        r"Fco\.?": "Fco.",
        r"Gel\.?": "Gel.",
        r"Got\.?": "Gotas.",
        r"Gotas\.?": "Gotas",
        r"Grag\.?": "Grag.",
        r"Gran\.?": "Gran.",
        r"Inhal\.?": "Inhal.",
        r"Iny\.?": "Iny.",
        r"Jabón\.?": "Jabon.",
        r"Jalea\.?": "Jalea.",
        r"Jer. Prell\.?": "Jer. Prell.",
        r"Jbe\.?": "Jbe.",
        r"Kit\.?": "Kit.",
        r"Lágrimas\.?": "Lagrimas.",
        r"Lap. Prell\.?": "Lap. Prell.",
        r"Lap\.?": "Lap.",
        r"Lata Polvo\.?": "Lata Polvo",
        r"Lata\.?": "Lata.",
        r"Leche\.?": "Leche",
        r"Liq\.?": "Liq.",
        r"Loc\.?": "Loc.",
        r"Oral Liq\.?": "Oral Liq",
        r"Ov\.?": "Ov.",
        r"Parche\.?": "Parche.",
        r"Pasta Dental\.?": "Pasta Dental.",
        r"Pasta\.?": "Pasta.",
        r"Past\.?": "Pasta.",
        r"Pda\.?": "Pomada.",
        r"Pomo\.?": "Pomo.",
        r"Polvo\.?": "Polvo.",
        r"Pote\.?": "Pote.",
        r"Pouchs?\.?": "Pouch.",
        r"Roll On\.?": "Roll On.",
        r"Rollon\.?": "Roll On.",
        r"Sachet\.?": "Sachet.",
        r"Shamp\.?": "Shamp.",
        r"Sol\.?": "Sol.",
        r"Sobres\.?": "Sobres.",
        r"Spray\.?": "Spray.",
        r"Sticks?\.?": "Stick.",
        r"Sup\.?": "Sup.",
        r"Susp\.?": "Susp.",
        r"Tab\.?": "Tab.",
        r"Talq\.?": "Talq.",
        r"Toall\.?": "Toall.",
        r"Tubo\.?": "Tubo.",
        r"UNC\.?": "Unc.",
        r"Ung\.?": "Ung.",
        r"Vag\.?": "Vag.",
        r"Vial\.?": "Vial."
    }

    # Find tipo value
    for pattern, tipo_value in patterns_to_write.items():
        if re.search(pattern, value, re.IGNORECASE):
            tipo = tipo_value
            break

    # Find Cantidad value
    cantidad_match = re.search(r"x (\d+)", value, re.IGNORECASE)
    if cantidad_match:
        cantidad = int(cantidad_match.group(1))

    return mg, tipo, cantidad

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
                
                # Extract mg, tipo, and cantidad information from the value
                mg, tipo, cantidad = extract_info(value)
                
                # Append matched values and extracted information to matched_rows
                matched_rows.append((input_value, mg, tipo, cantidad) + tuple(matched_row.values()))

    # Create DataFrame with matched rows
    columns = ["Value Searched", "mg", "tipo", "cantidad"] + list(values_df.columns)
    df = pd.DataFrame(matched_rows, columns=columns)
    
    # Sort DataFrame
    df = df.sort_values(by=["Value Searched", "tipo", "mg", "precio"], ascending=[True, True, True, False])

    # Write DataFrame to Excel file
    df.to_excel(output_file, index=False)

find_exact_match(input_file, input_column, values_file, values_column, output_file)
print(f"Excel file '{output_file}' created.")