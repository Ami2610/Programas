# Ejercicio 20
# Calcular el dinero total en euros y céntimos a partir de monedas de:
# 2€, 1€, 50¢, 20¢ y 10¢.

# Pedir la cantidad de cada tipo de moneda
monedas_2e = int(input("Cantidad de monedas de 2€: "))
monedas_1e = int(input("Cantidad de monedas de 1€: "))
monedas_50c = int(input("Cantidad de monedas de 50¢: "))
monedas_20c = int(input("Cantidad de monedas de 20¢: "))
monedas_10c = int(input("Cantidad de monedas de 10¢: "))

# Calcular el total en céntimos
total_centimos = (
    monedas_2e * 200 +
    monedas_1e * 100 +
    monedas_50c * 50 +
    monedas_20c * 20 +
    monedas_10c * 10
)

# Convertir a euros y céntimos
euros = total_centimos // 100
centimos = total_centimos % 100

# Mostrar el resultado
print(f"Total: {euros} euros y {centimos} céntimos")