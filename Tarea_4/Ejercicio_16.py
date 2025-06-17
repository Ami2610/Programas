# Ejercicio 16
# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por 
# pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
# Ejemplo:
# Introduzca número del dado: 5
# En la cara opuesta está el "dos".


# Se pide al usuario un número entre 1 y 6
numero_dado = int(input("Introduce el número del dado (1-6): "))

# Diccionario con las caras opuestas del dado
caras_opuestas = {
    1: "seis",
    2: "cinco",
    3: "cuatro",
    4: "tres",
    5: "dos",
    6: "uno"
}

# Se verifica si el número está en el rango permitido
if numero_dado in caras_opuestas:
    print(f"En la cara opuesta está el \"{caras_opuestas[numero_dado]}\".")
else:
    print("ERROR: número incorrecto.")
