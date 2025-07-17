# Ejercicio 8
# Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior, debe volver a pedirlo. A continuación, se introducen números hasta ingresar un 0. Al final, el programa debe mostrar:
# •	La suma de los números dentro del intervalo (intervalo abierto).
# •	Cuántos números están fuera del intervalo.
# •	Si se introdujo algún número igual a los límites del intervalo.

# Pedimos los límites del intervalo y validamos que el inferior sea menor que el superior
while True:
    limite_inferior = int(input("Introduce el límite inferior: "))
    limite_superior = int(input("Introduce el límite superior: "))
    if limite_inferior < limite_superior:
        break
    else:
        print("El límite inferior debe ser menor que el límite superior. Intenta de nuevo.\n")

# Inicializamos variables
suma_dentro = 0
fuera_intervalo = 0
igual_a_limite = False

print("\nIntroduce números (0 para terminar):")

while True:
    numero = int(input("Número: "))
    
    if numero == 0:
        break  # Finaliza la entrada de datos

    if limite_inferior < numero < limite_superior:
        suma_dentro += numero  # Acumula si está dentro del intervalo abierto
    else:
        fuera_intervalo += 1  # Cuenta si está fuera del intervalo

    # Verificamos si coincide con algún límite
    if numero == limite_inferior or numero == limite_superior:
        igual_a_limite = True

# Mostramos los resultados
print("\nResultados:")
print(f"Suma de los números dentro del intervalo: {suma_dentro}")
print(f"Cantidad de números fuera del intervalo: {fuera_intervalo}")
if igual_a_limite:
    print("Se introdujo al menos un número igual a uno de los límites.")
else:
    print("No se introdujo ningún número igual a los límites.")
