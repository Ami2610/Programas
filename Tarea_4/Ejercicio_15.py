# Ejercicio 15
# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
# de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 
# 70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es 
# otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por 
# cada concepto una persona que realiza una llamada.

# Se pide la duración de la llamada en minutos
duracion = int(input("Introduce la duración de la llamada en minutos: "))

# Se pide el día de la llamada
dia = input("Introduce el día (domingo/otro): ").lower()

# Si no es domingo, también se pide el turno
turno = ""
if dia != "domingo":
    turno = input("Introduce el turno (mañana/tarde): ").lower()

# Inicializamos el costo
costo = 0

# Calculamos el costo por bloques de tiempo
if duracion > 10:
    costo += (duracion - 10) * 0.50
    duracion = 10
if duracion > 8:
    costo += (duracion - 8) * 0.70
    duracion = 8
if duracion > 5:
    costo += (duracion - 5) * 0.80
    duracion = 5
costo += duracion * 1.00

# Calculamos el impuesto según el día y el turno
if dia == "domingo":
    impuesto = costo * 0.03
elif turno == "mañana":
    impuesto = costo * 0.15
else:
    impuesto = costo * 0.10

# Calculamos el total con impuestos
total = costo + impuesto

# Mostramos todos los detalles
print("Costo base: {:.2f} euros".format(costo))
print("Impuesto: {:.2f} euros".format(impuesto))
print("Costo total: {:.2f} euros".format(total))
