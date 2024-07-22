class Orden:
    contador_orden = 0

    def __init__(self, producto):
        Orden.contador_orden+=1
        self.id_orden=Orden.contador_orden
        self.producto=producto
    
    def __str__(self):
        pass

class Producto:
    contador_producto=0
    def __init__(self, nombre, precio):
        Producto.contador_producto+=1
        self.id_producto=Producto.contador_producto
        self.nombre=nombre
        self.precio=precio
    
    def __str__(self):
        pass
