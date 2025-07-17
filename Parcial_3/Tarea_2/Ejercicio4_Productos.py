# Creación de la clase padre Producto
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Categoría: {self.categoria}")

#Creación de la clase hija ProductoConDescuento que hereda de Producto
class ProductoConDescuento(Producto):
    def __init__(self, producto_base, descuento):
        # Reutilizamos el producto base directamente
        super().__init__(producto_base.nombre, producto_base.precio, producto_base.categoria)
        self.descuento = descuento
        self.precio_final = self.precio * (1 - self.descuento / 100)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Descuento: {self.descuento}%")
        print(f"Precio con descuento: ${self.precio_final:.2f}")

# Crear un producto base
producto_base1 = Producto("Laptop", 15000, "Electrónica")
producto_base2 = Producto("Zapatos", 5000, "Calzado")
# Aplicar descuento al mismo producto
producto_con_descuento1 = ProductoConDescuento(producto_base1, 10)
producto_con_descuento2 = ProductoConDescuento(producto_base2, 10)
# Mostrar resultados
print("Producto original:")
producto_base1.mostrar_info()

print("\nProducto con descuento:")
producto_con_descuento1.mostrar_info()

print("\nProducto original:")
producto_base2.mostrar_info()

print("\nProducto con descuento:")
producto_con_descuento2.mostrar_info()
