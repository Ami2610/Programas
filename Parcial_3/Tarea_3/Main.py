# Importamos la clase Juego desde el archivo Game.py
from Game import Juego

# Este bloque se ejecuta solo si este archivo se ejecuta directamente (no si se importa desde otro archivo)
if __name__ == "__main__":
    
    # Se crea una instancia del juego
    game = Juego()

    # Se inicia el juego llamando al método iniciar()
    game.iniciar()
