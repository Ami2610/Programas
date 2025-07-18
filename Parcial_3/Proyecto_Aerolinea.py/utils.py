class Validador:
    @staticmethod
    def validar_entrada(opcion, opciones_validas):
        """Valida si la opción ingresada está en el conjunto permitido."""
        return opcion in opciones_validas

    @staticmethod
    def validar_edad(edad):
        """Valida si la edad es un número entero no negativo."""
        try:
            return int(edad) >= 0
        except ValueError:
            return False
