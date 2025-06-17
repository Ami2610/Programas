# Ejercicio 1
# Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

# Pedimos al usuario que introduzca el primer número
numero_1 = float(input("Introduce el primer número: "))

# Pedimos al usuario que introduzca el segundo número
numero_2 = float(input("Introduce el segundo número: "))

# Comparamos si el primer número es mayor que el segundo
if numero_1 > numero_2:
    # Si la condición se cumple, mostramos que el primero es mayor
    print("El primer número es mayor que el segundo.")
else:
    # Si no se cumple, mostramos que no es mayor (puede ser igual o menor)
    print("El primer número no es mayor que el segundo.")