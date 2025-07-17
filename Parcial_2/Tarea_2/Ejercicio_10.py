# Ejercicio 10
# Calcular la calificación final de un alumno en Algoritmos, considerando:
# - 55% del promedio de tres parciales
# - 30% del examen final
# - 15% del trabajo final

# Pedir las calificaciones de los tres parciales
parcial_1 = float(input("Ingresa la calificación del primer parcial: "))
parcial_2 = float(input("Ingresa la calificación del segundo parcial: "))
parcial_3 = float(input("Ingresa la calificación del tercer parcial: "))

# Calcular el promedio de los parciales
promedio_parciales = (parcial_1 + parcial_2 + parcial_3) / 3

# Pedir las calificaciones del examen final y del trabajo final
examen_final = float(input("Ingresa la calificación del examen final: "))
trabajo_final = float(input("Ingresa la calificación del trabajo final: "))

# Calcular la calificación final ponderada
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# Mostrar el resultado de forma sencilla
print(f"Calificación final: {calificacion_final}")