# Ejercicio 17
# Determinar la hora de llegada a una ciudad B, dada la hora de salida de A (HH:MM:SS)
# y el tiempo de viaje en segundos.

# Pedir la hora de salida en formato HH:MM:SS
hora_salida = input("Ingresa la hora de salida (HH:MM:SS): ")

# Pedir el tiempo de viaje en segundos
tiempo_viaje_segundos = int(input("Ingresa el tiempo de viaje en segundos: "))

# Separar la hora, los minutos y los segundos
horas, minutos, segundos = map(int, hora_salida.split(":"))

# Convertir todo a segundos
segundos_totales_salida = horas * 3600 + minutos * 60 + segundos

# Sumar el tiempo de viaje
segundos_totales_llegada = segundos_totales_salida + tiempo_viaje_segundos

# Calcular la nueva hora de llegada
hora_llegada = (segundos_totales_llegada // 3600) % 24
minuto_llegada = (segundos_totales_llegada % 3600) // 60
segundo_llegada = segundos_totales_llegada % 60

# Mostrar la hora de llegada con formato HH:MM:SS
print(f"Hora de llegada: {hora_llegada:02d}:{minuto_llegada:02d}:{segundo_llegada:02d}")