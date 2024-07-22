from clase_producto import Producto
from clase_orden import Orden

producto1=Producto('Camisa', 100.01)
producto2=Producto('Pantalon', 150.02)
producto3=Producto('Calcetin', 50.03)
producto4=Producto('Blusa', 70.04)

productos_1= [producto1, producto2]
productos_2= [producto3, producto4]

orden1=Orden(productos_1)
#aca le agrego los productos
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)

print(f'Total Orden {Orden.contador_ordenes}: {orden1.calcular_total()}')

orden2=Orden(productos_2)
print(orden2)
print(f'Total Orden {Orden.contador_ordenes}: {orden2.calcular_total()}')