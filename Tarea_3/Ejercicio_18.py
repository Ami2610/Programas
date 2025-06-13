# Ejercicio 18
# Mostrar las iniciales de una persona a partir de su nombre y dos apellidos.

# Pedir al usuario el nombre y los dos apellidos
nombre = input("Ingresa tu nombre: ")
apellido_1 = input("Ingresa tu primer apellido: ")
apellido_2 = input("Ingresa tu segundo apellido: ")

# Obtener las iniciales en mayúsculas
iniciales = nombre[0].upper() + apellido_1[0].upper() + apellido_2[0].upper()

# Mostrar las iniciales
print(f"Iniciales: {iniciales}")