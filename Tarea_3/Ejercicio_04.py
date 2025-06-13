# Ejercicio 4
# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

# Pedimos al usuario que ingrese dos números
numero_1 = float(input("Ingresa el primer número: "))
numero_2 = float(input("Ingresa el segundo número: "))

# Realizamos las operaciones básicas
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2

# Verificamos que el segundo número no sea cero para dividir
if numero_2 != 0:
    division = numero_1 / numero_2
else:
    division = "No se puede dividir entre cero"

# Mostramos los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)