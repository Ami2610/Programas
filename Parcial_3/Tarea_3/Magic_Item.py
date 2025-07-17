# Definimos la clase MagicItem, que representa un objeto mágico en un juego
class MagicItem:
    
    # Método constructor: se ejecuta al crear un nuevo objeto de tipo MagicItem
    def __init__(self, nombre, tipo, efecto):
        self.nombre = nombre    # Nombre del objeto (ej. "Poción de curación", "Hacha mágica")
        self.tipo = tipo        # Tipo del objeto (puede ser "pocion" o "arma")
        self.efecto = efecto    # Valor numérico que representa el efecto del objeto (cuánto cura o cuánto aumenta el daño)

    # Método para usar el objeto mágico sobre un personaje
    def usar(self, personaje):
        
        # Si el tipo es "pocion", se usa para recuperar vida
        if self.tipo == "pocion":
            # Verifica si el personaje ya tiene la vida al máximo
            if personaje.vida >= 100:
                print(f"{personaje.nombre} ya tiene la vida al máximo. La poción no tuvo efecto.")
            else:
                vida_inicial = personaje.vida   # Guarda la vida actual del personaje antes de curar
                personaje.vida = min(personaje.vida + self.efecto, 100)  # Suma el efecto, pero no permite pasar de 100
                vida_recuperada = personaje.vida - vida_inicial          # Calcula cuánta vida se recuperó realmente
                print(f"{personaje.nombre} toma {self.nombre} y recupera {vida_recuperada} puntos de vida.")

        # Si el tipo es "arma", se usa para aumentar el daño
        elif self.tipo == "arma":
            personaje.daño += self.efecto   # Aumenta el daño del personaje en la cantidad del efecto
            print(f"{personaje.nombre} equipa {self.nombre} y su daño aumenta en {self.efecto} puntos.")
