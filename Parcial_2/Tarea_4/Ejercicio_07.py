# Ejercicio 7
# Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

# Pedimos al usuario un número para mostrar su tabla de multiplicar
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")

# Mostramos la tabla del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
