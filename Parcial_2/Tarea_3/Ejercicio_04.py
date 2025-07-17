# Ejercicio 4 
# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, 
# o un mensaje de aviso en caso contrario.

# Solicitamos el número que será el dividendo
dividendo = float(input("Introduce el dividendo: "))

# Solicitamos el número que será el divisor
divisor = float(input("Introduce el divisor: "))

# Verificamos si el divisor es diferente de cero
if divisor != 0:
    # Si se puede dividir, mostramos el resultado
    print("Resultado de la división:", dividendo / divisor)
else:
    # Si no se puede dividir, mostramos un mensaje de error
    print("No se puede dividir entre cero.")
