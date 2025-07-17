# Definimos la clase Personaje, que representa a un personaje de un juego
class Personaje:
    
    # Método constructor: se ejecuta al crear una nueva instancia de la clase
    def __init__(self, nombre, vida, ataque, nivel):
        self.nombre = nombre    # Nombre del personaje
        self.vida = vida        # Cantidad de vida o salud del personaje
        self.ataque = ataque    # Valor de daño que el personaje puede causar
        self.nivel = nivel      # Nivel del personaje (puede reflejar experiencia o poder)

    # Método para atacar a otro personaje
    def atacar(self, personaje2):
        # Imprime quién ataca a quién y cuántos puntos de daño causa
        print(f"{self.nombre} ataca a {personaje2.nombre} y causa {self.ataque} puntos de daño.")
        
        # Resta los puntos de ataque a la vida del personaje atacado
        personaje2.vida -= self.ataque

        # Si la vida del personaje atacado baja de 0, se ajusta a 0 para evitar valores negativos
        if personaje2.vida < 0:
            personaje2.vida = 0

    # Método para mostrar el estado actual del personaje
    def estado(self):
        # Imprime el nombre, vida, nivel y ataque del personaje
        print(f"{self.nombre} - Vida: {self.vida} | Nivel: {self.nivel} | Ataque: {self.ataque}")
