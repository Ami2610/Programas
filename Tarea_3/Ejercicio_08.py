# Ejercicio 8
# Calcular el sueldo total de un vendedor con un sueldo base más un 10% extra por comisión de tres ventas.

# Pedir el sueldo base
sueldo_base = float(input("Ingresa el sueldo base del vendedor: $"))

# Pedir el monto de las tres ventas
venta_1 = float(input("Ingresa el monto de la primera venta: $"))
venta_2 = float(input("Ingresa el monto de la segunda venta: $"))
venta_3 = float(input("Ingresa el monto de la tercera venta: $"))

# Calcular la comisión (10% del total de ventas)
total_ventas = venta_1 + venta_2 + venta_3
comision = total_ventas * 0.10

# Calcular el sueldo total (sueldo base + comisión)
sueldo_total = sueldo_base + comision

# Mostrar el resultado de forma sencilla
print(f"Sueldo total: ${sueldo_total}")