import pandas as pd
import re

def extract_info(value):
    # Initialize variables
    mg = None
    tipo = None
    cantidad = None
    
    # Find mg value
    mg_match = re.search(r"(\d+)mg", value, re.IGNORECASE)
    if mg_match:
        mg = int(mg_match.group(1))

    # Find tipo value
    tipo_pattern = (
        r"(Aer\.?|Amp\.?|Blst\.?|'Bolsa Doble'|'Bolsa Simple'|Bolsa\.?|Caja\.?|Caps\.?|Caram\.?|Cart\.?|Champú\.?|Colir\.?|Colut\.?|Comp\.|Crema|Desodorante\.?|"
        r"Dosficador\.?|Dosificador\.?|Elixir\.?|Emul\.?|Env\.?|Espuma\.?|Est\.?|Espátula\.?|Fco\.?|Gel\.?|Got\.?|Gotas\.?|Grag\.?|Gran\.?|Inhal\.?|Iny\.?|Jabón\.?|"
        r"Jalea\.?|Jer. Prell\.?|Jbe\.?|Kit\.?|Lágrimas\.?|'Lap. Prell'\.?|Lap\.|Lata Polvo\.?|Lata\.?|Leche\.?|Liq\.?|Loc\.?|Oral Liq\.?|Ov\.?|Parche\.?|"
        r"Pasta Dental\.?|Pasta\.?|Past\.?|Pda\.?|Pomo\.?|Polvo\.?|Pote\.?|Pouchs?\.?|Roll On\.?|Rollon\.?|Sachet\.?|Shamp\.|Sol\.?|Sobres\.?|Spray\.?|"
        r"Sticks?\.?|Sup\.?|Susp\.?|Tab\.?|Talq\.?|Toall\.?|Tubo\.?|UNC\.?|Ung\.?|Vag\.|Vial\.?)"
    )
    tipo_match = re.search(tipo_pattern, value)
    if tipo_match:
        tipo = tipo_match.group(1)

    # Find Cantidad value
    # If tipo is "Crema" or "Fco.", set cantidad to 1
    if tipo and tipo.lower() in ['crema', 'fco.', 'pomo', 'ung.', 'amp.', 'loc.', 'gel', 'gotas', 'pda.']:
        cantidad = 1
    elif cantidad_match := re.search(r"x (\d+)", value, re.IGNORECASE):
        cantidad = int(cantidad_match.group(1))

    return mg, tipo, cantidad

def main():
    # Read input file
    input_file = "Kairos_pelado.xlsx"
    column1 = 'droconcat'
    column2 = 'pre_Descripcion'
    output_file = "Kairos_x.xlsx"
    
    input_df = pd.read_excel(input_file)

    # Store matched rows
    matched_rows = []

    for index, row in input_df.iterrows():
        # Concatenate column1 and column2 with a space between them
        input_value = f"{row[column1]} {row[column2]}"

        # Extract mg, tipo, and cantidad information from the value
        mg, tipo, cantidad = extract_info(input_value)

        # Append matched values to matched_rows along with additional columns from the input file
        matched_row = [row[column1], row[column2], input_value, mg, tipo, cantidad]
        matched_rows.append(matched_row)

    # Create DataFrame with matched rows
    columns = [column1, column2, "Value Searched", "mg", "tipo", "cantidad"]
    df_matched = pd.DataFrame(matched_rows, columns=columns)
    
    # Concatenate df_matched with input_df
    df_combined = pd.concat([input_df, df_matched[["Value Searched", "mg", "tipo", "cantidad"]]], axis=1)
    
    # Write DataFrame to Excel file
    df_combined.to_excel(output_file, index=False)
    print(f"Excel file '{output_file}' created.")

if __name__ == "__main__":
    main()