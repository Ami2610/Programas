# Ejercicio 20
# Muestra en pantalla los primeros N números primos, donde N se pide por teclado.

import math  # Para usar sqrt

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Pedimos al usuario cuántos números primos quiere ver
n = int(input("¿Cuántos números primos deseas mostrar?: "))

contador = 0    # Contador de primos encontrados
numero = 2      # Comenzamos desde el primer número primo

print(f"\nPrimeros {n} números primos:")

# Bucle hasta que encontremos N primos
while contador < n:
    if es_primo(numero):
        print(numero)
        contador += 1
    numero += 1
