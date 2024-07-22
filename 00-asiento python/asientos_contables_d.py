import pandas as pd
from datetime import timedelta

# Ruta del archivo Excel de entrada
input_file = r'C:\Users\usuario\Desktop\Balance 2021\Sumas y Saldos 2021_3.xlsx'
output_file = r'C:\Users\usuario\Desktop\Balance 2021\Sumas y Saldos 2021_listo_testeo.xlsx'

# Leer las hojas de trabajo "BANCO", "ASIENTOS" y "PARTIDAS_PRESUP"
df_BANCO = pd.read_excel(input_file, sheet_name='BANCO')
df_ASIENTOS = pd.read_excel(input_file, sheet_name='ASIENTOS')
df_PARTIDAS_PRESUP = pd.read_excel(input_file, sheet_name='PARTIDAS_PRESUP')

# Seleccionar las columnas requeridas
columns_to_select_1 = [
    '#CTA', '#NUM', '#FECHA', '#DIA', '#MES', '#COD', '#NOTA', '#ORDEN_PAGO', '#PROVEEDOR', '#PART_PRESU', 
    '#SALDO_DEUDOR', '#SALDO_ACREEDOR', '#ASIENTO_1', '#FECHA_1', '#CTA_CONT_1', '#DETALLE_1', '#DEBE_1', '#HABER_1', '#NOTA_1',
    '#ASIENTO_2', '#FECHA_2', '#CTA_CONT_2', '#DETALLE_2', '#DEBE_2', '#HABER_2', '#NOTA_2',
    '#ASIENTO_3', '#FECHA_3', '#CTA_CONT_3', '#DETALLE_3', '#DEBE_3', '#HABER_3', '#NOTA_3',
    '#ASIENTO_4', '#FECHA_4', '#CTA_CONT_4', '#DETALLE_4', '#DEBE_4', '#HABER_4', '#NOTA_4'
]

columns_to_select_2 = [
    "#COD_A", "#CTA_DEBE_A", "#DET_CTA_DEBE_A", "#CTA_HABER_A", "#DET_CTA_HABER_A", "#NOTA_A", 
    "#CTA_DEBE_A2", "#DET_CTA_DEBE_A2", "#CTA_HABER_A2", "#DET_CTA_HABER_A2", "#NOTA_A2"
]

columns_to_select_3 = [
    "#PART_PRESU", "#CTA_PP", "#DET_PP"
]

# Filtrar las columnas seleccionadas
df_BANCO_filtered = df_BANCO[columns_to_select_1]
df_ASIENTOS_filtered = df_ASIENTOS[columns_to_select_2]
df_PARTIDAS_PRESUP_filtered = df_PARTIDAS_PRESUP[columns_to_select_3]

# Asegurarse de que la columna '#FECHA' sea de tipo datetime
df_BANCO['#FECHA'] = pd.to_datetime(df_BANCO['#FECHA'], errors='coerce')

# Fusionar DataFrames
df_combined_1 = pd.merge(df_BANCO_filtered, df_ASIENTOS_filtered, left_on='#COD', right_on='#COD_A', how='left')
df_combined = pd.merge(df_combined_1, df_PARTIDAS_PRESUP_filtered, on='#PART_PRESU', how='left')

# Funciones para poblar las nuevas columnas
def account_entry_1(row, local_vars, asiento_prefix, fecha_prefix, cta_cont_prefix, detalle_prefix, debe_prefix, haber_prefix, nota_prefix,
                    asiento_2_prefix, fecha_2_prefix, cta_cont_2_prefix, detalle_2_prefix, debe_2_prefix, haber_2_prefix, nota_2_prefix):
    row[asiento_prefix] = local_vars['cta'] * 100000 + local_vars['num']
    row[fecha_prefix] = local_vars['fecha']
    row[cta_cont_prefix] = local_vars['cta_debe_a']
    row[detalle_prefix] = local_vars['det_cta_debe_a']
    row[debe_prefix] = local_vars['saldo_deudor']
    row[haber_prefix] = local_vars['saldo_acreedor']
    row[nota_prefix] = local_vars['nota_a'] + (str(local_vars['orden_pago']) if local_vars['cod'] != 96.3 else str(local_vars['nota']))
    row[asiento_2_prefix] = local_vars['cta'] * 100000 + local_vars['num']
    row[fecha_2_prefix] = local_vars['fecha']
    row[cta_cont_2_prefix] = local_vars['cta_haber_a']
    row[detalle_2_prefix] = local_vars['det_cta_haber_a']
    row[debe_2_prefix] = local_vars['saldo_acreedor']
    row[haber_2_prefix] = local_vars['saldo_deudor']
    row[nota_2_prefix] = local_vars['nota_a'] + (str(local_vars['orden_pago']) if local_vars['cod'] != 96.3 else str(local_vars['nota']))

def account_entry_2(row, local_vars, asiento_3_prefix, fecha_3_prefix, cta_cont_3_prefix, detalle_3_prefix, debe_3_prefix, haber_3_prefix, nota_3_prefix,
                    asiento_4_prefix, fecha_4_prefix, cta_cont_4_prefix, detalle_4_prefix, debe_4_prefix, haber_4_prefix, nota_4_prefix, part_pres_prefix, cta_pp_prefix, det_pp_prefix):
    row[asiento_3_prefix] = local_vars['cta'] * 100000 * 2 + local_vars['num']
    row[fecha_3_prefix] = local_vars['fecha'] - timedelta(days=15)
    row[cta_cont_3_prefix] = local_vars['cta_debe_a2'] if pd.notnull(local_vars['cta_debe_a2']) else local_vars['cta_pp']
    row[detalle_3_prefix] = local_vars['det_cta_debe_a2'] if pd.notnull(local_vars['det_cta_debe_a2']) else local_vars['det_pp']
    row[debe_3_prefix] = local_vars['saldo_deudor']
    row[haber_3_prefix] = local_vars['saldo_acreedor']
    row[nota_3_prefix] = local_vars['nota_a2'] + str(local_vars['orden_pago'])
    row[asiento_4_prefix] = local_vars['cta'] * 100000 * 2 + local_vars['num']
    row[fecha_4_prefix] = local_vars['fecha'] - timedelta(days=15)
    row[cta_cont_4_prefix] = local_vars['cta_haber_a2']
    row[detalle_4_prefix] = local_vars['det_cta_haber_a2']
    row[debe_4_prefix] = local_vars['saldo_acreedor']
    row[haber_4_prefix] = local_vars['saldo_deudor']
    row[nota_4_prefix] = local_vars['nota_a2'] + str(local_vars['orden_pago'])
    row[part_pres_prefix] = local_vars['part_presu']
    row[cta_pp_prefix] = local_vars['cta_pp']
    row[det_pp_prefix] = local_vars['det_pp']

# Función para procesar cada fila
def process_row(row):
    local_vars = {
        'cta': row['#CTA'],
        'num': row['#NUM'],
        'fecha': row['#FECHA'],
        'dia': row['#DIA'],
        'mes': row['#MES'],
        'cod': float(row['#COD']),
        'nota': row['#NOTA'],
        'orden_pago': row['#ORDEN_PAGO'],
        'proveedor': row['#PROVEEDOR'],
        'part_presu': row['#PART_PRESU'],
        'saldo_deudor': row['#SALDO_DEUDOR'],
        'saldo_acreedor': row['#SALDO_ACREEDOR'],
        'cta_debe_a': row['#CTA_DEBE_A'],
        'det_cta_debe_a': row['#DET_CTA_DEBE_A'],
        'cta_haber_a': row['#CTA_HABER_A'],
        'det_cta_haber_a': row['#DET_CTA_HABER_A'],
        'nota_a': row['#NOTA_A'],
        'cta_debe_a2': row['#CTA_DEBE_A2'],
        'det_cta_debe_a2': row['#DET_CTA_DEBE_A2'],
        'cta_haber_a2': row['#CTA_HABER_A2'],
        'det_cta_haber_a2': row['#DET_CTA_HABER_A2'],
        'nota_a2': row['#NOTA_A2'],
        'cta_pp': row['#CTA_PP'],
        'det_pp': row['#DET_PP']
    }

    cod_1_set = {19.4, 20.13, 22.1, 22.3, 22.4, 25.1, 25.2, 25.3, 25.4, 30.31, 30.43, 50.24, 50.44, 51.94, 52.94, 56.4, 60.2, 81.3, 81.4, 81.6, 89.3, 89.4, 96.3}
    cod_2_set = {80.2, 80.3, 80.4}

    if local_vars['cod'] in cod_1_set:
        account_entry_1(row, local_vars, '#ASIENTO_1', '#FECHA_1', '#CTA_CONT_1', '#DETALLE_1', '#DEBE_1', '#HABER_1', '#NOTA_1',
                        '#ASIENTO_2', '#FECHA_2', '#CTA_CONT_2', '#DETALLE_2', '#DEBE_2', '#HABER_2', '#NOTA_2')
    elif local_vars['cod'] in cod_2_set:
        account_entry_1(row, local_vars, '#ASIENTO_1', '#FECHA_1', '#CTA_CONT_1', '#DETALLE_1', '#DEBE_1', '#HABER_1', '#NOTA_1',
                        '#ASIENTO_2', '#FECHA_2', '#CTA_CONT_2', '#DETALLE_2', '#DEBE_2', '#HABER_2', '#NOTA_2')
        account_entry_2(row, local_vars, '#ASIENTO_3', '#FECHA_3', '#CTA_CONT_3', '#DETALLE_3', '#DEBE_3', '#HABER_3', '#NOTA_3',
                        '#ASIENTO_4', '#FECHA_4', '#CTA_CONT_4', '#DETALLE_4', '#DEBE_4', '#HABER_4', '#NOTA_4',
                        '#PART_PRESU', '#CTA_PP', '#DET_PP')

# Apply the function to each row of the DataFrame
df_processed = df_combined.apply(process_row, axis=1)
# Set the option to display all columns
pd.set_option('display.max_columns', None)
print(df_combined.head())

# Exclude columns before writing to Excel
columns_to_exclude = [
    '#CTA', '#NUM', '#FECHA', '#DIA', '#MES', '#COD', '#NOTA', '#ORDEN_PAGO', '#PROVEEDOR', '#PART_PRESU', '#SALDO_DEUDOR', '#SALDO_ACREEDOR',
    '#COD_A', '#CTA_DEBE_A', '#DET_CTA_DEBE_A', '#CTA_HABER_A', '#DET_CTA_HABER_A', '#NOTA_A',
    '#CTA_DEBE_A2', '#DET_CTA_DEBE_A2', '#CTA_HABER_A2', '#DET_CTA_HABER_A2', '#NOTA_A2',
    '#CTA_PP', '#DET_PP'
]
# Exclude columns
df_processed = df_processed.drop(columns=columns_to_exclude)

# Drop rows with all NaN values
df_processed.dropna(how='all', inplace=True)

# Define the column names for the new DataFrame
column_names = ["#ASIENTO", "#FECHA", "CTA", "#DETALLE", "#DEBE", "#HABER", "#NOTA"]

# Initialize an empty list to store the reshaped data
reshaped_data = []

# Define the number of columns for the final DataFrame
num_columns = 7

for i in range(0, df_processed.shape[1], num_columns):
    chunk = df_processed.iloc[:, i:i + num_columns]
    reshaped_data.extend(chunk.values.flatten())

# Create the new DataFrame from the reshaped data
df_final = pd.DataFrame([reshaped_data[i:i + num_columns] for i in range(0, len(reshaped_data), num_columns)], columns=column_names)

# Create the new DataFrame from the organized data
df = pd.DataFrame(df_final)

# Convert the "AA" column to numeric
df_final["#ASIENTO"] = pd.to_numeric(df["#ASIENTO"], errors='coerce')

df_final["#FECHA"] = df["#FECHA"].dt.strftime('%d/%m/%Y') 

# Convert the "AB" column to datetime
df_final["#FECHA"] = pd.to_datetime(df["#FECHA"], errors='coerce')

# Sort the DataFrame first by "AA" and then by "AB"
df_sorted = df_final.sort_values(by=["#ASIENTO", "#FECHA"])

# Save the resulting DataFrame to a new Excel file
df_sorted.to_excel(output_file, index=False)

print("¡Conversión completada!")