# Creación de la clase Mascota
# Esta clase representa una mascota con nombre, especie y edad.
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, soy un/a {self.especie} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")

# Crear objetos de la clase Mascota
mascota1 = Mascota("Luna", "perra", 3)
mascota2 = Mascota("Milo", "gato", 2)
mascota3 = Mascota("Rocky", "hamster", 1)

# Llamar al método presentarse para cada mascota
mascota1.presentarse()
mascota2.presentarse()
mascota3.presentarse()

# Llamar al método cumplir_anios
mascota1.cumplir_anios()
mascota2.cumplir_anios()
mascota3.cumplir_anios()