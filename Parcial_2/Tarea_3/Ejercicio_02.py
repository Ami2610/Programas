# Ejercicio 2 
# Algoritmo que pida un número y diga si es positivo, negativo o 0.

# Solicitamos al usuario que introduzca un número
numero = float(input("Introduce un número: "))

# Verificamos si el número es mayor que 0
if numero > 0:
    print("El número es positivo.")
# Verificamos si el número es menor que 0
elif numero < 0:
    print("El número es negativo.")
# Si no es mayor ni menor, entonces es igual a 0
else:
    print("El número es cero.")