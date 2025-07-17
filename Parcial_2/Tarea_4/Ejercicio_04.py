# Ejercicio 4
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar 
# cuántos números introducidos son mayores que 0, menores que 0 e iguales a 0.

# Pedimos al usuario cuántos números quiere introducir
cantidad = int(input("¿Cuántos números vas a introducir?: "))

# Inicializamos contadores para positivos, negativos y ceros
mayores_que_cero = 0
menores_que_cero = 0
iguales_a_cero = 0

# Bucle que se repite según la cantidad ingresada
for i in range(cantidad):
    numero = float(input(f"Introduce el número {i + 1}: "))  # Se permite decimal

    # Clasificamos el número según su valor
    if numero > 0:
        mayores_que_cero += 1
    elif numero < 0:
        menores_que_cero += 1
    else:
        iguales_a_cero += 1

# Mostramos los resultados
print("\nResultados:")
print(f"Números mayores que 0: {mayores_que_cero}")
print(f"Números menores que 0: {menores_que_cero}")
print(f"Números iguales a 0: {iguales_a_cero}")
