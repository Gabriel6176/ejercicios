from clase_producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes+=1
        self._id_orden=Orden.contador_ordenes
        #la convierto en una lista a productos
        self._productos=list(productos)
    
    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total=0
        for producto in self._productos:
            #aca no uso: "total += producto._precio" ya que 
            # no debo usar un atributo encapsulado de otra clase
            # lo que hago es hacer un get en la clase_producto con @property
            total += producto.precio
        return total    

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'
        return f'Orden: {self._id_orden} \nProductos: {productos_str}'


#if __name__=='__main__':