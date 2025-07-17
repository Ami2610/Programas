# Ejercicio 19
# Calcular la nota final de un estudiante según:
# - Respuesta correcta: +5 puntos.
# - Respuesta incorrecta: -1 punto.
# - Respuesta en blanco: 0 puntos.

# Pedir la cantidad de respuestas de cada tipo
respuestas_correctas = int(input("Cantidad de respuestas correctas: "))
respuestas_incorrectas = int(input("Cantidad de respuestas incorrectas: "))
respuestas_blanco = int(input("Cantidad de respuestas en blanco: "))

# Calcular la nota final con base en la puntuación indicada
nota_final = (respuestas_correctas * 5) + (respuestas_incorrectas * -1) + (respuestas_blanco * 0)

# Mostrar la nota final
print(f"Nota final del estudiante: {nota_final}")