# Ejercicio 1
# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros 
# entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. 
# Por ejemplo, 5! = 1 × 2 × 3 × 4 × 5 = 120).

# Pedimos al usuario que ingrese un número entero
numero = int(input("Introduce un número para calcular su factorial: "))

# Inicializamos el factorial en 1
factorial = 1

# Si el número es negativo, no tiene factorial
if numero < 0:
    print("El factorial no está definido para números negativos.")
# Si el número es 0, su factorial es 1 por definición
elif numero == 0:
    print("El factorial de 0 es 1")
# Si es un número positivo, calculamos el factorial
else:
    for i in range(1, numero + 1):
        factorial *= i  # Multiplicamos factorial por cada número de 1 a n
    print(f"El factorial de {numero} es {factorial}")
