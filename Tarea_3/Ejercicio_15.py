# Ejercicio 15
# Intercambiar los valores de dos variables A y B e imprimir el resultado.

# Pedir los valores de A y B
a = input("Ingresa el valor de A: ")
b = input("Ingresa el valor de B: ")

# Intercambiar los valores usando una asignación múltiple
a, b = b, a

# Mostrar los nuevos valores
print(f"Nuevo valor de A: {a}")
print(f"Nuevo valor de B: {b}")