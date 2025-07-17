# Ejercicio 13
# Una empresa registra las horas trabajadas diariamente por un empleado durante la semana (6 días) y requiere determinar el 
# total de horas trabajadas y el sueldo correspondiente.

# Pedimos al usuario la tarifa por hora
tarifa_hora = float(input("Introduce el pago por hora: "))

# Inicializamos el total de horas trabajadas
total_horas = 0

# Recorremos los 6 días de trabajo
for dia in range(1, 7):
    horas = float(input(f"Introduce las horas trabajadas en el día {dia}: "))
    total_horas += horas  # Acumulamos las horas

# Calculamos el sueldo total
sueldo = total_horas * tarifa_hora

# Mostramos los resultados
print(f"\nTotal de horas trabajadas en la semana: {total_horas} horas")
print(f"Sueldo correspondiente: ${sueldo:.2f} ")
