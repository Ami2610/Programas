# Ejercicio 16
# Calcular el tiempo (en minutos) en que un vehículo más rápido alcanza a otro, dada la distancia d y velocidades v1 y v2.

# Pedir la distancia entre los dos vehículos (en kilómetros)
distancia = float(input("Ingresa la distancia entre los dos vehículos (km): "))

# Pedir las velocidades (v1 más lento, v2 más rápido)
velocidad_lento = float(input("Ingresa la velocidad del vehículo más lento (km/h): "))
velocidad_rapido = float(input("Ingresa la velocidad del vehículo más rápido (km/h): "))

# Calcular la diferencia de velocidad
diferencia_velocidad = velocidad_rapido - velocidad_lento

# Verificar que el más rápido realmente tenga mayor velocidad
if diferencia_velocidad <= 0:
    print("El vehículo más rápido debe tener mayor velocidad que el lento.")
else:
    # Calcular el tiempo en horas que tardará en alcanzarlo
    tiempo_horas = distancia / diferencia_velocidad

    # Convertir el tiempo a minutos
    tiempo_minutos = tiempo_horas * 60

    # Mostrar el resultado
    print(f"El vehículo más rápido alcanzará al más lento en {tiempo_minutos:.2f} minutos.")