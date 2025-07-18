from vuelos import inicializar_vuelos
from reservas import reservar_asiento
from pasajeros import listar_pasajeros
from ingresos import calcular_ingresos
from utils import Validador 

class AplicacionConsola:
    def __init__(self):
        self.opciones_validas = ['1', '2', '3', '4', '5', '6']
        self.ejecutar_menu()

    def mostrar_menu(self):
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Inicializar Vuelos")
        print("2. Reservar Asiento")
        print("3. Ver Mapa de Asientos (por implementar)")
        print("4. Listar Pasajeros")
        print("5. Calcular Ingresos")
        print("6. Salir")

    def ejecutar_menu(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if not Validador.validar_entrada(opcion, self.opciones_validas):
                print("Opción inválida. Intente de nuevo.")
                continue

            if opcion == '1':
                inicializar_vuelos()
            elif opcion == '2':
                reservar_asiento()
            elif opcion == '4':
                listar_pasajeros()
            elif opcion == '5':
                calcular_ingresos()
            elif opcion == '6':
                print("Fin de la ejecución.")
                break

if __name__ == "__main__":
    AplicacionConsola()
