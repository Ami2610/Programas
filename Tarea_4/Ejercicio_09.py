# Ejercicio 9
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor).

# Se piden los tres números al usuario
numero_1 = float(input("Introduce el primer número: "))
numero_2 = float(input("Introduce el segundo número: "))
numero_3 = float(input("Introduce el tercer número: "))

# Se agrupan en una lista
numeros = [numero_1, numero_2, numero_3]

# Se ordenan en orden descendente
numeros.sort(reverse=True)

# Se muestra el resultado ordenado
print("Números ordenados de mayor a menor:", numeros)
