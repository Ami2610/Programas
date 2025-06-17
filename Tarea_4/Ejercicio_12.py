# Ejercicio 12
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

# Se pide el día, mes y año al usuario
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

# Asumimos que la fecha es válida por defecto
valido = True

# Comprobamos si el mes está en el rango correcto
if mes < 1 or mes > 12:
    valido = False
# Comprobamos si el día es válido para el mes dado
elif dia < 1:
    valido = False
elif mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31:
    valido = False
elif mes in [4, 6, 9, 11] and dia > 30:
    valido = False
elif mes == 2:
    # Verificamos si el año es bisiesto
    es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    if (es_bisiesto and dia > 29) or (not es_bisiesto and dia > 28):
        valido = False

# Mostramos si la fecha es válida o no
if valido:
    print("La fecha es correcta.")
else:
    print("La fecha no es válida.")
