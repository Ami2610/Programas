class Vuelo:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.asientos = []

    def info(self):
        return f"Vuelo de {self.origen} a {self.destino}"

    def total_asientos(self):
        return len(self.asientos)

class VueloTurista(Vuelo):
    def __init__(self, origen, destino):
        super().__init__(origen, destino)
        self.asientos = [0] * 30

    def clase(self):
        return "Clase Turista"

class VueloBusiness(Vuelo):
    def __init__(self, origen, destino):
        super().__init__(origen, destino)
        self.asientos = [0] * 10

    def clase(self):
        return "Clase Business"

def inicializar_vuelos():
    vuelo1 = VueloTurista("Quito", "Guayaquil")
    vuelo2 = VueloBusiness("Quito", "Guayaquil")
    print(vuelo1.info(), "-", vuelo1.clase(), "-", vuelo1.total_asientos(), "asientos")
    print(vuelo2.info(), "-", vuelo2.clase(), "-", vuelo2.total_asientos(), "asientos")
