# Ejercicio 15
# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 €, y así sucesivamente. 
# Realiza un algoritmo para determinar el pago mensual y el total después de los 20 meses.

# Inicializamos variables
pago_mensual = 10  # Primer pago
total_pagado = 0

print("Pagos mensuales durante 20 meses:")

# Recorremos los 20 meses
for mes in range(1, 21):
    print(f"Mes {mes}: ${pago_mensual} ")
    total_pagado += pago_mensual  # Sumamos al total
    pago_mensual *= 2  # El siguiente mes se paga el doble

# Mostramos el total pagado al final de los 20 meses
print(f"\nTotal pagado después de 20 meses: ${total_pagado} ")
