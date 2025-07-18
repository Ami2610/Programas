from utils import Validador

class Pasajero:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_menor(self):
        return self.edad < 18

def listar_pasajeros():
    print("Función para listar pasajeros")

    nombre = input("Ingrese nombre del pasajero: ")
    edad_input = input("Ingrese edad del pasajero: ")

    if Validador.validar_edad(edad_input):
        edad = int(edad_input)
        pasajero = Pasajero(nombre, edad)
        print(f"Pasajero: {pasajero.nombre} ({pasajero.edad} años) - Menor de edad: {pasajero.es_menor()}")
    else:
        print("Edad inválida. Debe ser un número entero no negativo.")
