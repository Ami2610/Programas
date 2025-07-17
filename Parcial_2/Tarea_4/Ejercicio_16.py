# Ejercicio 16
# Una empresa paga a sus empleados con base en las horas trabajadas en la semana. Realiza un algoritmo para determinar el sueldo semanal 
# de N trabajadores y el total pagado por la empresa.

# Pedimos al usuario cuántos trabajadores hay
n = int(input("Introduce la cantidad de trabajadores: "))

# Inicializamos el total que pagará la empresa
total_pagado = 0

# Recorremos cada trabajador
for i in range(1, n + 1):
    print(f"\nTrabajador {i}:")
    horas = float(input("  Horas trabajadas esta semana: "))
    tarifa = float(input("  Pago por hora: $"))
    
    sueldo = horas * tarifa  # Calculamos el sueldo individual
    total_pagado += sueldo   # Lo sumamos al total

    print(f"  Sueldo semanal: ${sueldo:.2f} ")

# Mostramos el total pagado por la empresa
print(f"\nTotal pagado por la empresa a los {n} trabajadores: ${total_pagado:.2f} ")
