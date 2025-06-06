# “Mini tienda: cálculo de ventas y salud”

# Se pide el nombre del usuario
nombre = str(input("Ingrese su nombre: "))

# Se piden peso y altura para calcular el índice de masa corporal (IMC)
peso = float(input("Ingrese su peso (en kg): "))
altura = float(input("Ingrese su altura (en m): "))
imc = round((peso / altura ** 2), 2)  # Fórmula del IMC, redondeado a 2 decimales

# Se pide cuántas barras de pan antiguas se vendieron
barras_antiguas = int(input("Ingrese la cantidad de barras de pan antiguas vendidas: "))
precio_habitual = 3.49  # Precio normal de cada barra
descuento = 0.60  # 60% de descuento
descuento_por_barra = precio_habitual * descuento  # Cuánto se descuenta por barra
precio_descuento = barras_antiguas * (precio_habitual - descuento_por_barra)  # Precio total con descuento


# Se simula el interés de una cuenta de ahorros
valor_depositado = float(input("Ingrese el valor depositado: $"))
interes = 0.04  # 4% de interés anual
balance_año1 = valor_depositado * (1 + interes)  # Saldo tras 1 año
balance_año2 = balance_año1 * (1 + interes)  # Saldo tras 2 años
balance_año3 = balance_año2 * (1 + interes)  # Saldo tras 3 años
print()

#Se muestra un resumen de los todos los datos calculados
print("¡Hola", nombre + "!")
print()

print("Tu índice de masa corporal es: " + str(imc))
print()

print("Has vendido", barras_antiguas, "barras de pan del día anterior.")
print("Precio habitual de la barra de pan: $" + str(precio_habitual))
print("Descuento por barra: $" + str(round(descuento_por_barra, 2)))
print("Precio final: $" + str(round(precio_descuento, 2)))
print()

print("Has depositado $"+ str(round(valor_depositado, 2)), "en tu cuenta de ahorros.")
print("Saldo después del primer año: $" + str(round(balance_año1, 2)))
print("Saldo después del segundo año: $" + str(round(balance_año2, 2)))
print("Saldo después del tercer año: $" + str(round(balance_año3, 2)))
print()

# Mensaje de despedida
print("¡Gracias por usar el sistema!")