# Ejercicio 19
# Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, 
# América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona 
# a la que va dirigido. Lo anterior se muestra en la tabla:
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones
# de logística y de seguridad. Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su 
# caso, el rechazo de la entrega.

# Se solicita el peso del paquete
peso = float(input("Introduce el peso del paquete en kg: "))

# Se solicita la zona a la que se enviará el paquete
zona = input("Introduce la zona (norte, centro, sur, europa, asia): ").lower()

# Diccionario con el precio por kilo para cada zona
precios_por_kg = {
    "norte": 24.00,
    "centro": 20.00,
    "sur": 21.00,
    "europa": 10.00,
    "asia": 18.00
}

# Si el paquete excede el peso máximo permitido, se rechaza
if peso > 5:
    print("El paquete no puede ser transportado por exceder el peso máximo.")
# Verificamos si la zona es válida
elif zona not in precios_por_kg:
    print("Zona no válida.")
else:
    # Calculamos el costo total según el peso y la zona
    costo_total = peso * precios_por_kg[zona]
    print(f"El costo de envío es: {costo_total:.2f} euros.")
