# Ejercicio 7
# Convertir una cantidad de minutos a horas y minutos.

# Pedir al usuario la cantidad de minutos
minutos_totales = int(input("Ingresa la cantidad de minutos: "))

# Calcular la cantidad de horas (división entera)
horas = minutos_totales // 60

# Calcular los minutos restantes (residuo de la división)
minutos_restantes = minutos_totales % 60

# Mostrar el resultado
print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos_restantes} minutos.")