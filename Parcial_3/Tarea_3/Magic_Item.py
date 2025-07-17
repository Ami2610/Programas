# Definimos la clase MagicItem, que representa un objeto mágico en un juego
class MagicItem:
    
    # Método constructor: se ejecuta al crear un nuevo objeto de tipo MagicItem
    def __init__(self, nombre, tipo, efecto):
        self.nombre = nombre    # Nombre del objeto (ej. "Poción de vida", "Espada mágica")
        self.tipo = tipo        # Tipo del objeto (puede ser "pocion" o "arma")
        self.efecto = efecto    # Valor numérico que representa el efecto del objeto (cuánto cura o cuánto aumenta el ataque)

    # Método para usar el objeto mágico sobre un personaje
    def usar(self, personaje):
        # Si el tipo es "pocion", se usa para recuperar vida
        if self.tipo == "pocion":
            personaje.vida += self.efecto   # Aumenta la vida del personaje en la cantidad del efecto
            print(f"{personaje.nombre} usa {self.nombre} y recupera {self.efecto} puntos de vida.")

        # Si el tipo es "arma", se usa para aumentar el ataque
        elif self.tipo == "arma":
            personaje.ataque += self.efecto  # Aumenta el ataque del personaje en la cantidad del efecto
            print(f"{personaje.nombre} equipa {self.nombre} y su ataque aumenta en {self.efecto} puntos.")
