# Creación de la clase padre Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, velocidad = 0):
        self.__marca = marca         # Atributo privado
        self.__modelo = modelo       # Atributo privado
        self.__velocidad = velocidad # Atributo privado

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, nueva_velocidad):
        self.__velocidad = nueva_velocidad

# Creación de la clase hija Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def acelerar(self, incremento = 10):
        nueva_velocidad = self.get_velocidad() + incremento
        self.set_velocidad(nueva_velocidad)
        print(f"El auto ha acelerado. Nueva velocidad: {self.get_velocidad()} km/h")

# Ejemplo de uso
auto1 = Auto("Toyota", "Corolla")
print("Velocidad inicial:", auto1.get_velocidad())
auto1.acelerar()
auto1.acelerar(20)
print("Velocidad final:", auto1.get_velocidad())