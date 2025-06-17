# Ejercicio 13
# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, 
# y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar 
# cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A, se le cargan 
# 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos 
# cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

# Se pide el tipo de uva
tipo = input("Introduce el tipo de uva (A/B): ").upper()

# Se pide el tamaño de la uva
tamano = int(input("Introduce el tamaño de la uva (1/2): "))

# Se pide el precio inicial por kilo
precio_inicial = float(input("Introduce el precio inicial por kilo: "))

# Se pide la cantidad de kilos entregados
kilos = float(input("Introduce los kilos entregados: "))

# Se ajusta el precio según el tipo y tamaño
if tipo == "A":
    if tamano == 1:
        precio_inicial += 0.20
    elif tamano == 2:
        precio_inicial += 0.30
elif tipo == "B":
    if tamano == 1:
        precio_inicial -= 0.30
    elif tamano == 2:
        precio_inicial -= 0.50

# Se calcula la ganancia total
ganancia = precio_inicial * kilos

# Se muestra el resultado
print("Ganancia obtenida: {:.2f} euros".format(ganancia))
