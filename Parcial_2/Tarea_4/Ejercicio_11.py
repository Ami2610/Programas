# Ejercicio 11
# Escribe un programa que determine si un número introducido por teclado es primo o no. Un número primo solo es divisible entre 
# él mismo y la unidad. Nota: Basta probar hasta la raíz cuadrada del número para ver si es divisible por otro.

import math  # Importamos para usar la función sqrt (raíz cuadrada)

# Pedimos al usuario que introduzca un número entero mayor que 1
numero = int(input("Introduce un número entero mayor que 1: "))

# Comprobamos que el número sea válido
if numero <= 1:
    print("El número debe ser mayor que 1.")
else:
    es_primo = True  # Suponemos que es primo

    # Solo probamos divisores desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False  # Si es divisible, no es primo
            break

    # Mostramos el resultado
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
