# Importa la clase Personaje desde el archivo Character.py
from Character import Personaje

# Importa la clase MagicItem desde el archivo Magic_Item.py
from Magic_Item import MagicItem

# Definimos la clase Juego, que controla la lógica del juego
class Juego:

    # Constructor del juego: crea los personajes y los objetos mágicos
    def __init__(self):
        # Crea al personaje del jugador (héroe)
        self.heroe = Personaje("Kratos", 100, 20, 1)
        
        # Crea al enemigo que enfrentará el jugador
        self.enemigo = Personaje("Monstruo", 125, 15, 2)
        
        # Crea una poción que puede usar el héroe para curarse
        self.pocion = MagicItem("Poción de curación", "pocion", 30)
        
        # Crea un arma que puede usar el héroe para aumentar su ataque
        self.arma = MagicItem("Hacha mágica", "arma", 10)

    # Método principal que inicia y controla el desarrollo del juego
    def iniciar(self):
        print("¡Bienvenido a las Aventuras en el Reino Encantado!\n")
        
        # Muestra el estado inicial de los personajes
        self.heroe.estado()
        self.enemigo.estado()

        turnos = 0  # Contador de turnos
        # El juego continúa mientras los dos personajes estén vivos y no se excedan los 10 turnos
        while self.heroe.vida > 0 and self.enemigo.vida > 0 and turnos < 10:
            print("\n¿Qué acción deseas hacer?")
            print("1. Atacar al Monstruo")
            print("2. Usar poción de curación")
            print("3. Usar Hacha mágica")

            # Solicita al jugador una opción
            opcion = int(input("Selecciona una opción (1-3): "))

            # Según la opción elegida, se realiza una acción
            if opcion == 1:
                self.heroe.atacar(self.enemigo)  # El héroe ataca al enemigo
            elif opcion == 2:
                self.pocion.usar(self.heroe)     # El héroe usa la poción para curarse
            elif opcion == 3:
                self.arma.usar(self.heroe)       # El héroe usa el arma para aumentar su ataque
            else:
                print("Opción no válida.")       # Manejo de opciones incorrectas

            # Si el enemigo aún está vivo, contraataca
            if self.enemigo.vida > 0:
                self.enemigo.atacar(self.heroe)

            # Muestra el estado actual de ambos personajes después del turno
            print("\n--- Estado Actual ---")
            self.heroe.estado()
            self.enemigo.estado()
            turnos += 1  # Se suma un turno

        # Al final del juego, se muestra quién ganó
        print("\n--- Game Over ---")
        if self.heroe.vida > self.enemigo.vida:
            print(f"¡Has vencido al Monstruo!")
        else:
            print("El Monstruo te ha derrotado ¡Inténtalo de nuevo!")
