# Ejercicio 13
# Leer un número y mostrar su raíz cuadrada y cúbica.
# Sin usar funciones predefinidas para la raíz cúbica.

# Pedir un número al usuario
numero = float(input("Ingresa un número: "))

# Calcular la raíz cuadrada
raiz_cuadrada = pow(numero, 0.5)

# Calcular la raíz cúbica sin funciones predefinidas
raiz_cubica = numero ** (1/3)

# Mostrar los resultados
print(f"Raíz cuadrada: {raiz_cuadrada}")
print(f"Raíz cúbica: {raiz_cubica}")