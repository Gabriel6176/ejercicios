import pandas as pd

# Ruta del archivo Excel de entrada
input_file = r'C:\Users\usuario\Desktop\Balance 2021\Sumas y Saldos 2021_2.xlsx'
output_file = r'C:\Users\usuario\Desktop\Balance 2021\Sumas y Saldos 2021_listo_test.xlsx'

# Leer las hojas de trabajo "BANCO", "ASIENTOS" y "PARTIDAS_PRESUP"
df_BANCO = pd.read_excel(input_file, sheet_name='BANCO')
df_ASIENTOS = pd.read_excel(input_file, sheet_name='ASIENTOS')
df_PARTIDAS_PRESUP = pd.read_excel(input_file, sheet_name='PARTIDAS_PRESUP')

# Seleccionar las columnas requeridas de BANCO
columns_to_select_1 = [
    '#CTA', '#NUM', '#FECHA', '#DIA', '#MES', '#COD', '#NOTA', 
    '#ORDEN_PAGO', '#PROVEEDOR', '#PART_PRESU', '#SALDO_DEUDOR', '#SALDO_ACREEDOR',
    '#ASIENTO_1', '#FECHA_1', '#CTA_CONT_1', '#DETALLE_1', '#DEBE_1', '#HABER_1', '#NOTA_1',
    '#ASIENTO_2', '#FECHA_2', '#CTA_CONT_2', '#DETALLE_2', '#DEBE_2', '#HABER_2', '#NOTA_2',
    '#ASIENTO_3', '#FECHA_3', '#CTA_CONT_3', '#DETALLE_3', '#DEBE_3', '#HABER_3', '#NOTA_3',
    '#ASIENTO_4', '#FECHA_4', '#CTA_CONT_4', '#DETALLE_4', '#DEBE_4', '#HABER_4', '#NOTA_4'
]

# Seleccionar las columnas requeridas de ASIENTOS
columns_to_select_2 = [
    "#COD_A", "#CTA_DEBE_A", "#DET_CTA_DEBE_A", "#CTA_HABER_A", "#DET_CTA_HABER_A", 
    "#NOTA_A", "#CTA_DEBE_A2", "#DET_CTA_DEBE_A2", "#CTA_HABER_A2", "#DET_CTA_HABER_A2", 
    "#NOTA_A2"
]

# Seleccionar las columnas requeridas de PARTIDAS_PRESUP
columns_to_select_3 = [
    "#PART_PRESU", "#CTA_PP", "#DET_PP"
]

# Filtrar las columnas seleccionadas
df_BANCO_filtered = df_BANCO[columns_to_select_1]
df_ASIENTOS_filtered = df_ASIENTOS[columns_to_select_2]
df_PARTIDAS_PRESUP_filtered = df_PARTIDAS_PRESUP[columns_to_select_3]

# Fusionar df_BANCO_filtered y df_ASIENTOS_filtered basado en #COD y #COD_A
df_combined_1 = pd.merge(df_BANCO_filtered, df_ASIENTOS_filtered, left_on='#COD', right_on='#COD_A', how='left')

# Fusionar el resultado anterior con df_PARTIDAS_PRESUP_filtered basado en #PART_PRESU
df_combined = pd.merge(df_combined_1, df_PARTIDAS_PRESUP_filtered, on='#PART_PRESU', how='left')

# Check columns and rows of the merged DataFrame
print("Columns in merged DataFrame:", df_combined.columns)
print("First few rows of merged DataFrame:\n", df_combined.head())


# Función para poblar las nuevas columnas basado en el valor de #COD
def account_entry_1(row, local_vars, asiento_prefix, fecha_prefix, cta_cont_prefix, detalle_prefix, debe_prefix, haber_prefix, nota_prefix,
                    asiento_2_prefix, fecha_2_prefix, cta_cont_2_prefix, detalle_2_prefix, debe_2_prefix, haber_2_prefix, nota_2_prefix):
    row[asiento_prefix] = local_vars['cta'] * 100000 + local_vars['num']
    row[fecha_prefix] = local_vars['fecha']
    row[cta_cont_prefix] = local_vars['cta_debe_a']
    row[detalle_prefix] = local_vars['det_cta_debe_a']
    row[debe_prefix] = local_vars['saldo_deudor']
    row[haber_prefix] = local_vars['saldo_acreedor']
    row[nota_prefix] = local_vars['nota_a']
    row[asiento_2_prefix] = local_vars['cta'] * 100000 + local_vars['num']
    row[fecha_2_prefix] = local_vars['fecha']
    row[cta_cont_2_prefix] = local_vars['cta_haber_a']
    row[detalle_2_prefix] = local_vars['det_cta_haber_a']
    row[debe_2_prefix] = local_vars['saldo_deudor']
    row[haber_2_prefix] = local_vars['saldo_acreedor']
    row[nota_2_prefix] = local_vars['nota_a']

def account_entry_2(row, local_vars, asiento_3_prefix, fecha_3_prefix, cta_cont_3_prefix, detalle_3_prefix, debe_3_prefix, haber_3_prefix, nota_3_prefix,
                    asiento_4_prefix, fecha_4_prefix, cta_cont_4_prefix, detalle_4_prefix, debe_4_prefix, haber_4_prefix, nota_4_prefix, part_pres_prefix, cta_pp_prefix, det_pp_prefix):
    row[asiento_3_prefix] = local_vars['cta'] * 100000 + local_vars['num'] * 2
    row[fecha_3_prefix] = local_vars['fecha'] - 15
    row[cta_cont_3_prefix] = local_vars['cta_debe_a2']
    row[detalle_3_prefix] = local_vars['det_cta_debe_a2']
    row[debe_3_prefix] = local_vars['saldo_deudor']
    row[haber_3_prefix] = local_vars['saldo_acreedor']
    row[nota_3_prefix] = local_vars['nota_a2']
    row[asiento_4_prefix] = local_vars['cta'] * 100000 + local_vars['num'] * 2
    row[fecha_4_prefix] = local_vars['fecha'] - 15
    row[cta_cont_4_prefix] = local_vars['cta_haber_a2']
    row[detalle_4_prefix] = local_vars['det_cta_haber_a2']
    row[debe_4_prefix] = local_vars['saldo_deudor']
    row[haber_4_prefix] = local_vars['saldo_acreedor']
    row[nota_4_prefix] = local_vars['nota_a2']
    row[part_pres_prefix] = local_vars['part_presu']
    row[cta_pp_prefix] = local_vars['cta_pp']
    row[det_pp_prefix] = local_vars['det_pp']

def process_row(row):
    # Crear un diccionario local para almacenar las variables
    local_vars = {
        'cta': row['#CTA'],
        'num': row['#NUM'],
        'fecha': row['#FECHA'],
        'dia': row['#DIA'],
        'mes': row['#MES'],
        'cod': row['#COD'],
        'nota': row['#NOTA'],
        'orden_pago': row['#ORDEN_PAGO'],
        'proveedor': row['#PROVEEDOR'],
        'part_presu': row['#PART_PRESU'],
        'saldo_deudor': row.get('#SALDO_DEUDOR', 0),
        'saldo_acreedor': row.get('#SALDO_ACREEDOR', 0),
        #ASIENTO 1
        'cta_debe_a': row.get('#CTA_DEBE_A'),
        'det_cta_debe_a': row.get('#DET_CTA_DEBE_A'),
        'cta_haber_a': row.get('#CTA_HABER_A'),
        'det_cta_haber_a': row.get('#DET_CTA_HABER_A'),
        'nota_a': row.get('#NOTA_A'),
        #ASIENTO 2
        'cta_debe_a2': row.get('#CTA_DEBE_A2'),
        'det_cta_debe_a2': row.get('#DET_CTA_DEBE_A2'),
        'cta_haber_a2': row.get('#CTA_HABER_A2'),
        'det_cta_haber_a2': row.get('#DET_CTA_HABER_A2'),
        'nota_a2': row.get('#NOTA_A2'),
        #-------------------------------------------
        'part_presu': row.get("#PART_PRESU"),
        'cta_pp': row.get("#CTA_PP"),
        'det_pp': row.get("#DET_PP")
    }

    # Condiciones para asignar valores a las nuevas columnas basado en local_vars['cod']
    if local_vars['cod'] == 1:
        pass
    elif local_vars['cod'] == 19.4:
        account_entry_1(row, local_vars, 
                        '#ASIENTO_1', '#FECHA_1', '#CTA_CONT_1', '#DETALLE_1', '#DEBE_1', '#HABER_1', '#NOTA_1',
                        '#ASIENTO_2', '#FECHA_2', '#CTA_CONT_2', '#DETALLE_2', '#DEBE_2', '#HABER_2', '#NOTA_2')
    elif local_vars['cod'] == 80.3:
        #--------------------ASIENTO 1 --------------------------------
        account_entry_1(row, local_vars, 
                        '#ASIENTO_1', '#FECHA_1', '#CTA_CONT_1', '#DETALLE_1', '#DEBE_1', '#HABER_1', '#NOTA_1',
                        '#ASIENTO_2', '#FECHA_2', '#CTA_CONT_2', '#DETALLE_2', '#DEBE_2', '#HABER_2', '#NOTA_2')
        #--------------------ASIENTO 2 --------------------------------
        account_entry_2(row, local_vars, 
                        '#ASIENTO_3', '#FECHA_3', '#CTA_CONT_3', '#DETALLE_3', '#DEBE_3', '#HABER_3', '#NOTA_3',
                        '#ASIENTO_4', '#FECHA_4', '#CTA_CONT_4', '#DETALLE_4', '#DEBE_4', '#HABER_4', '#NOTA_4',
                        '#PART_PRESU', '#CTA_PP', '#DET_PP')

    return row


# Aplicar la función a cada fila del DataFrame
df_processed = df_combined.apply(process_row, axis=1)

# Guardar el DataFrame resultante en un nuevo archivo Excel
df_processed.to_excel(output_file, index=False)

print("¡Conversión completada!")