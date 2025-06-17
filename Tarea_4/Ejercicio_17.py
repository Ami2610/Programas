# Ejercicio 17
# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número
# nos da un error.

# Se solicita un número del 1 al 7
numero_dia = int(input("Introduce el número del día (1-7): "))

# Diccionario que asocia número con día de la semana
dias_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Verificamos si el número está en el rango permitido
if numero_dia in dias_semana:
    print(f"El día correspondiente es: {dias_semana[numero_dia]}")
else:
    print("ERROR: número de día incorrecto.")
