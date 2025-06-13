# Ejercicio 2
# Calcular el perímetro y área de un rectángulo dada su base y su altura.

# Solicita al usuario que ingrese la base del rectángulo y la convierte a número decimal
base_rectangulo = float(input("Ingrese la base del rectángulo: "))

# Solicita al usuario que ingrese la altura del rectángulo y la convierte a número decimal
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Calcula el perímetro del rectángulo usando la fórmula: 2 * (base + altura)
perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)

# Calcula el área del rectángulo usando la fórmula: base * altura
area_rectangulo = base_rectangulo * altura_rectangulo

# Muestra el resultado del perímetro en pantalla
print("El perímetro del rectángulo es:", perimetro_rectangulo)

# Muestra el resultado del área en pantalla
print("El área del rectángulo es:", area_rectangulo)