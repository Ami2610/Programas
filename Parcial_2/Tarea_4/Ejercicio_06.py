# Ejercicio 6
# Escribe un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# Pedimos dos números al usuario
inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

# Aseguramos que el inicio sea menor o igual al fin
if inicio > fin:
    inicio, fin = fin, inicio  # Intercambiamos los valores si están en orden inverso

print(f"Números pares entre {inicio} y {fin}:")

# Recorremos el rango y mostramos solo los números pares
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:  # Verificamos si el número es par
        print(numero)
