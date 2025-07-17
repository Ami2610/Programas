# Ejercicio 10
# Algoritmo que muestre la tabla de multiplicar de los números 1, 2, 3, 4 y 5.

# Mostramos las tablas de multiplicar del 1 al 5
for numero in range(1, 6):  # Recorremos los números del 1 al 5
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):  # Multiplicamos del 1 al 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
