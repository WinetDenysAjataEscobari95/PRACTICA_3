from producto import Producto
from archivo_producto import ArchivoProducto

arch = ArchivoProducto("productos.txt")
arch.crearArchivo()

p1 = Producto(1, "Azucar", 8.5)
p2 = Producto(2, "Leche", 6.0)
p3 = Producto(3, "Aceite", 12.5)

arch.guardarProducto(p1)
arch.guardarProducto(p2)
arch.guardarProducto(p3)

print("Buscar producto con código 2:")
b = arch.buscaProducto(2)
if b:
    print(b.mostrar())

print("Promedio de precios:", arch.promedioPrecios())

print("Producto más caro:")
print(arch.productoMasCaro().mostrar())
