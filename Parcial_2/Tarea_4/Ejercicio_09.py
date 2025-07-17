# Ejercicio 9
# Escribe un programa que, dados dos números (uno real como base y un entero positivo como exponente), muestre el resultado de 
# la potencia. No se puede utilizar el operador de potencia.

# Pedimos la base (puede ser número decimal) y el exponente (entero positivo)
base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero positivo): "))

# Validamos que el exponente sea positivo
if exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    resultado = 1  # Inicializamos el resultado

    # Multiplicamos la base por sí misma exponente veces
    for _ in range(exponente):
        resultado *= base

    # Mostramos el resultado final
    print(f"{base} elevado a {exponente} es {resultado}")
