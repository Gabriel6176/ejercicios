import pandas as pd
import psycopg2

def ejecutar_consulta_sql(query):
    # Establecer conexión con la base de datos
    print("INICIO DE CONECCION A LA BASE")
    conexion = psycopg2.connect(
        dbname='HOSCALPRUEBA',
        user='calipso',
        password='calipso',
        host='127.21.14.21',
        port=5432  # Puerto PostgreSQL
    )
    try:
        with conexion.cursor() as cursor:
            # Ejecutar la consulta SQL
            cursor.execute(query)
            # Obtener los resultados, si es necesario
            resultados = cursor.fetchall()
            return resultados
    finally:
        # Cerrar la conexión
        conexion.close()

# Ejemplo de consulta SQL
consulta = """
SELECT * FROM   V_ITEMINVENTARIO
"""
# Llamada a la función para ejecutar la consulta
resultados = ejecutar_consulta_sql(consulta)

if resultados:
    # Convertir los resultados a un DataFrame de pandas
    df = pd.DataFrame(resultados)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel('resultados.xlsx', index=False)

    print("Resultados exportados a resultados.xlsx")
else:
    print("La consulta no devolvió resultados.")

"""
select * 
from (
SELECT 
	ALIAS_0.CANTIDAD2_CANTIDAD CANTIDAD, 
	ALIAS_1.NOMBRE UNIDAD_MEDIDA, 
		ALIAS_3.CODIGO CODIGO, 
	ALIAS_3.DESCRIPCION PRODUCTO, 
	ALIAS_4.NOMBRE DEPOSITO, 
	ALIAS_5.NOMBRE UBICACION, 
	ALIAS_10.NOMBRERUBRO RUBRO, 
	UD.SUBRUBRO_N SUBRUBRO
FROM   V_ITEMINVENTARIO ALIAS_0  
left outer join v_deposito ALIAS_4 on ALIAS_4.id = ALIAS_0.deposito_id
left outer join v_ubicacion ALIAS_5 on ALIAS_5.id = ALIAS_0.ubicacion_id 
LEFT OUTER JOIN V_UNIDADMEDIDA ALIAS_1 ON ALIAS_0.CANTIDAD2_UNIDADMEDIDA_ID = ALIAS_1.ID   
LEFT OUTER JOIN V_PRODUCTO ALIAS_3 ON ALIAS_0.PRODUCTO_ID = ALIAS_3.ID   
LEFT OUTER JOIN V_UD_PRODUCTO UD ON UD.ID = ALIAS_3.BOEXTENSION_ID
LEFT OUTER JOIN V_SEGMENTO ALIAS_9 ON ALIAS_3.SEGMENTO_ID = ALIAS_9.ID   
LEFT OUTER JOIN V_RUBRO ALIAS_10 ON ALIAS_3.RUBRO_ID = ALIAS_10.ID   
WHERE 
	ALIAS_3.ACTIVESTATUS = 0  AND  
	ALIAS_0.BO_PLACE_ID = ALIAS_5.ITEMSINVENTARIO_ID  AND   
	ALIAS_0.BO_PLACE_ID IS NOT NULL   AND  
	ALIAS_0.CANTIDAD2_CANTIDAD <> 0
union all 
SELECT distinct 
	0 CANTIDAD, 
	'' UNIDAD_MEDIDA, 
	ALIAS_3.CODIGO CODIGO, 
	ALIAS_3.DESCRIPCION PRODUCTO, 
	'' DEPOSITO, 
	'' UBICACION, 
	v_rubro.NOMBRERUBRO RUBRO, 
	UD.SUBRUBRO_N SUBRUBRO
from V_PRODUCTO ALIAS_3
left outer join v_rubro on v_rubro.id = alias_3.rubro_id
LEFT OUTER JOIN V_UD_PRODUCTO UD ON UD.ID = ALIAS_3.BOEXTENSION_ID
where ALIAS_3.CODIGO not in (
SELECT PROD2.CODIGO as codigo
from V_PRODUCTO PROD2
left outer join V_ITEMINVENTARIO PROD3 ON PROD3.PRODUCTO_ID = PROD2.ID  
where PROD3.CANTIDAD2_CANTIDAD is not null and PROD3.CANTIDAD2_CANTIDAD <> 0 ) 
) z
	order by z.CODIGO, z.producto, z.deposito
"""