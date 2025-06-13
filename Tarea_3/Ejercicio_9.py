# Ejercicio 9
# Calcular el precio final de una compra aplicando un descuento del 15%.

# Pedir el precio original de la compra
precio_original = float(input("Ingresa el precio original de la compra: $"))

# Calcular el 15% de descuento
descuento = precio_original * 0.15

# Calcular el precio final después del descuento
precio_final = precio_original - descuento

# Mostrar el precio final de forma clara
print(f"Precio final con 15% de descuento: ${precio_final}")