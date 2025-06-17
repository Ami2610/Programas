# Ejercicio 6:
# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

# Pedimos al usuario que introduzca una letra
letra = input("Introduce una letra: ")

# Verificamos si la letra es mayúscula y solo hay un carácter
if letra.isupper() and len(letra) == 1:
    print("Es una letra mayúscula.")
else:
    print("No es una letra mayúscula.")
