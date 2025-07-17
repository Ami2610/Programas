# Ejercicio 3
# Escribe un programa que lea un número e indique si es par o impar.

# Pedimos al usuario que introduzca un número entero
numero = int(input("Introduce un número entero: "))

# Verificamos si el residuo al dividir entre 2 es 0
if numero % 2 == 0:
    print("El número es par.")
else:
    # Si el residuo no es 0, es impar
    print("El número es impar.")
