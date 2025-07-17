# Ejercicio 2
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación, 
# va pidiendo números y respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que
# quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (y te dice en cuántos intentos 
# lo has logrado) o si se llega al límite de intentos, mostrando el número generado.

import random  # Importamos el módulo para generar números aleatorios

# Generamos un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Definimos el número máximo de intentos
intentos_maximos = 10

# Contador de intentos realizados
intentos_realizados = 0

print("Adivina el número (entre 1 y 100). Tienes 10 intentos.")

# Bucle que se repite hasta que se acierte o se acaben los intentos
while intentos_realizados < intentos_maximos:
    intento = int(input("Introduce un número: "))
    intentos_realizados += 1  # Aumentamos el contador de intentos

    # Comprobamos si el número introducido es igual al secreto
    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos_realizados} intentos.")
        break  # Salimos del bucle si se adivina el número
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    
    # Mostrar cuántos intentos quedan
    print(f"Te quedan {intentos_maximos - intentos_realizados} intentos.\n")

# Si no se adivina en los intentos disponibles
if intento != numero_secreto:
    print(f"Lo siento, no lograste adivinar el número. Era {numero_secreto}.")
