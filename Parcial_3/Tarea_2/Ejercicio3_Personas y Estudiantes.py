# Creación de la clase padre Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Creación de la clase hija Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
        super().presentarse()  # Llamamos al método de Persona
        print(f"Estudio la carrera de {self.carrera}.")

# Instancias y uso de los métodos
persona1 = Persona("Ana", 30)
estudiante1 = Estudiante("Luis", 20, "Ingeniería")

persona1.presentarse()
estudiante1.presentarse()
