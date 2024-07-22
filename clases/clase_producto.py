class Producto:
    contador_producto=0
    def __init__(self, nombre, precio):
        Producto.contador_producto+=1
        self._id_producto=Producto.contador_producto
        self._nombre=nombre
        self._precio=precio
    
    @property
    def precio(self):
        return self._precio
    
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__=='__main__':
    producto1=Producto('Camisa', 100)
    print(producto1)
    producto2=Producto('Pantalon', 150)
    print(producto2)

