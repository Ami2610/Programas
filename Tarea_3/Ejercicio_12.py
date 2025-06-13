# Ejercicio 12
# Calcular la distancia entre dos puntos (x1, y1) y (x2, y2) en el plano.

import math  # Importamos la biblioteca para usar la función sqrt

# Pedir las coordenadas del primer punto
x1 = float(input("Ingresa la coordenada x1: "))
y1 = float(input("Ingresa la coordenada y1: "))

# Pedir las coordenadas del segundo punto
x2 = float(input("Ingresa la coordenada x2: "))
y2 = float(input("Ingresa la coordenada y2: "))

# Calcular la distancia usando la fórmula
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar el resultado
print(f"Distancia entre los dos puntos: {distancia}")