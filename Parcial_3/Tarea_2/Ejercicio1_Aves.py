# Creacion de la clase padre Ave
class Ave:
    def __init__(self, nombre):
        self.nombre = nombre

    def volar(self):
        print(f"{self.nombre} está volando.")

# Creación de clases hijas Aguila y Pinguino que heredan de Ave
class Aguila(Ave):
    def volar(self):
        print("El águila vuela alto.")

class Pinguino(Ave):
    def volar(self):
        print("El pingüino no puede volar.")

# Creación de objetos de las clases hijas
aguila = Aguila("Águila Real")
pinguino = Pinguino("Pingüino Emperador")

# Llamar al método volar para cada ave
aguila.volar()
pinguino.volar()
