# Ejercicio 5
# Algoritmo que pide caracteres e imprime "VOCAL" si son vocales y "NO VOCAL" en caso contrario. El programa termina cuando se 
# introduce un espacio.

print("Introduce caracteres uno a uno. Introduce un espacio para terminar.")

while True:
    caracter = input("Introduce un carácter: ")

    # Validamos que solo se ingrese un carácter
    if len(caracter) != 1:
        print("Por favor, introduce solo un carácter.")
        continue

    # Si se introduce un espacio, terminamos el programa
    if caracter == ' ':
        print("Programa terminado.")
        break

    # Convertimos a minúscula para facilitar la comparación
    caracter = caracter.lower()

    # Verificamos si es una vocal
    if caracter in 'aeiou':
        print("VOCAL")
    else:
        print("NO VOCAL")
