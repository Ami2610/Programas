# Ejercicio 18
# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

# Se solicita el número del mes
mes = int(input("Introduce un número de mes (1-12): "))

# Verificamos el número ingresado y mostramos los días correspondientes
if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("Este mes tiene 31 días.")
elif mes in [4, 6, 9, 11]:
    print("Este mes tiene 30 días.")
elif mes == 2:
    print("Este mes tiene 28 o 29 días.")
else:
    print("ERROR: número de mes incorrecto.")
