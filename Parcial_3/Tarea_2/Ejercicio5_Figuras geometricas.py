import math

# Creación de la clase padre Figura
class Figura:
    def calcular_area(self):
        pass  # Método vacío, se implementará en las subclases

# Creación de la clase hija Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

# Creación de la clase hija Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Crear lista de figuras
figuras = [
    Cuadrado(4),
    Circulo(3),
    Cuadrado(7),
    Circulo(5)
]

# Aplicar polimorfismo
for figura in figuras:
    area = figura.calcular_area()
    print(f"Área: {area:.2f}")
