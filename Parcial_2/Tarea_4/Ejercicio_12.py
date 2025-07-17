# Ejercicio 12
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año si, al final de cada mes, deposita cantidades 
# variables de dinero. Además, se debe mostrar cuánto lleva ahorrado cada mes.

# Inicializamos la variable que almacenará el total ahorrado
total_ahorrado = 0

# Recorremos los 12 meses del año
for mes in range(1, 13):
    # Pedimos la cantidad ahorrada en ese mes
    cantidad = float(input(f"Introduce la cantidad ahorrada en el mes {mes}: "))
    
    # Sumamos al total
    total_ahorrado += cantidad
    
    # Mostramos el ahorro acumulado hasta ese mes
    print(f"Ahorro acumulado después del mes {mes}: ${total_ahorrado:.2f}\n")

# Al final, mostramos el total ahorrado en el año
print(f"Total ahorrado en el año: ${total_ahorrado:.2f}")
