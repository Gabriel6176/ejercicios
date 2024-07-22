import pandas as pd
from fuzzywuzzy import process

# Read Excel files into pandas DataFrames
medicamentos_df = pd.read_excel("medicamentos.xlsx")
kairos_df = pd.read_excel("kairos_c.xlsx")

# Adjust fuzzy matching parameters and use partial matching
def find_best_match(value, choices):
    best_match, score = process.extractOne(value, choices, scorer=process.partial_ratio)
    return best_match

# Iterate through each value in "tipo" column of medicamentos_df
for index, row in medicamentos_df.iterrows():
    tipo = row["TIPO"]
    # Find the best match in "pre_Descripcion" column of kairos_df
    best_match = find_best_match(tipo, kairos_df["concatenar"])
    if best_match:
        # Retrieve the corresponding row from kairos_df
        matched_row = kairos_df[kairos_df["concatenar"] == best_match]
        # Paste the information into medicamentos_df after column "c"
        for column in matched_row.columns:
            if column != "concatenar":  # Exclude the description column
                medicamentos_df.at[index, column] = matched_row.iloc[0][column]

# Write the updated DataFrame back to "medicamentos.xlsx"
medicamentos_df.to_excel("medicamentos_updated.xlsx", index=False)

