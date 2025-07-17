# Ejercicio 19
# Realiza un ejemplo de menú con distintas opciones hasta seleccionar "Salir".

# Bucle que mantiene el menú activo hasta que el usuario elija salir
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Saludar")
    print("2. Mostrar una suma")
    print("3. Decir la hora (simulada)")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        print("¡Hola! Gracias por usar el menú.")
    elif opcion == "2":
        print(f"La suma de 3 + 5 es {3 + 5}")
    elif opcion == "3":
        print("La hora actual es: 12:34 (simulada)")  # Puedes usar datetime para obtener la real
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta pronto!")
        break  # Termina el bucle y el programa
    else:
        print("Opción no válida. Intenta de nuevo.")
