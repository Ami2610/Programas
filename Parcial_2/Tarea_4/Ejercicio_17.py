# Ejercicio 17
# Similar al ejercicio 16, pero registrando los días trabajados y las horas de cada día. Calcula el sueldo semanal de N trabajadores y 
# el total pagado por la empresa.

# Pedimos la cantidad de trabajadores
n = int(input("Introduce la cantidad de trabajadores: "))

# Inicializamos el total que pagará la empresa
total_pagado = 0

# Recorremos cada trabajador
for i in range(1, n + 1):
    print(f"\nTrabajador {i}:")
    tarifa = float(input("  Pago por hora: "))
    dias = int(input("  ¿Cuántos días trabajó esta semana?: "))
    
    horas_totales = 0  # Acumulador de horas por semana

    # Recorremos los días trabajados
    for d in range(1, dias + 1):
        horas_dia = float(input(f"    Horas trabajadas en el día {d}: "))
        horas_totales += horas_dia

    sueldo = horas_totales * tarifa  # Calculamos el sueldo semanal
    total_pagado += sueldo           # Lo sumamos al total general

    print(f"  Horas totales: {horas_totales} horas")
    print(f"  Sueldo semanal: {sueldo:.2f} €")

# Mostramos el total pagado por la empresa
print(f"\nTotal pagado por la empresa a los {n} trabajadores: {total_pagado:.2f} €")
