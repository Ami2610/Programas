# Ejercicio 7
# Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. 
# Pueden ocurrir tres cosas:
    # El exponente sea positivo, sólo tienes que imprimir la potencia.
    # El exponente sea 0, el resultado es 1.
    # El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

# Pedimos al usuario que introduzca la base
base = float(input("Introduce la base: "))

# Pedimos al usuario que introduzca el exponente
exponente = int(input("Introduce el exponente: "))

# Si el exponente es positivo, se calcula la potencia normalmente
if exponente > 0:
    resultado = pow(base, exponente)
# Si el exponente es 0, el resultado es 1 por definición
elif exponente == 0:
    resultado = 1
# Si el exponente es negativo, se calcula la inversa de la potencia positiva
else:
    resultado = 1 / pow(base, abs(exponente))

# Se muestra el resultado final
print("El resultado es:", resultado)
