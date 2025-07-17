# Ejercicio 3
# Algoritmo que pide números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

# Inicializamos variables para la suma y el conteo de números
suma = 0
contador = 0

print("Introduce números (0 para terminar):")

while True:
    numero = float(input("Número: "))  # Leemos un número (puede ser decimal)

    if numero == 0:
        break  # Salimos del bucle si el número es 0

    suma += numero  # Sumamos el número
    contador += 1   # Contamos cuántos números se han introducido

# Comprobamos si se introdujeron números (evita división por cero)
if contador > 0:
    media = suma / contador  # Calculamos la media
    print(f"Suma total: {suma}")
    print(f"Media: {media}")
else:
    print("No se introdujeron números.")
