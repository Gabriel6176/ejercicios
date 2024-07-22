import pandas as pd
import re

# Define the file and sheet names
input_file = "Medicamentos_galileo.xlsx"
sheet_name = "Hoja1"

# Read the Excel file
df = pd.read_excel(input_file, sheet_name=sheet_name)

# Define the patterns to search for
patterns = [
    (r"AMP", "Amp."),
    (r"AMPOLLA", "Amp."),
    (r"CAPS", "Caps."),
    (r"COLUTORIO", "Col."),
    (r"COMPRIMIDO", "Comp."),
    (r"\bCOMP\b", "Comp."),
    (r"CREMA", "Crema."),
    (r"FRASCO", "Fco."),
    (r"GOTAS", "Gotas."),
    (r"GTAS", "Gotas."),
    (r"INYECTABLE", "Iny."),
    (r"JARABE", "Jbe."),
    (r"JGA PRELLENADA", "Jer Prell."),
    (r"JERINGA PRELLENA", "Jer Prell."),
    (r"LOCION", "Loc."),
    (r"SACHET", "Sachet."),
    (r"SOL", "Sol."),
    (r"SUSPENSION", "Susp."),
    (r"SUSP.", "Susp."),
    (r"SUPOSITORIO.", "Sup."),
    (r"UNGUENTO", "Ung.")
]

# Function to evaluate and set the "TIPO" and "MG" columns
def evaluate_row(value):
    tipo = None
    mg = None
    
    # Check for TIPO
    for pattern, tipo_value in patterns:
        if re.search(pattern, value, re.IGNORECASE):
            tipo = tipo_value
            break  # Break if pattern is found

    # Check for MG
    mg_match = re.search(r"\b(\d{1,3})\s?MG\b", value, re.IGNORECASE)
    if mg_match:
        mg = int(mg_match.group(1))
    
    return tipo, mg

# Apply the function to each row in the "Value Searched" column and create new columns for TIPO and MG
df['TIPO'], df['MG'] = zip(*df['Value Searched'].apply(evaluate_row))

# Save the updated DataFrame back to the Excel file
with pd.ExcelWriter(input_file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Updated '{sheet_name}' in '{input_file}' with 'TIPO' and 'MG' values based on pattern matching.")